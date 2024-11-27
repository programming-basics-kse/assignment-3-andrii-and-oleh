'''import argparse

parser = argparse.ArgumentParser(description="description123")

subparsers = parser.add_subparsers(dest="operation")

# Create a sub-parser for the 'add' operation
add_parser = subparsers.add_parser('add', help='Addition')
add_parser.add_argument('numbers', nargs='+', type=int, help='Numbers to add')

# Create a sub-parser for the 'subtract' operation
subtract_parser = subparsers.add_parser('subtract', help='Subtraction')
subtract_parser.add_argument('numbers', nargs='-', type=int, help='Numbers to subtract')

#add argument to parser (-- means optional arguments, required type, help message for user)
parser.add_argument("-n", "--num", type=int, help="enter number")
#parser.add_argument("word", help="enter word")
#get arguments from parser
args = parser.parse_args()
number = args.num
#word = args.word
if args.operation == 'add':
    result = sum(args.numbers)
elif args.operation == 'subtract':
    result = args.numbers[0] - sum(args.numbers[1:])

print(f"Number - {result}")
#print(f"Word - {word}")
'''

countries = {
    'Ukraine': {
        '1999': 2,
        '1998': 3,
        '2000': 0
    },
    'Astana': {
        '1999': 1,
        '1998': 2,
        '2000': 0
    }
}
counter = 0
for state in countries:
    for year in countries[state]:
        if countries[state][year] > counter:
            max = year
    print(f"{state}: best year was {max} with {countries[state][max]} medals")
