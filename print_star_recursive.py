def print_star(N : int):
    if N == 0:
        return
    print_star(N - 1)
    print('*' * N)

def print_star_reversed(N : int):
    if N == 0:
        return
    print('*' * N)
    print_star_reversed(N - 1)

print_star(100)
print_star_reversed(99)
