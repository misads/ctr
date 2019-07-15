# encoding=utf-8

import numpy as np
import csv
import pickle
from sklearn import metrics
import sys
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='show .csv file or count items')

    parser.add_argument('path', help='pickle file')
    args = parser.parse_args()

    return args


if __name__ == '__main__':

    args = parse_args()

    path = args.path

    with open(path, 'rb') as f:
        data = pickle.load(f, encoding='bytes')

    with open('submission.csv', 'w', encoding='utf-8', newline='') as f:
        csv_writer = csv.writer(f)
        head = ['id', 'probability']
        csv_writer.writerow(head)  # 写一行
        for i in range(1000000):
            row = [i + 1, round(data[1][i], 6)]
            csv_writer.writerow(row)
