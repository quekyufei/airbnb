import pandas as pd

def addSessionsCount(df_t, df_s):
  counted = df_s['user_id'].value_counts(sort=False)
  new = df_t.join(counted, on='id').rename(columns={'user_id':'session_count'})
  return new

if __name__ == '__main__':
  addSessionsCount(pd.read_csv('downloaded_datasets/train_users_2.csv'), pd.read_csv('downloaded_datasets/sessions.csv'))
