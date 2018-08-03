def reverse_list(l):
    for i in range(len(l)//2):
        c = l[i]
        l[i] = l[len(l)-i-1]
        l[len(l)-i-1] = c
    return l


def reverse_list_2(l):
    return l[::-1]


def print_multiplication_table(max, space):
    max = max + 1
    for i in range(1, max):
        l = []
        for j in range(1, max):
            l.append(i*j)
        format_string = '{{:{}d}}'.format(space)
        print(''.join([format_string.format(n) for n in l]))


def print_odd_nums(max):
    print(', '.join([str(n) for n in range(1, max, 2)]))


def max_value(l):
    mv = l[0]
    for i in l:
        if i > mv:
            mv = i
    return mv


def max_value_2(l):
    return max(l)


def rgb2hexstr(l):
    print(''.join([hex(i)[2:].zfill(2) for i in l]))


def sum_integers_in_file(file_name='tmp.txt'):
    with open(file_name) as f:
        lines = f.readlines()
    l = [int(i) for i in lines]
    return sum(l)
