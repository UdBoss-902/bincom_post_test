def fibonacci_generator(n):
    """
    Generator function that yields the first n numbers 
    in the Fibonacci sequence efficiently.
    """
    if n <= 0:
        return
    
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def main():
    print("=== FIBONACCI SERIES GENERATOR ===")
    
    try:
        # Get user input for the number of terms
        n_terms = int(input("Enter the number of terms you want to generate: "))
        
        if n_terms <= 0:
            print("Please enter a positive integer greater than 0.")
            return

        print(f"\nGenerating first {n_terms} terms of the Fibonacci series:")
        
        # Iterate over the generator and print each term
        sequence = list(fibonacci_generator(n_terms))
        print(", ".join(map(str, sequence)))
        
    except ValueError:
        print("Invalid input! Please enter a valid whole number.")

if __name__ == "__main__":
    main()