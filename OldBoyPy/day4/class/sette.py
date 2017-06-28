#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class test:
    def __init__(self, value):
        self.__Value = value

    @property
    def get_private(self):
        return self.__Value

    @get_private.setter
    def get_private(self, value):
        self.__Value = value

a = test('woke')
print(a.get_private)
a.get_private = '123'
print(a.get_private)