import argparse


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
            line[-1] = line[-1][:-1]
            if (country.capitalize() == line[6] or country.upper() == line[7]) and year == line[9] and line[
                -1] in medals:
                print(", ".join(line[1:]))
                medalists.append(", ".join(line[1:]))
                medals[line[-1]] += 1
                country_in_list = True
        if int(year) < 1896 and not int(year) % 2:
            print("there weren't any olympiad this year")
            print("try entering even number greater than 1896")
        elif not country_in_list:
            print("There is no such country in dataset or it didn't participated")
        elif len(medalists) < 10:
            print("There are less then 10 medalists")

        print(f"Bronze: {medals["Bronze"]}, Silver: {medals['Silver']}, Gold: {medals['Gold']}")

    if output_file != None:
        with open(output_file, "w") as datafile:
            datafile.write("\n".join(medalists))


def interactive_command(args):
    while True:
        try:
            country = input("Please, enter your country: ")
            country_stat = {}
            olympiads = []
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
            print(f"{medals_each_year[0][0]} was the best for {country.capitalize()}. It has {sum(medals_each_year[0][1].values())} medalists.")
            print(f"{medals_each_year[-1][0]} was the worst for {country.capitalize()}. It has {sum(medals_each_year[-1][1].values())} medalists.")
            bronze = 0
            silver = 0
            gold = 0
            for i in country_stat:
                bronze += country_stat[i]["Bronze"]
                silver += country_stat[i]["Silver"]
                gold += country_stat[i]["Gold"]
            print(f"average: bronze - {round(bronze/len(country_stat))}, silver - {round(silver/len(country_stat))}, gold - {round(gold/len(country_stat))}")
        except IndexError:
            pass


parser = argparse.ArgumentParser(description='Andrii')

parser.add_argument("file")
parser.add_argument("-medals", "--medals", nargs=2,
                    help="enter one country and a year of olympiad to get medalists from this country")
parser.add_argument("-interactive", "--interactive", help="etner start to go into interactive mode")
parser.add_argument("-output", "--output")

args = parser.parse_args()

output_file = args.output
data_file = args.file

if args.medals != None:
    medals_command(args)
elif args.interactive.lower() == "start":
    interactive_command(args)
