#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Animal(object):
    def run(self, value):
        print('Animal is running...',value)


class Dog(Animal):

    def run(self, value):
        print('Dog is running...', value)


class Cat(Animal):

    def run(self,value):
        print('Cat is running...', value)


def run_twice(animal,str):
    animal.run(str)
    animal.run(str)

dog = Dog()
run_twice(dog,'dddd')