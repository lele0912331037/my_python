#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class father(object):

    def __init__(self, name):
        self.Fname = name
        print('father.__init__')

    def F_Func(self):
        print('father.Func')

    def bad(self):
        print('father.bad.function')


class Son(father):

    def __init__(self,son):
        self.Son = son
        print('Son.__init__')
        # 调用父类的__init__方法
        # 方法1
        father.__init__(self)
        # 方法2
        #super(Son, self).__init__()

    def S_Func(self):
        print('Son.func')

    def bad(self):
        print('son.bad.function')

    def S_bad(self):
        father.bad(self)
        print('son.bad.function')
#set1 = father('555')
set1 = Son('123')
#set1 = Son('123')
#print(set1)
#set1.S_Func()
#set1.F_Func()
#set1.bad()
print('\n')
#set1.S_bad()

#Son()