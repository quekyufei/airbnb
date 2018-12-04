import pandas as pd
import numpy as np

def main():
	df = pd.read_csv('train_and_count.csv')
	df = simplify_classes(df)
	df = process_age(df)
	df = process_affiliate_channel(df)
	df.to_csv('modified_datasets/boolClass_age_affchn.csv', index=False)

def simplify_classes(df):
	df.country_destination = np.where(df.country_destination=='NDF', 'NDF', 'Booked')
	return df

def process_age(df):
	df.age = np.where(df.age>100, 100, df.age)
	df.age = np.where(df.age<16, 16, df.age)

	df.age = np.where(np.isnan(df.age), 37.735711, df.age)
	return df

def process_affiliate_channel(df):
	aff_chn = ['direct', 'sem-brand', 'sem-non-brand', 'other']
	df.affiliate_channel = np.where(df.affiliate_channel.isin(aff_chn), df.affiliate_channel, 'other')
	return df

if __name__ == '__main__':
	main()	