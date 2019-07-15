# encoding=utf-8

import numpy as np
import csv

import argparse


def parse_args():

    parser = argparse.ArgumentParser(description='limit .csv file')

    parser.add_argument('path')

    parser.add_argument('--tab', '-t', action='store_true', help='use \\t split')

    parser.add_argument('--limit', '-l', default=100, type=int, help='show items limit')

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = parse_args()

    path = args.path
    limit = args.limit

    if args.tab:
        dialect = 'excel-tab'
    else:
        dialect = 'excel'

    with open(path, 'r', encoding='utf-8') as f:
        csv_file = csv.reader(f, dialect=dialect)
        i = 0
        output = path[:-4] + '_%d.csv' % limit
        print(output)
        with open(output, 'w', encoding='utf-8', newline='') as f2:  # 如果在windows下打开csv出现空行的情况,加一个newline=''参数

            csv_writer = csv.writer(f2)

            for row in csv_file:
                csv_writer.writerow(row)  # 写多行
                print(row)
                i = i + 1
                if i % 1000000 == 0:
                    print(i)

                if i == limit:
                    break

            print('total:%d' % i)


