#!/usr/bin/env python3
def print_fibonacci(length):
    fibonacci_list = [0, 1]
    for i in range(2, length):
        next_number = fibonacci_list[i - 1] + fibonacci_list[i - 2]
        fibonacci_list.append(next_number)
    print(fibonacci_list)