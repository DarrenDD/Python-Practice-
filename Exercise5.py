def header():
    print("\nPrime Number Checker\n")

def get_valid_input():
    while True:
        user_input = int(input("Please enter an integer between 1 and 5000: "))
        if user_input < 1 or user_input > 5000:
            print("Invalid input, please try again")
        else:
            return int(user_input)

def get_factors(num_entered):
    factors = []
    for i in range(1, num_entered + 1):
        remainder = num_entered % i
        if remainder == 0:
            factors.append(i)
    return factors

def main():
    header()
    
    again = 'y'
    while again.lower() == 'y':
        input_num = get_valid_input()
        inputfactors = get_factors(input_num)
        if len(inputfactors) == 2:
            print(f"{input_num} is a prime number. ")
        else:
            print(f"{input_num} is NOT a prime number. ")
            print(f"It has a {len(inputfactors)} factors:", end = " ")
            for factor in inputfactors:
                print(factor, end = " ")
            print()
        print()
        
        again = input("Try again (y/n): ")
        print()
    print("bye")
        
if __name__ == "__main__":
    main()