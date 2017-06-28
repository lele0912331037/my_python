#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Province:

    def __init__(self, name, age, job, w_from, city, money):
        self.name = name
        self.age = age
        self.job = job
        self.w_from = w_from
        self.city = city
        self.__money = money
    def __str__(self):
        return