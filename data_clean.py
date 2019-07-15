# encoding=utf-8

import numpy as np
import csv
import pandas as pd

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='clean data')

    parser.add_argument('path')

    args = parser.parse_args()

    return args


bill = {'CPC': 0, 'CPM': 1, 'CPD': 2}

if __name__ == '__main__':
    args = parse_args()

    path = args.path

    with open(path, 'r', encoding='utf-8') as f:
        out = path[:-4] + '_clean.csv'
        print(out)
        csv_file = csv.reader(f)
        '''
        读取的csv_file是一个iterator，每个元素代表一行
        '''
        with open(out, 'w', encoding='utf-8',newline='') as f2:  # 如果在windows下打开csv出现空行的情况,加一个newline=''参数
            j = 0
            csv_writer = csv.writer(f2)
            for row in csv_file:
                row[1] = int(row[1][1:])
                row[3] = int(row[3][11:13])
                row[14] = int(bill[row[14]])
                for i in range(0, 21):
                    if row[i]:
                        if isinstance(row[i], str):
                            row[i] = int(float(row[i]))
                    else:
                        row[i] = 0
                j = j + 1
                if j % 100000 == 0:
                    print(j)

                csv_writer.writerow(row)  # 写一行
    '''
    for i in range(0, len(data)):
        data.iloc[i, 1] = int(data.iloc[i, 1][1:])
        data.iloc[i, 3] = int(data.iloc[i, 3][11:13])
        data.iloc[i, 14] = int(bill[data.iloc[i, 14]])
        if i % 1000000 == 0:
            print(i)


    print(data.dtypes)
    '''


    # data.to_csv(out, index=False, sep=',', header=None)
