import sys
import math

def is_prime(n):
    """Checks if a number is prime using an optimized trial division method."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_pth_prime(p):
    """Finds the p-th prime number."""
    if p <= 0:
        raise ValueError("Position 'p' must be a positive integer.")
    
    # The first prime is 2
    if p == 1:
        return 2
        
    count = 1  # We already have '2' as the first prime
    num = 1    # Start checking from 3
    
    while count < p:
        num += 2  # Check only odd numbers
        if is_prime(num):
            count += 1
            
    return num

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <p>")
        print("  <p>: The position of the prime number you want to find (e.g., 10 for the 10th prime).")
        sys.exit(1)
        
    try:
        p_input = int(sys.argv[1])
        result = find_pth_prime(p_input)
        print(f"The {p_input}th prime number is: {result}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
