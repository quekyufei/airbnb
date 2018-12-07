import pandas as pd
import numpy as np

def main(userfile, sessionsfile):
    ufile = pd.read_csv(userfile)
    sfile = pd.read_csv(sessionsfile)
    actions = sfile['action']
    uselessActions = getUselessActions(actions)
    # sfile.action = np.where(df.action.isin(list_of_actions), ‘other’, df.action)
    # for i, row in sfile.iterrows():
    #     if row['action'] in uselessActions:
    #         sfile.drop(index=i)
    temp = sfile[~sfile.action.isin(uselessActions)][['user_id', 'action']]
    print(pd.get_dummies(pd.concat([temp[['user_id']], pd.get_dummies(temp[['action']])], axis=1)))
    # agg_sessions = temp.groupby('user_id').action.value_counts()
    # print(agg_sessions.to_frame())

    # new = ufile.set_index('id').join(temp2.set_index('user_id'))
    # print(new)

    #
    # for i, row in ufile.iterrows():


def getUselessActions(actions):
    actioncount = {}
    for action in actions:
        if action not in actioncount:
            actioncount[action] = 1
        else:
            actioncount[action] += 1
    uselessActions = set()
    for action in actioncount:
        if actioncount[action] < 5000:
            uselessActions.add(action)
    return uselessActions

if __name__ == '__main__':
    main('train_users_2.csv','sessions.csv')
