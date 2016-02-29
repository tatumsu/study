import pickle
import user
if __name__ == '__main__':
    tatum = user.User('tautm', 36, 'tatum.su@augmentum.com')
    father = user.User('su.qiling', 63, 'su.qiling@163.com')
    mother = user.User('tang.yunzhen', 61, 'tang.yunzheng@163.com')

    tatum.father = father
    tatum.mother = mother

    print('Dump user object as string:')
    str = pickle.dumps(tatum)
    print(str)

    print('Dump user object to file users.data')
    f = open('users.data', 'bw')
    pickle.dump(tatum, f)
    f.close()
    print('Dump successfully')

    print('Load user object from file users.data')
    f = open('users.data', 'br')
    bullstb = pickle.load(f)
    f.close()
    print('Load user object successfully:')
    print(tatum)
