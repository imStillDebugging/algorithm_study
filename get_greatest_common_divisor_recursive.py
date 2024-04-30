def get_greatest_common_divisor(A : int, B : int, divisor : int) -> int:
    if ((A % divisor == 0) and (B % divisor == 0)):
        return divisor
    elif divisor == 1:
        return 1
    else:
        return get_greatest_common_divisor(A, B, divisor - 1)

A, B = map(int, input().split())
print(get_greatest_common_divisor(A, B, min(A, B)))
