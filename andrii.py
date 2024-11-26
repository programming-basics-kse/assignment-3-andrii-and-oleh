import argparse

parser = argparse.ArgumentParser(description='Andrii')

parser.add_argument("file")

subparsers = parser.add_subparsers(dest='command')


medals_parser = subparsers.add_parser("medals")
medals_parser.add_argument("country")
medals_parser.add_argument("year")

args = parser.parse_args()


