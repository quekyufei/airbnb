
import datetime
import pandas as pd
import math

INPUT = './all/train_users_2.csv'
OUTPUT = './all/train_users_3.csv'




def main(file, output_file):
  df = pd.read_csv(file)
  df = process_date(df)
  cols = df.columns.tolist()
  new_cols = cols[:-3] + cols [-2:] + cols[-3:-2]
  df = df[new_cols]
  df.to_csv(output_file, index=False)


def process_date(df):
  dates = df['date_account_created']
  daysWeek = []
  daysYear = []
  for date in dates:
    date_obj = getDateObj(date)
    if not date_obj:
      daysWeek.append(0)
      daysYear.append(0)
      continue
    daysWeek.append(getDayOfWeek(date_obj))
    daysYear.append(getDayOfYear(date_obj))
  df['dayOfWeek'] = daysWeek
  df['dayOfYear'] = daysYear

  return df.drop('date_account_created', axis=1).drop('date_first_booking', axis=1).drop('timestamp_first_active', axis=1)


def getDateObj(s):
  if not isinstance(s, str):
    return None
  (day, month, year) = [int(x) for x in s.split('/')]
  return datetime.date(year, month, day)


def getDayOfWeek(date_obj):
  return date_obj.isoweekday()

def getDayOfYear(date_obj):
  return date_obj.toordinal() - datetime.date(date_obj.year, 1, 1).toordinal() + 1

if __name__ == '__main__':
  main(INPUT, OUTPUT)