# coding: utf-8
# bitarrays pickles are smaller, thus faster to pickle
# during tests we find that processes is slightly better than threads for single image compression,
#   due to the fact that a lot of data is been passed into and out of subprocesses
# when compressing multiple images concurrently,
#   data transfer in processes eats up the performance gain
# the best performance is achieved when processing different images in processes,
#   and rows of a image in threads
# this is expected since processes now only have to transfer file paths, which is little data
# By the way, it is bad idea to spawn sub processes in sub processes, like we did in this example,
#   never do this in real life
# It is usually, almost always not clear which concurrency paradime is useful for a specific application,
#   so it is often a good idea to prototype a few different strategies before committing to one
# Other libraries to check:
#   * execnet, a libarary that permits local and remote share-nothing concurrency
#   * Parallel python, an alternative interpreter that can execute threads in parallel
#   * Cython, a python-compatible language that compiles to C and has primitives to release the GIL
#       and take advantage of fully parallel multi-threading
#   * PyPy-STM, an experimental implementation of software transactional memory
#       on top of the ultra-fast PyPy implementation of the Python interpreter
#   * Gevent
import sys
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from pathlib import Path

from PIL import Image
from bitarray import bitarray


def compress_chunk(chunk):
    # run-length encoding
    # intended to compress 127-bit bitarray type chunks,
    #   longer chunks produce meaningless result (overflow)
    # the 127-bit requirement is hard coded with the magic number 128 used in bitwise 'or',
    #   the `|` operator
    compressed = bytearray()
    # start count
    count = 1
    # set init leading bit
    last = chunk[0]
    for bit in chunk[1:]:
        if bit != last:
            # `128 *` makes the 8th bit of the encoded symbol indecates
            #   the `last` leading bit, 1 or 0
            # 1st to 7th bits saves `count`,
            #   so if count > 127, the resulted symbol overflows
            compressed.append(count | (128 * last))  # add a coded symbol
            # reset count
            count = 0
            # reset leading bit
            last = bit
        # continue counting repeated bits
        count += 1
    compressed.append(count | (128 * last))  # add the final coded symbol
    # result is a variable length of run-length symbols, each contains 8 bits (a byte),
    #   the 1st bit tells us the run-length symbol are 1s or 0s,
    #   the 2nd-8th bits shows the count of the 1s or 0s of the symbol, saved in the 1st bit
    return compressed


def compress_row(row):
    compressed = bytearray()
    chunks = split_bits(row, 127)  # chunks are feeded to compress_chunk, which is hardcoded to handle 127-bit chunks
    for chunk in chunks:
        compressed.extend(compress_chunk(chunk))
    return compressed


def split_bits(bits, width):
    for i in range(0, len(bits), width):
        yield bits[i:i+width]


def compress_in_executor(executor, bits, width):
    row_compressors = []
    for row in split_bits(bits, width):
        compressor = executor.submit(compress_row, row)
        row_compressors.append(compressor)
    compressed = bytearray()
    for compressor in row_compressors:
        compressed.extend(compressor.result())
    return compressed


def compress_image(in_filename, out_filename, executor=None):
    executor = executor if executor else ProcessPoolExecutor()
    with Image.open(in_filename) as image:
        # convert(): to black-and-white mode,
        # getdata(): returns iterator,
        # bitarray(): for quicker transfer
        bits = bitarray(image.convert('1').getdata())
        width, height = image.size
    compressed = compress_in_executor(executor, bits, width)
    with open(out_filename, 'wb') as file:
        file.write(width.to_bytes(2, 'little'))
        file.write(height.to_bytes(2, 'little'))
        file.write(compressed)


def single_image_main():
    in_filename, out_filename = sys.argv[1:3]
    #executor = ThredPolExecutor(4)
    executor = ProcessPoolExecutor()
    compress_image(in_filename, out_filename, executor)


def compress_dir(in_dir, out_dir):
    if not out_dir.exists():
        out_dir.mkdir()
    executor = ProcessPoolExecutor()
    for file in (f for f in in_dir.iterdir() if f.suffix == '.bmp'):
        out_file = (out_dir / file.name).with_suffix('.rle')
        executor.submit(compress_image, str(file), str(out_file))


def dir_images_main():
    in_dir, out_dir = (Path(p) for p in sys.argv[1:3])
    compress_dir(in_dir, out_dir)


def decompress(width, height, bytes):
    image = Image.new('1', (width, height))
    col = 0
    row = 0
    for byte in bytes:
        color = (byte & 128) >> 7
        count = byte & ~128
        for _ignore in range(count):
            image.putpixel((row, col), color)  # sets one pixel at a time
            row += 1
        if not row % width:  # start next col
            col += 1
            row = 0
    return image


with open(sys.argv[1], 'rb') as file:
    width = int.from_bytes(file.read(2), 'little')
    height = int.from_bytes(file.read(2), 'little')
    image = decompress(width, height, file.read())
    image.save(sys.argv[2], 'bmp')
