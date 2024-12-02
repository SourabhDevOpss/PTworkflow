# Step 1: Create a new file named multiplication.py

import argparse

# Step 2: Set up argument parser
parser = argparse.ArgumentParser(description='Multiply three numbers.')

# Step 3: Define the arguments
parser.add_argument('-Number1', type=int, required=True, help='First number')
parser.add_argument('-Number2', type=int, required=True, help='Second number')
parser.add_argument('-Number3', type=int, required=True, help='Third number')

# Step 4: Parse the arguments
args = parser.parse_args()

# Step 5: Multiply the numbers and print the result
result = args.Number1 * args.Number2 * args.Number3
print(f'The result of multiplying {args.Number1}, {args.Number2}, and {args.Number3} is {result}')
