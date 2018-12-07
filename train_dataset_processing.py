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
	# Create new row
	df['active-create-difference'] = df.apply(lambda row: parse_date_difference(str(row.date_account_created), str(row.timestamp_first_active)), axis=1)
	return df

def parse_date_difference(create, active):
	# 2010-06-28
	account = datetime.strptime(create, '%Y-%m-%d')
	# 20090319043255
	active = datetime.strptime(active, '%Y%m%d%H%M%S')
	delta = account - active
	return delta.days	

def onehot_gender(df):
	return pd.get_dummies(df, columns=['gender'],prefix='gender')

def onehot_signup_method(df):
	return pd.get_dummies(df, columns=['signup_method'],prefix='su_method')

def onehot_language(df):
	return pd.get_dummies(df, columns=['language'],prefix='lan')

def onehot_aff_chnl(df):
	return pd.get_dummies(df, columns=['affiliate_channel'],prefix='aff_chn')

def onehot_aff_prov(df):
	return pd.get_dummies(df, columns=['affiliate_provider'],prefix='aff_prov')

def onehot_1st_aff_trck(df):
	return pd.get_dummies(df, columns=['first_affiliate_tracked'],prefix='1st_aff_trck')

def onehot_su_app(df):
	return pd.get_dummies(df, columns=['signup_app'],prefix='su_app')

def onehot_1st_dev(df):
	return pd.get_dummies(df, columns=['first_device_type'],prefix='1st_dev')

def onehot_1st_brow(df):
	return pd.get_dummies(df, columns=['first_browser'],prefix='1st_brow')

if __name__ == '__main__':
	main()