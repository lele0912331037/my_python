#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# yield应用，模拟xreadline


def MyxReadlines():
    seek = 0
    while True:
        with open('domain改进版.sh', 'r') as f:
            f.seek(seek)
            date = f.readline()
            if date:
                seek = f.tell()
                yield date
            else:
                return
for i in MyxReadlines():
    print(i.strip('\n'))



def MyxReadline():
    seek = 0
    while True:
        with open('domain改进版.sh', 'r') as f:
            f.seek(seek)
            date = f.readline()
            if date:
                seek = f.tell()
                print(date)
            else:
                return
for i in MyxReadline():
    print(i.strip('\n'))
