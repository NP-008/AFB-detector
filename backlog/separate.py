import os
import shutil
import random

source = '/hdd/AFB/tile/64/'
des_test = '/hdd/AFB/tile/64/test/'
des_train = '/hdd/AFB/tile/64/train/'


pos_lst = os.listdir(source+'positive')
random.shuffle(pos_lst)
a = int(0.2*len(pos_lst))
pos_test = pos_lst[:a]
pos_train = pos_lst[a:]
b = len(pos_train)
b = b*6
print('positive list checked')

neg_lst = os.listdir(source+'negative')
random.shuffle(neg_lst)
neg_test = neg_lst[:a]
neg_train = neg_lst[a:a+b]
print('negative list checked')

for i in pos_test:
  path = os.path.join(source+'positive/', i)
  shutil.copy(path, des_test+'positive/')
print('positive test moved')

for i in neg_test:
  path = os.path.join(source+'negative/', i)
  shutil.copy(path, des_test+'negative/')
print('negative test moved')

for i in pos_train:
  path = os.path.join(source+'positive/', i)
  shutil.copy(path, des_train+'positive/')
print('positive train moved')

for i in neg_train:
  path = os.path.join(source+'negative/', i)
  shutil.copy(path, des_train+'negative/')
print('negative train moved')
