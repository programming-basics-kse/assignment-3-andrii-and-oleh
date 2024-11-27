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

parser = argparse.ArgumentParser(description='Andrii')

parser.add_argument("file")
parser.add_argument( "-medals", "--medals", nargs=2)
parser.add_argument("-output", "--output")

args = parser.parse_args()

output_file = args.output
data_file = args.file


if args.medals != None:
    medals_command(args)