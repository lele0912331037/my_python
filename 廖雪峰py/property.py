#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用@property
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width=value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height=value

    @property
    def resolution(self):
        self._resolution = self._height*self._width
        return self._resolution
# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution