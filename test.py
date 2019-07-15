# encoding=utf-8

import numpy as np
import csv

from sklearn import metrics
import sys
import tensorflow as tf

uid = 'u104057654'

import pandas as pd


temp = tf.range(0, 100) + tf.constant(1, shape=[100])
temp = tf.reshape(temp, [10, 5, 2])
f = tf.constant([[1, 5, 9, 3, 8, 6]])
temp2 = tf.gather(temp, f)

emv_v2 = []
emv_v2.append(tf.reshape(tf.range(48), [3, 1, 16]))
emv_v2.append(tf.reshape(tf.range(64), [4, 1, 16]))

#emv_v2 = tf.reshape(tf.range(1280), [4, 20, 16])

f1 = tf.ones([2, 20],dtype=tf.int32)
f2 = tf.ones([2, 20],dtype=tf.int32)

f = tf.reshape(tf.range(40), [2, 20])

emb_inp_v2=[]
emb_inp_v2.append(tf.gather(emv_v2[0], f1))
emb_inp_v2.append(tf.gather(emv_v2[1], f2))

#emb_inp_v2 = tf.gather(emv_v2, f)
#emb_inp_v2 = tf.reshape(tf.range(6400), [-1, 20, 20, 16])  # None × 20 × 20 × k
#emb_inp_v2 = tf.reduce_sum(emb_inp_v2 * tf.transpose(emb_inp_v2, [0, 2, 1, 3]), -1)

k = [[[1, 2, 3]], [[1]], [[3]]]

emb_inp_v2 = tf.concat(emb_inp_v2, 2)

with tf.Session() as sess:
    #d = tf.concat(k, -1)
    #print(sess.run(d))
    print(sess.run(tf.shape(emb_inp_v2)))



#print(sess.run(tf.shape(emb_inp_v2)))
