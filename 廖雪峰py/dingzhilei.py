#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, ages):
        self._name = name
        if not isinstance(ages, int):
            raise ValueError('ages must be an integer!')
        if ages<1 or ages>100:
            raise ValueError('ages must between 1 - 100!')
        self._ages = ages

    @property
    def ages(self):
        return self._ages
    @ages.setter
    def ages (self,ages):
        if not isinstance(ages, int):
            raise ValueError('ages must be an integer!')
        if ages<1 or ages>100:
            raise ValueError('ages must between 1 - 100!')
        self._ages = ages      
    def __str__(self):
        return 'Student object (name: %s,age: %s)' % (self._name,self._ages)
    __repr__ = __str__


class Fib(object):
    def __init__(self):
       self.a,self.b=0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>1000:
            raise StopIteration()
        return self.a
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b = 1,1
            for x in range(n):
                a,b = b,a+b
            return a
        if isinstance(n,slice):
            start=n.start
            stop=n.stop
            if start is None:
                start=0
            a,b = 1,1
            L=[]
            for x in range(stop):
                if x>start:
                    L.append(a)
                a,b=b,a+b
            return L
    def __str__(self):
        return '%s %s' % (self.a,self.b)
    __repr__ = __str__

class Chain1(object):

    def __init__(self, path=''):
        self._path = path
    def __getattr__(self,path):
        return Chain1('%s/%s' % (self._path,path))
    def __str__(self):
        return self._path
    __repr__ = __str__

class Chain(object):

    def __init__(self, path='GET '):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s-%s' % (self._path,path))

    #def __call__(self,path):
     #   return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__