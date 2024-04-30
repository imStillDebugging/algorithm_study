def get_sum(n : int) -> int:
    return (get_sum(n-1) + n) if n > 1 else 1

print(get_sum(1000000))
