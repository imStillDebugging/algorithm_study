fibonacci_list = [0, 1]

for i in range(2, 30):
    fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])

print(fibonacci_list[29])
