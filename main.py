from train_dataset_processing import *
from adding_total_browse_time import *
from datetime_processing import *
from action_processing import *
from adding_sessions_count import *
from add_justin_attr import *
import onehot as oh
import pandas as pd

def shiftCountryDestination(df):
  cols = df.columns.tolist()
  index_country = cols.index('country_destination')
  new_cols = cols[:index_country] + cols [index_country+1:] + cols[index_country: index_country+1]
  return df[new_cols]



df = pd.read_csv('downloaded_datasets/train_users_2.csv')
df_s = pd.read_csv('downloaded_datasets/sessions.csv')
df = add_add_delete_phone_attribute(df)
print('Added deleted phone attributes')
df = add_user_devices(df)
print('Added user devices')
df = addSessionsCount(df, df_s)
print('Added sessions count')
df = sumTimeElapsed(df, df_s)
print('Added the time spent in total')
df = simplify_classes(df)
print("simplified classes")
df = process_age(df)
print("processed age")
df = process_affiliate_channel(df)
print("processed channel")
df = process_languages(df)
print("processed languages")
df = process_first_browser(df)
print("processed browser")
df = diff_active_create(df)
print("processed active diff")
df = process_date(df)
print("processed date")
print("formatted date")
df = processAction(df)
print("processed action")
df.session_count = df.session_count.fillna(0)
df = df.fillna(0)
df = df.drop(columns=['id'])

for col in oh.onehotlist:
  df = oh.onehot(df, col)

df = shiftCountryDestination(df)
df = df.drop(columns=['user_id_x', 'user_id_y'])

df.to_csv('modified_datasets/processed_user_onehot.csv', index=False)

