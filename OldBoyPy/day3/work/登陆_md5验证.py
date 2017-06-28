# -*- coding: utf-8 -*-
db = dict
db = {'3': 'e10adc3949ba59abbe56e057f20f883e', '23': 'e10adc3949ba59abbe56e057f20f883e'}


def get_md5(username,password):
    import hashlib
    md5 = hashlib.md5()
    # 统一加盐位置, 避免register和login加盐不一致,导致验证错误;
    md5.update((password + username + '456').encode('utf-8'))
    return md5.hexdigest()


def register(username,password):
    # 验证 用户名密码是否合法
    if username in db or username == ''or password == '':
        print('Username/password error')
    else:
        db[username] = get_md5(username,password)


def login(username,password):
    # 验证 用户名密码是否合法
    if username not in db or username == ''or password == '':
        exit('Username/password error')
    else:
        if db[username] == get_md5(username, password):
            print('welcome')
        else:
            print('please check username or password.')

if __name__ == '__main__':
    while True:
        choose = input('1. regist;\n2. login;\n3. exit.\n')
        if choose == '1':
            register(input('input username:'), input('input password:'))
        elif choose == '2':
            login(input('input username:'), input('input password:'))
        elif choose == '3':
            print(db)
            print('Bye.')
            break
        else:
            print('Input error.')