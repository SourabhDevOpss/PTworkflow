# Step 1: Create a new file named subtraction.py

import argparse

# Step 2: Set up argument parser
parser = argparse.ArgumentParser(description='Subtract two numbers.')

# Step 3: Define the arguments
parser.add_argument('-Number1', type=int, required=True, help='First number')
parser.add_argument('-Number2', type=int, required=True, help='Second number')

# Step 4: Parse the arguments
args = parser.parse_args()

# Step 5: Subtract the numbers and print the result
result = args.Number1 - args.Number2
print(f'The result of subtracting {args.Number2} from {args.Number1} is {result}') 
