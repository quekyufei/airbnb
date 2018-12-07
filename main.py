from train_dataset_processing import *
from adding_total_browse_time import *
from datetime_processing import *
from action_processing import *
from adding_sessions_count import *
import pandas as pd

df = pd.read_csv('downloaded_datasets/train_users_2.csv')
df_s = pd.read_csv('downloaded_datasets/sessions.csv')
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
df = df.fillna('other')
df = df.drop(columns=['id'])
cols = df.columns.tolist()
index_country = cols.index('country_destination')
new_cols = cols[:index_country] + cols [index_country+1:] + cols[index_country: index_country+1]
df = df[new_cols]
df.to_csv('processed_user.csv', index=False)
