import pandas as pd
onehotlist = ['gender', 'signup_method', 'language', 'affiliate_channel', 'affiliate_provider', 'first_affiliate_tracked', 'signup_app', 'first_device_type', 'first_browser']

def main():
  df = pd.read_csv('processed_user.csv')
  for col in onehotlist:
    df = onehot(df, col)
  cols = df.columns.tolist()
  index_country = cols.index('country_destination')
  new_cols = cols[:index_country] + cols [index_country+1:] + cols[index_country: index_country+1]
  df = df[new_cols]

  df.to_csv('processed_user_onehot.csv', index=False)

def onehot(df, col):
  print(col)
  return pd.get_dummies(df, columns=[col],prefix=col)


if __name__ == '__main__':
  main()