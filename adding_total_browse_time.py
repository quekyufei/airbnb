import pandas as pd

SESSIONS_DATAFILE = './downloaded_datasets/sessions.csv'
TRAIN_DATAFILE = './downloaded_datasets/train_users_2.csv'

def sum_time_elapsed(df_t, df_s):
  user_total_time = df_s.groupby('user_id', sort=False).agg({'age':'sum'})
  df = df_t.join(user_total_time, on='id')
  print(df)


def main():
  df_t = pd.read_csv(TRAIN_DATAFILE)
  df_s = pd.read_csv(SESSIONS_DATAFILE)
  sum_time_elapsed(df_t, df_s)

if __name__ == '__main__':
  main()