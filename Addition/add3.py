# Step 1: Create a new file named addition.py

import argparse

# Step 2: Set up argument parser
parser = argparse.ArgumentParser(description='Add three numbers.')

# Step 3: Define the arguments
parser.add_argument('-Number1', type=int, required=True, help='First number')
parser.add_argument('-Number2', type=int, required=True, help='Second number')
parser.add_argument('-Number3', type=int, required=True, help='Third number')

# Step 4: Parse the arguments
args = parser.parse_args()

# Step 5: Add the numbers and print the result
result = args.Number1 + args.Number2 + args.Number3
print(f'The result of adding {args.Number1}, {args.Number2}, and {args.Number3} is {result}')
