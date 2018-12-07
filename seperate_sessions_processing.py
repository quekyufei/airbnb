import pandas as pd

def addColumnWhetherInSession(df_t, df_s):
  df3 = df_t.id.isin(df_s.user_id.unique())
  # df3 = df_s.user_id.isin(df_t.id)
  # in_sess_list = []
  # print(df3)
  # for data in df_t.id:
  #   if data in df3:
  #     in_sess_list.append(True)
  #   else:in_sess_list.append(False)
  df_t['is_present_in_session'] = df3
  df_t.to_csv('./modified_datasets/in_session_column.csv', index=False)

if __name__ == '__main__':
  addColumnWhetherInSession(pd.read_csv('./downloaded_datasets/train_users_2.csv'), pd.read_csv('./downloaded_datasets/sessions.csv'))
