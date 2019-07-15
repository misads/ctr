# encoding=utf-8

import numpy as np
import csv
import matplotlib.pyplot as plt
import  pandas as pd



train_df = pd.read_csv('train_small.csv', header=None)

for row in train_df:
    print(row)

train_df.to_csv("test.csv", index=False, sep=',', header=None)

'''
train_df.columns = ['label', 'uid', 'aid', 'time', 'media', 'loc', 'cid', 'net']

user_feature = pd.read_csv('user_small.csv')
user_feature.columns = ['uid', 'age', 'sex', 'city', 'province', 'device', 'service']
#ad_Feature = pd.read_csv('input/adFeature.csv')


train = pd.merge(train_df, user_feature, on='uid', how='left')

train.to_csv("test.csv", index=False, sep=',')

# np.save('train_df.index', np.array(train.index))
'''


'''
with open('user_info.csv', 'r', encoding='utf-8') as f:
    csv_file = csv.reader(f)
    i = 0
    dic = {}
    for row in csv_file:
        #print(row)
        dic[row[0]] = row[1:]
        i = i + 1
        if i % 1000000 == 0:
            print('%d/50' % (i/1000000))

'''

'''
with open('train_20190518.csv', 'r') as f:

    csv_file = csv.reader(f)

    i = 0
    all = np.zeros(24)
    no_clicks = np.zeros(24)
    for row in csv_file:
        time = row[3]
        time = int(time[11:13])
        click = row[0]
        if click == '0':
            no_clicks[time] = no_clicks[time] + 1
        all[time] = all[time] + 1
        #print(time)
        # print(type(click))
        #if click == '1':
        #    clicks = clicks + 1
        i = i + 1
        if i % 1000000 == 0:
            print('%d/159' % (i/1000000))
        if i == 100000000:
            break

    print(all)
'''



