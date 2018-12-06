import pandas as pd
import numpy as np
def main(userfile):
    ufile = pd.read_csv(userfile)
    return processAction(ufile)


def processAction(ufile):
    sfile = pd.read_csv('./downloaded_datasets/sessions.csv')
    actions = sfile['action']
    uselessActions = getUselessActions(actions)
    temp = sfile[~sfile.action.isin(uselessActions)][['user_id', 'action']]
    print("removing useless action")
    temp2 = pd.concat([temp[['user_id']], pd.get_dummies(temp[['action']])], axis=1)
    print("concat done")
    temp3 = temp2.groupby(['user_id']).sum()
    print("agg done")
    new = pd.merge(ufile, temp3, how='left', left_on = 'id', right_on = 'user_id')
    return new

def getUselessActions(actions):
    actioncount = {}
    for action in actions:
        if action not in actioncount:
            actioncount[action] = 1
        else:
            actioncount[action] += 1
    uselessActions = set()
    for action in actioncount:
        if actioncount[action] < 10000:
            uselessActions.add(action)
    return uselessActions

if __name__ == '__main__':
    main('./all/train_users_2.csv')
