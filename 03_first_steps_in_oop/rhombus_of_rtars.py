def print_row(size, row_size):
    for row in range(size - row_size):
        print(' ', end='')
    for row in range(1, row_size):
        print('*', end=' ')
    print('*')


size = int(input())
for row_size in range(1, size):
    print_row(size, row_size)
for row_size in range(size, 0, -1):
    print_row(size, row_size)

