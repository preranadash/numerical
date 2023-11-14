def generate_fibonacci(n):
    fib_numbers = [0, 1]

    while len(fib_numbers) < n:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])

    return fib_numbers

def main():
    n = 10
    fibonacci_sequence = generate_fibonacci(n)

    print(f"The first {n} Fibonacci numbers are:")
    for number in fibonacci_sequence:
        print(number)

if __name__ == "__main__":
    main()
