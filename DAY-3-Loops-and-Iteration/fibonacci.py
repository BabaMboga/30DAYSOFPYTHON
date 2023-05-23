n = int(input("Enter a positive interger: "))

def fibonacci(n):
    fib_list = [0,1]

    if n <= 0 :
        return []
    if n == 1:
        return [0]
    if n == 2:
        return fib_list 
    
    while len(fib_list) < n:
        new_number = fib_list[-1] + fib_list[-2]
        fib_list.append(new_number)

    return fib_list

fibonacci_sequence = fibonacci(n)
print(f"Fibonacci sequence for first {n} numbers: ")
print(fibonacci_sequence)