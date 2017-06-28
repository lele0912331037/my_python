#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

# 长用于接口
class Alert:
    __metaclass__ = ABCMeta

    @abstractmethod
    def Send(self): pass


class Weixin(Alert):

    def __init__(self):
        print('__init__')

    def Send(self):
        print('send.weixin')
c = Weixin()
c.Send()
