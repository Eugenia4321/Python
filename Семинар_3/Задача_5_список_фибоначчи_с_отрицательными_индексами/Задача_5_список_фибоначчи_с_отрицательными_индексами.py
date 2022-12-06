


number = int(input('Enter N = '))

def fibonacci_numbers(n):
    
     array_fibonacci_numbers = []
     a, b = 1, 1
     for _ in range(n):
         array_fibonacci_numbers.append(a)
         a, b = b, a + b
     a, b = 0, 1
     for _ in range (n+1):
         array_fibonacci_numbers.insert(0, a)
         a, b = b, a - b
     return array_fibonacci_numbers

print(f'{fibonacci_numbers(number)}')