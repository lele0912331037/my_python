#!/usr/bin/env python3 
# -*- coding:utf-8 -*-
import sys,os

if len(sys.argv) <= 3:
    print('usage:./sed.py old_text new_text filename')
    sys.exit()

old_text,new_text,file_name = sys.argv[1],sys.argv[2],sys.argv[3]
new_file = file_name
if "--bak" in sys.argv:
    new_file = file_name+'.bak'
    os.rename(file_name,new_file)
text = ''
fr = open(new_file,'r')
for x in fr.readlines():
   text += x.replace(old_text,new_text)
fr.close()
fw = open(file_name,'w')
fw.write(text)
fw.close()