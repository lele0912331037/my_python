#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Profession(object):

    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes

    def __str__(self, *args, **kwargs):
        print(self.name, self.attributes)
        return '{}{}'.format(self.name, self.attributes)
    __repr__ = __str__


class Race(Profession):

    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes

    def __str__(self, *args, **kwargs):
        return '{}{}'.format(self.name, self.attributes)
    __repr__ = __str__

#a = Profession('人族', '平均')
#a = Race('datang', 'liliang')
#print(a)
