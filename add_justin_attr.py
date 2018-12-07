import csv
import pandas as pd

def add_add_delete_phone_attribute(trainusers2):
    users = dict()
    headers = ['user_id', 'added_phone', 'deleted_phone']

    with open('downloaded_datasets/sessions.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0] == 'user_id':
                continue
                
            elif row[0] not in users :
                users[row[0]] = list()
                if row[3] == 'create_phone_numbers':
                    users[row[0]].append(1)
                else:
                    continue
            
            elif row[0] in users and row[3] == 'create_phone_numbers' and len(users[row[0]]) == 0:
                users[row[0]].append(1)
            
            elif row[0] in users and row[3] == 'delete_phone_numbers' and len(users[row[0]]) == 1:
                users[row[0]].append(1)

    for user in users:
        if len(users[user]) == 0:
            users[user].append(0)
            users[user].append(0)
        
        if len(users[user]) == 1 and users[user][0] == 1:
            users[user].append(0)
            
    with open('modified_datasets/add_delete_phone.csv', 'w', newline = '') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(headers)
        for user in users:
            row = [user]
            row += users[user]
            csv_writer.writerow(row)

    toadd = pd.read_csv('modified_datasets/add_delete_phone.csv')
    new = pd.merge(trainusers2, toadd, how='left', left_on='id', right_on='user_id')
    return new 

def add_user_devices(trainusers2):
    users = dict()
    oldheaders = list()
    headers = ['user_id']
    devices = list()

    with open('downloaded_datasets/sessions.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0] == 'user_id':
                oldheaders = row
                
            elif row[0] not in users:
                users[row[0]] = list()
                if row[4] not in users[row[0]]:
                    users[row[0]].append(row[4])
            
            elif row[0] in users:
                if row[4] not in users[row[0]]:
                    users[row[0]].append(row[4])
            

    with open('downloaded_datasets/sessions.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        linecount = 0
        for row in csv_reader:
            if row[0] == 'user_id':
                pass
            elif row[4] not in devices:
                devices.append(row[4])
                
    headers += devices

    with open('modified_datasets/user_devices.csv', 'w', newline = '') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(headers)
        for user in users:
            row = [user]
            for device in devices:
                if device in users[user]:
                    row += '1'
                else:
                    row += '0'
            csv_writer.writerow(row)
    
    toadd = pd.read_csv('modified_datasets/user_devices.csv')
    new = pd.merge(trainusers2, toadd, how='left', left_on='id', right_on='user_id')
    return new 






        
