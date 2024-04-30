### 4주차 과제 소스코드

----
### 소스코드 :
1. get_loop_sum.py :
```python
total_sum = 0

for i in range(1,1000001):
    total_sum += i

print(total_sum)
```

2. get_recursive_sum.py :
```python
def get_sum(n : int) -> int:
    return (get_sum(n-1) + n) if n > 1 else 1

print(get_sum(1000000))
```

3. factorial_loop.py :
```python
factorial_result = 1

for i in range(1, 101):
    factorial_result *= i

print(factorial_result)
```

4. factorial_recursive.py :
```python
def factorial(n : int) -> int:
    return factorial(n-1) * n if n > 1 else 1
print(factorial(100))
```

5. fibonacci_loop.py :
```python
fibonacci_list = [0, 1]

for i in range(2, 30):
    fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])

print(fibonacci_list[29])
```

6. fibonacci_recursive.py :
```python
def fibonacci(N : int):
    if N == 0 :
        return 0
    elif N == 1:
        return 1
    else:
        return fibonacci(N - 1) + fibonacci(N - 2)

print(fibonacci(29))
```

7. get_greatest_common_divisor_loop.py :
```python
A, B = map(int, input().split())

for i in range(min(A, B), 0, -1):
    if((A % i == 0) and (B % i == 0)):
        print(i)
        break
```

8. get_greatest_common_divisor_recursive.py :
```python
def get_greatest_common_divisor(A : int, B : int, divisor : int) -> int:
    if ((A % divisor == 0) and (B % divisor == 0)):
        return divisor
    elif divisor == 1:
        return 1
    else:
        return get_greatest_common_divisor(A, B, divisor - 1)

A, B = map(int, input().split())
print(get_greatest_common_divisor(A, B, min(A, B)))
```

9. print_star_loop.py :
```python
for i in (list(range(1, 101)) + list(range(99, 0, -1))):print('*' * i)
```

10. print_star_recursive.py
```python
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
```
