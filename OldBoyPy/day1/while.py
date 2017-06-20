#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

count = 0
while True:
    print_num = int(input('Which loop do you want it to be printed out:'))
    if print_num <=count:
        print ('已经过了%s' % (print_num))
        continue
    while True:
        if count == print_num:
            print ('There you got the number:', count)
            choice = input('Do you want to continue the loop?(y/n)')
            if choice == 'n':
                sys.exit()
            else:
                break
        count += 1
        print ('loop:', count)  