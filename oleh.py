import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")
year_parser = subparsers.add_parser('total')
year_parser.add_argument('year')
args = parser.parse_args()



with open('Olympic Athletes - athlete_events.tsv', 'r') as file:
    next(file)
    countries = {}
    for row in file:
        row = row.split('\t')
        row[-1] = row[-1][:-1]
        if row[9] == args.year:
            if row[6] not in countries:
                countries[row[6]] = {'Bronze': 0, 'Silver': 0, 'Gold': 0}
            if row[-1] in countries[row[6]]:
                countries[row[6]][row[-1]] += 1
    print(countries)

