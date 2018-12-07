import pandas as pd
import numpy as np


SESSIONS_DATAFILE = './downloaded_datasets/sessions.csv'
TRAIN_DATAFILE = './downloaded_datasets/train_users_2.csv'
OUTPUT_DATAFILE = './modified_datasets/total_browse_time.csv'

def sum_time_elapsed(df_t, df_s, fill_blank_method='median'):
  user_total_time = df_s.groupby('user_id', sort=False).agg({'secs_elapsed':'sum'})
  median = 0
  if fill_blank_method == 'median':
    median = np.median(df_t.join(user_total_time, on='id', how='inner').secs_elapsed)
  df = df_t.join(user_total_time, on='id')
  df.secs_elapsed = df.secs_elapsed.fillna(median)
  return df




def main():
  df_t = pd.read_csv(TRAIN_DATAFILE)
  df_s = pd.read_csv(SESSIONS_DATAFILE)
  sum_time_elapsed(df_t, df_s)

if __name__ == '__main__':
  main()