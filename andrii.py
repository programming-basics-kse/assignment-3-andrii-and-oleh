import argparse

parser = argparse.ArgumentParser(description='Andrii')

parser.add_argument("file")

subparsers = parser.add_subparsers(dest='command')


medals_parser = subparsers.add_parser("medals")
medals_parser.add_argument("country")
medals_parser.add_argument("year")

args = parser.parse_args()

if args.command == "medals":
    medalists = []
    medals = {
        "Bronze": 0,
        "Silver": 0,
        "Gold": 0
    }
    country_in_list = False
    with open(args.file, "r") as datafile:
        next(datafile)
        #minimum year is 1896
        #all years are even
        for line in datafile:
            line = line.split("\t")
            line[-1] = line[-1][:-1]
            if (args.country.capitalize() == line[6] or args.country == line[7]) and args.year == line[9] and line[-1] in medals:
                print(", ".join(line))
                medalists.append(", ".join(line))
                medals[line[-1]] += 1
                country_in_list = True
        if int(args.year) < 1896 and not int(args.year) % 2:
            print("there weren't any olympiad this year")
            print("try entering even number greater than 1896")
        elif not country_in_list:
            print("There is no such country in dataset or it didn't participated")
        elif len(medalists) < 10:
            print("There are less then 10 medalists")

        print(f"Bronze: {medals["Bronze"]}, Silver: {medals['Silver']}, Gold: {medals['Gold']}")

