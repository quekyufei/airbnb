from train_dataset_processing import *
from datetime_processing import *
from action_processing import *
import pandas as pd

df = pd.read_csv('train_and_count.csv')
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
cols = df.columns.tolist()
new_cols = cols[:-3] + cols [-2:] + cols[-3:-2]
df = df[new_cols]
print("formatted date")
df = processAction(df)
print("processed action")
df.session_count = df.session_count.fillna(0)
df = df.fillna('other')
df.
df = df.drop(columns=['id'])
df.to_csv('processed_user.csv', index=False)
