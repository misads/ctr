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

    parser.add_argument('path')

    parser.add_argument('--tab', '-t', action='store_true', help='csv file use \\t split')
    parser.add_argument('--expand', '-e', default=1, type=int, help="expand times")
    parser.add_argument('--frac', '-f', default=1.0, type=float, help="keep prob")

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    path = args.path
    expand = args.expand
    f = args.frac
    df = pd.read_csv(path, sep=',', header=None)
    df = df.sample(frac=f).reset_index(drop=True)
    df2 = df
    for i in range(expand-1):
        df_copy = df.sample(frac=f).reset_index(drop=True)
        df2 = pd.concat([df2, df_copy], ignore_index=True)
        del df_copy


    df2.to_csv(path[:-4] + '_shuffle_%dx.csv' % expand, index=False, header=None)


