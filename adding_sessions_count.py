import pandas as pd

# get count of unique ids seen in sessions.csv
# sessions = pd.read_csv('/Users/QuekYufei/Downloads/all/sessions.csv')
# counted = sessions['user_id'].value_counts(sort=False)
# counted.to_csv('/Users/QuekYufei/Downloads/all/sessions_counted.csv')


def addSessionsCount(df_t, df_s):
  counted = df_s['user_id'].value_counts(sort=False)
  new = df_t.set_index('id').join(counted).rename(columns={'user_id':'session_count'})
  return new

if __name__ == '__main__':
  addSessionsCount(pd.read_csv('downloaded_datasets/train_users_2.csv'), pd.read_csv('downloaded_datasets/sessions.csv'))