# encoding=utf-8

import numpy as np
import csv
import pandas as pd
from sklearn import metrics
import sys
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="""['label', 'uid', 'aid', 'time', 'siteid', 'slotid', 'cid', 'net',
                    'age', 'gender', 'city', 'province', 'phoneType', 'carrier',
                    'billid', 'primid', 'creative', 'inter', 'app', 'c1', 'c2']""")

    parser.add_argument('path')

    parser.add_argument('--tab', '-t', action='store_true', help='csv file use \\t split')

    parser.add_argument('--save', '-s', action='store_true', help='save result to local file')

    parser.add_argument('--group', '-g', action='store_true', help='group final result')

    parser.add_argument('--all', '-a', action='store_true', help='show all')

    parser.add_argument('--descend', '-d', action='store_true', help='descend sort')

    parser.add_argument('--field', '-f', default='uid', type=str, help="required. default='uid'")

    parser.add_argument('--field2', '-f2', default='', type=str,
                        help="field2, use for cross feature, empty for single feature")

    parser.add_argument('--limit', '-l', default=10, type=int, help='show items limit')

    parser.add_argument('--mode', '-m', help='statistics mode, default=count',
                        choices=['count', 'ratio', 'mean', 'unique'],
                        default='count')

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = parse_args()

    path = args.path
    limit = args.limit
    mode = args.mode
    field = args.field
    field2 = args.field2
    group = args.group
    all = args.all
    descend = args.descend

    save = args.save

    train_df = pd.read_csv(path, header=None)
    train_df.columns = ['label', 'uid', 'aid', 'time', 'siteid', 'slotid', 'cid', 'net',
                        'age', 'gender', 'city', 'province', 'phoneType', 'carrier',
                        'billid', 'primid', 'creative', 'inter', 'app', 'c1', 'c2']
    #test.columns = ['index', 'uid', 'aid', 'time', 'siteid', 'slotid', 'cid', 'net']


    if mode == 'count':

        if field2:  # cross feature
            cross_field = field + '_' + field2
            new_field = train_df[field].astype(str).values + '_' + train_df[field2].astype(str).values
            train_df[cross_field] = new_field
            c = train_df.groupby(cross_field).size().reset_index(name=cross_field + '_count')
            train = pd.merge(train_df, c, on=cross_field, how='left')

            if group:
                gp = [field, field2, cross_field + '_count']
                train = train.groupby(gp).size().reset_index(name='count')

        else:
            if group:
                c = train_df[field].value_counts().reset_index(name=field + "_count")
                #gp = [field, field + "_count"]
                #train = train.groupby(gp).size().reset_index(name='count')
                train = c
            else:
                c = train_df.groupby(field).size().reset_index(name=field + "_count")
                train = pd.merge(train_df, c, on=field, how='left')



        if save:  # save
            pass
        else:  # preview

            #train_df['new_field'] = train_df['aid'].astype(str).values + '_' + train_df['gender'].astype(str).values
            #c2 = train_df.groupby('new_field').size().reset_index(name='new_field' + "_count")

            #train = pd.merge(train_df, c2, on='new_field', how='left')


            print(train)

        #print(train_df[field].value_counts()[:limit])

        #train_df['count'] = train_df[field].values
        #print(train_df[:limit])

    elif mode == 'ratio':
        if field2:  # cross feature
            if field2 == 'label':

                train_1 = train_df[train_df.label == 1]
                b = train_1.groupby([field]).size().reset_index(name=field + '_1')
                train_df = pd.merge(train_df, b, on=field, how='left')
                #del b
                train_df = train_df.fillna(0)


                c = train_df.groupby(field).size().reset_index(name=field + "_count")
                train = pd.merge(train_df, c, on=field, how='left')
                del c

                train[field + '_1_ratio'] = train[field + '_1'] / train[field + "_count"] / 0.061935
                train = train.fillna(1.00000)
                del train_df
                if descend:
                    train = train.sort_values(field + '_1_ratio', axis=0,ascending=False, inplace=False)
                if group:
                    train = train.groupby([field, field + '_1_ratio']).size().reset_index(name='count')

                #################
                '''
                c = train_df['label'].value_counts(normalize=True).reset_index(name=field2 + "_ratio")
   
                r_1 = train = c[field2 + "_ratio"].max()
                train_df['label_1'] = r_1
                train = train_df
                '''

                #train = b[b.label == 1]
                #b[field2 + "_ratio"] = b[field2 + "_ratio"].max()

            else:
                norm = True
                relative = [('primid', 'aid')]
                if (field, field2) in relative :
                    norm = False

                cross_field = field + '_' + field2
                new_field = train_df[field].astype(str).values + '_' + train_df[field2].astype(str).values
                train_df[cross_field] = new_field

                b = train_df.groupby(cross_field).size().reset_index(name=cross_field + '_count')
                train_df = pd.merge(train_df, b, on=cross_field, how='left')
                train_df.drop([cross_field], axis=1, inplace=True)
                del b
                c = train_df.groupby(field).size().reset_index(name=field + "_count")


                train = pd.merge(train_df, c, on=field, how='left')
                del c
                del train_df

                if norm:
                    d = train[field2].value_counts(normalize=True).reset_index(name=field2 + "_ratio")
                    d.columns = [field2, field2 + '_ratio']
                    train = pd.merge(train, d, on=field2, how='left')

                train[field + '_' + field2 + '_ratio'] = train[cross_field + '_count'] / train[field + "_count"]
                if norm:
                    train[field + '_' + field2 + '_norm'] = train[field + '_' + field2 + '_ratio'] / train[field2 + '_ratio']

                    train.drop([cross_field + '_count', field + "_count"], axis=1, inplace=True)

                if group:
                    gp = [field, field2, field + '_' + field2 + '_ratio']
                    if norm:
                        gp.append(field + '_' + field2 + '_norm')
                    train = train.groupby(gp).size().reset_index(name='count')

        else:

            c = train_df[field].value_counts(normalize=True).reset_index(name=field + "_ratio")
            c.columns = [field, field + '_ratio']
            train = pd.merge(train_df, c, on=field, how='left')

        if all:
            pd.set_option('display.max_rows', None)

        print(train)

    elif mode == 'mean':
        pass
    elif mode == 'unique':
        pass

    print()
# print(train_df[a>2]) train_df['uid'].isin


