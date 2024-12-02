# Step 1: Create a new file named division.py

import argparse

# Step 2: Set up argument parser
parser = argparse.ArgumentParser(description='Divide two numbers.')

# Step 3: Define the arguments
parser.add_argument('-Number1', type=float, required=True, help='First number')
parser.add_argument('-Number2', type=float, required=True, help='Second number')

# Step 4: Parse the arguments
args = parser.parse_args()

# Step 5: Divide the numbers and print the result
if args.Number2 == 0:
    print("Error: Division by zero is not allowed.")
else:
    result = args.Number1 / args.Number2
    print(f'The result of dividing {args.Number1} by {args.Number2} is {result}')
