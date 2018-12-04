import pandas as pd

# get count of unique ids seen in sessions.csv
sessions = pd.read_csv('/Users/QuekYufei/Downloads/all/sessions.csv')
counted = sessions['user_id'].value_counts(sort=False)
counted.to_csv('/Users/QuekYufei/Downloads/all/sessions_counted.csv')

# In between these lines I added a row to sessions_counted with col names: [id,session_count]

# join the train and session count data
main = pd.read_csv('/Users/QuekYufei/Downloads/all/train_users_2.csv')
new = main.set_index('id').join(counted.set_index('id'))

# swap columns around
cols = new.columns.tolist()
cols = cols[:-2] + cols[-1:] + cols[-2:-1]
new = new[cols]

# save to file
new.to_csv('/Users/QuekYufei/Downloads/all/train_and_count.csv')