import pandas as pd 
import csv 

def add_phone_delete_phone (maincsv):
    toadd = pd.read_csv('add_delete_phone.csv')
    new = pd.merge(maincsv, toadd, how='left', left_on='id', right_on='id')
    return new 

def user_devices(maincsv):
    toadd = pd.read_csv('user_devices.csv')
    new = pd.merge(maincsv, toadd, how='left', left_on='id', right_on='id')
    return new 

maincsv = pd.read_csv('processed_user.csv')

maincsv = add_phone_delete_phone(maincsv)
maincsv = user_devices(maincsv)

maincsv.to_csv('processed_user_2.csv',index=False)