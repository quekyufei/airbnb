import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import LogisticRegression

onehotlist = ['gender', 'signup_method', 'language', 'affiliate_channel', 'affiliate_provider', 'first_affiliate_tracked', 'signup_app', 'first_device_type', 'first_browser']

def logReg(data_dic):
  log_reg = LogisticRegression()
  log_reg.fit(data_dic['train']['data'], data_dic['train']['label'])
  # predictions = log_reg.predict(data_dic['test']['data'])
  score = log_reg.score(data_dic['test']['data'], data_dic['test']['label'])
  print(score)

def sortData(df):
  data = df[:-1]
  label = df['country_destination']
  train, test = np.split(df, [int(.7*len(df))])
  train_data, train_label = np.split(train, [-1], axis=1)
  # train_dic = {'data':train_data, 'label':train_label}
  test_data, test_label = np.split(test, [-1], axis=1)
  # test_dic = {'data':test_data, 'label':test_label}
  # return {'train': train_dic, 'test':test_dic}
  return {'train':{'data':train_data, 'label':train_label}, 'test':{'data':test_data, 'label':test_label}}




def onehot(df, col):
 return pd.get_dummies(df, columns=col,prefix=col)

if __name__ == '__main__':
  df = pd.read_csv('processed_user.csv')
  for col in onehotlist:
    df = onehot(df, col)
  data_dic = sortData(df)
  logReg(data_dic)


