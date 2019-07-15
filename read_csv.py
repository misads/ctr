# encoding=utf-8

import numpy as np
import csv

import argparse


def parse_args():

    parser = argparse.ArgumentParser(description='show .csv file or count items')

    parser.add_argument('path')

    parser.add_argument('--count', '-c', action='store_true', help='count items')

    parser.add_argument('--tab', '-t', action='store_true', help='use \\t split')

    parser.add_argument('--limit', '-l', default=100, type=int, help='show items limit')

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = parse_args()

    path = args.path
    limit = args.limit

    if args.count:
        count = True
    else:
        count = False

    if args.tab:
        dialect = 'excel-tab'
    else:
        dialect = 'excel'

    with open(path, 'r', encoding='utf-8') as f:
        csv_file = csv.reader(f, dialect=dialect)
        i = 0
        for row in csv_file:
            if not count:
                print(row)
            i = i + 1
            if i % 1000000 == 0:
                print(i)
            if (not count) and i == limit:
                break

        print('total:%d' % i)


