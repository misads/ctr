# encoding=utf-8

import numpy as np
import csv

from sklearn import metrics
import sys
import tensorflow as tf
import argparse
import pandas as pd

import pandas as pd

def parse_args():
    parser = argparse.ArgumentParser(description="ensemble")

    parser.add_argument('path1')
    parser.add_argument('path2')

    parser.add_argument('--tab', '-t', action='store_true', help='csv file use \\t split')
    parser.add_argument('--weight1', '-w1', default=5, type=int, help="weight for file1")
    parser.add_argument('--weight2', '-w2', default=5, type=int, help="weight for file2")

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    path1 = args.path1
    path2 = args.path2
    w1 = args.weight1/10.0
    w2 = args.weight2/10.0

    f1 = pd.read_csv(path1, sep=',', header=0)
    f1.columns = ['id', 'p']
    f2 = pd.read_csv(path2, sep=',', header=0)
    f2.columns = ['id', 'p']
    #print(f1)
    #  乘以权重，四舍五入
    f1['p'] = round(f1['p']*w1 + f2['p']*w2, 6)
    #print(f1)
    f1.columns = ['id', 'probability']
    f1.to_csv('submission.csv', index=False)


