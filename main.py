import argparse, sys
import matplotlib.pyplot as plt


def make_graph(medals):
    y = []
    x = []
    for i in range(len(medals)):
        y.append(sum(medals[i][1].values()))
        x.append(medals[i][0])
    plt.plot(x, y)
    plt.xticks(rotation=90)
    plt.show()


def total():
    try:
        if int(tot) > 1894 or int(tot) > 2020 or int(tot) % 2 != 0:
            print('Olimpiad didnt happen in this year unfortunatly.')
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
            for key in countries:
                print(f"{key} - ", end="")
                for key1 in countries[key]:
                    print(f"{key1}: {countries[key][key1]}", end="; ")
                print()
    except FileNotFoundError:
        print("no such file")


def over(overall):
    try:
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
    except FileNotFoundError:
        print("there is no such file")
    except KeyError:
        print("there is no such country")


def medals_command(args):
    country = args.medals[0]
    year = args.medals[1]
    medalists = []
    medals = {
        "Bronze": 0,
        "Silver": 0,
        "Gold": 0
    }
    country_in_list = False
    with open(args.file, "r") as datafile:
        next(datafile)
        # minimum year is 1896
        # all years are even
        for line in datafile:
            line = line.split("\t")
            if (country.capitalize() == line[6] or country.upper() == line[7]) and year == line[9] and line[
                -1][:-1] in medals:
                medalists.append(", ".join(line[1:]))
                medals[line[-1][:-1]] += 1
                country_in_list = True
            if len(medalists) == 10:
                break

        if int(year) < 1896 and not int(year) % 2:
            print("there weren't any olympiad this year")
            print("try entering even number greater than 1896")
        elif not country_in_list:
            print("There is no such country in dataset or it didn't participated")
        elif len(medalists) < 10:
            print("There are less then 10 medalists")
        else:
            print(*medalists)
            print(f"Bronze: {medals["Bronze"]}, Silver: {medals['Silver']}, Gold: {medals['Gold']}")

    if output_file != None:
        with open(output_file, "w") as datafile:
            datafile.write("\n".join(medalists))


def interactive_command(args):
    while True:
        try:
            country = input("Please, enter your country (or exit): ")
            country_stat = {}
            olympiads = []
            if country.lower() == "exit":
                sys.exit()
            with open(args.file, "r") as datafile:
                next(datafile)
                for line in datafile:
                    line = line.split("\t")
                    line[-1] = line[-1][:-1]
                    if country.capitalize() == line[6] or country.upper() == line[7]:
                        if line[9] not in country_stat:
                            country_stat[line[9]] = {"Bronze": 0, "Silver": 0, "Gold": 0}
                        if line[9] in country_stat and line[-1] in country_stat[line[9]]:
                            country_stat[line[9]][line[-1]] += 1
                            olympiads.append(line[11])
            first_olympiad = sorted(country_stat.keys(), key=lambda key: int(key))
            print(f"first participation of {country.capitalize()} - {first_olympiad[0]}")
            print(f"Olympiad took place in {olympiads[0]}")
            medals_each_year = sorted(country_stat.items(), key=lambda item: sum(item[1].values()), reverse=True)
            print(
                f"{medals_each_year[0][0]} was the best for {country.capitalize()}. It has {sum(medals_each_year[0][1].values())} medalists.")
            print(
                f"{medals_each_year[-1][0]} was the worst for {country.capitalize()}. It has {sum(medals_each_year[-1][1].values())} medalists.")
            bronze = 0
            silver = 0
            gold = 0
            for i in country_stat:
                bronze += country_stat[i]["Bronze"]
                silver += country_stat[i]["Silver"]
                gold += country_stat[i]["Gold"]
            print(
                f"average: bronze - {round(bronze / len(country_stat))}, silver - {round(silver / len(country_stat))}, gold - {round(gold / len(country_stat))}")
            if output_file != None:
                with open(output_file, "w") as datafile:
                    datafile.write(f"first participation of {country.capitalize()} - {first_olympiad[0]}\n")
                    datafile.write(f"Olympiad took place in {olympiads[0]}")
                    datafile.write("\n")
                    datafile.write(
                        f"{medals_each_year[0][0]} was the best for {country.capitalize()}. It has {sum(medals_each_year[0][1].values())} medalists.\n")
                    datafile.write(
                        f"{medals_each_year[-1][0]} was the worst for {country.capitalize()}. It has {sum(medals_each_year[-1][1].values())} medalists.\n")
                    datafile.write(
                        f"average: bronze - {round(bronze / len(country_stat))}, silver - {round(silver / len(country_stat))}, gold - {round(gold / len(country_stat))}")
            make_graph(medals_each_year)
        except IndexError:
            pass


parser = argparse.ArgumentParser(description=' This is a program to work with dataset about '
                                             ' whole information of OG, counntries and their '
                                             ' team members. ')

parser.add_argument("file", help="eneter a name of data file")
parser.add_argument("-med", "--medals", nargs=2,
                    help="enter one country and a year of olympiad to get medalists from this country")
parser.add_argument("-inter", "--interactive", help="etner start to go into interactive mode")
parser.add_argument("-out", "--output", help="name of output file")
parser.add_argument('-t', '--total', type=str, help='Enter an integer number between 1896 and 2020.')
parser.add_argument('-o', '--overall', nargs='+', help='Enter a list(or one) of countries, or their TeamCode.')

args = parser.parse_args()

output_file = args.output
data_file = args.file
year = args.total
overall = args.overall
tot = args.total

if args.medals != None:
    medals_command(args)
if args.interactive != None:
    if args.interactive.lower() == "start":
        interactive_command(args)
if not args.total == None:
    total()
if not args.overall == None:
    overall = [state.lower() for state in overall]
    over(overall)
