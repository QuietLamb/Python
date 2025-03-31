def hanoi(n, from_, to_, via_):
    if n == 1:
        print('Move disk {} from {} to {}'.format(n, from_, to_))
    else:
        hanoi(n - 1, from_, via_, to_)
        print('Move disk {} from {} to {}'.format(n, from_, to_))
        hanoi(n-1, via_, to_, from_)

hanoi(3, 'A', 'B', 'C')