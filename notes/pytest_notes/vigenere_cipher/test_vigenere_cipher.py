from vigenere_cipher import VigenereCipher, combine_character, separate_character


def test_encode():
    cipher = VigenereCipher('TRAIN')
    encoded = cipher.encode('ENCODEDINPYTHON')
    assert encoded == 'XECWQXUIVCRKHWA'


def test_encode_character():
    cipher = VigenereCipher('TRAIN')
    encoded = cipher.encode('E')
    assert encoded == 'X'


def test_encode_space():
    cipher = VigenereCipher('TRAIN')
    encoded = cipher.encode('ENCODED IN PYTHON')
    assert encoded == 'XECWQXUIVCRKHWA'


def test_encode_lowercase():
    cipher = VigenereCipher('TRain')
    encoded = cipher.encode('encoded in Python')
    assert encoded == 'XECWQXUIVCRKHWA'


def test_combine_character():
    assert combine_character('E', 'T') == 'X'
    assert combine_character('N', 'R') == 'E'


def test_extend_keyword():
    cipher = VigenereCipher('TRAIN')
    extended = cipher.extend_keyword(16)
    assert extended == 'TRAINTRAINTRAINT'


def test_separate_character():
    assert separate_character('X', 'T') == 'E'
    assert separate_character('E', 'R') == 'N'


def test_decode():
    cipher = VigenereCipher('TRAIN')
    decode = cipher.decode('XECWQXUIVCRKHWA')
    assert decode == 'ENCODEDINPYTHON'
