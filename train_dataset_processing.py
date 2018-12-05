import pandas as pd
import numpy as np
from datetime import datetime

def main():
	df = pd.read_csv('train_and_count.csv')
	df = simplify_classes(df)
	df = process_age(df)
	df = process_affiliate_channel(df)
	df = process_languages(df)
	df = process_first_browser(df)
	df = diff_active_create(df)
	df.to_csv('modified_datasets/boolClass_age_affchn_lan_browser.csv', index=False)

def simplify_classes(df):
	df.country_destination = np.where(df.country_destination=='NDF', 'NDF', 'Booked')
	return df

def process_age(df):
	# ~2% increase in accuracy with NBC
	df.age = np.where(df.age>100, 100, df.age)
	df.age = np.where(df.age<16, 16, df.age)

	df.age = np.where(np.isnan(df.age), 37.735711, df.age)
	return df

def process_affiliate_channel(df):
	# Doesn't seem to help; slight increase in accuracy
	aff_chn = ['direct', 'sem-brand', 'sem-non-brand', 'other']
	df.affiliate_channel = np.where(df.affiliate_channel.isin(aff_chn), df.affiliate_channel, 'other')
	return df

def process_languages(df):
	# Doesn't seem to help; slight increase in accuracy
	list_language = ['en', 'zh', 'fr']
	df.language = np.where(df.language.isin(list_language), df.language, 'other')
	return df

def process_first_browser(df):
	browser_list = ['Chrome', 'Safari', 'Firefox', '-unknown-', 'IE', 'Mobile Safari']
	df.first_browser = np.where(df.first_browser.isin(browser_list), df.first_browser, 'other')
	return df

def diff_active_create(df):
	first_active = df.timestamp_first_active
	account_created = df.date_account_created

	df['active-create-difference'] = df.apply(lambda row: parse_date_difference(str(row.date_account_created), str(row.timestamp_first_active)), axis=1)
	return df


def parse_date_difference(create, active):
	# 2010-06-28
	account = datetime.strptime(create, '%Y-%m-%d')
	# 20090319043255
	active = datetime.strptime(active, '%Y%m%d%H%M%S')
	delta = account - active
	return delta.days


if __name__ == '__main__':
	main()