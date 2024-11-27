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

'''def overall():
    with open(args.file, 'r') as file:
        next(file)
        countries = {}
        for row in file:
            row = row.split('\t')
            row[-1] = row[-1][:-1]
            if row[6].lower() in overall or row[7].lower() in overall:
                '''

parser = argparse.ArgumentParser()

parser.add_argument('file')

parser.add_argument('-t','--total', type=str)
parser.add_argument('-o', '--overall', nargs='+')



args = parser.parse_args()
year = args.total
overall = args.overall
for state in overall:
    state = state.lower()





if not args.total == None:
    total()



