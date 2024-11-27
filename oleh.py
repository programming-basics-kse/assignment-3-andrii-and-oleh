import argparse


def total():
    with open(args.file, 'r') as file:
        next(file)
        countries = {}
        for row in file:
            row = row.split('\t')
            row[-1] = row[-1][:-1]
            if year and row[9] == year:
                if row[6] not in countries:
                    countries[row[6]] = {'Bronze': 0, 'Silver': 0, 'Gold': 0}
                if row[-1] in countries[row[6]]:
                    countries[row[6]][row[-1]] += 1
        print(countries)


def over(overall):
    with open(args.file, 'r') as file:
        next(file)
        countries = {}
        for state in overall:
            countries[state] = {}
        for row in file:
            row = row.split('\t')
            row[-1] = row[-1][:-1]
            if row[6].lower() in countries:
                if not (row[9] in countries[row[6].lower()]):
                    countries[row[6].lower()][row[9]] = 0
                if row[-1] != 'NA':
                    countries[row[6].lower()][row[9]] += 1
            elif row[7].lower() in countries:
                if not (row[9] in countries[row[7].lower()]):
                    countries[row[7].lower()][row[9]] = 0
                if row[-1] != 'NA':
                    countries[row[7].lower()][row[9]] += 1
        counter = 0
        max = None
        for state in countries:
            for year in countries[state]:
                if countries[state][year] > counter:
                    max = year
                    counter = countries[state][year]
            print(f"{state.capitalize()}: best year was {max} with {countries[state][max]} medals")


parser = argparse.ArgumentParser(description=' This is a program to work with dataset about '
                                             ' whole information of OG, counntries and their '
                                             ' team members. ')

parser.add_argument('file')

parser.add_argument('-t', '--total', type=str, help='Enter an integer number between 1896 and 2020.')
parser.add_argument('-o', '--overall', nargs='+', help='Enter a list(or one) of countries, or their TeamCode.')

args = parser.parse_args()
year = args.total
overall = args.overall
overall = [state.lower() for state in overall]

if not args.total == None:
    total()
if not args.overall == None:
    over(overall)
