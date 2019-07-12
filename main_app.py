# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 16:27:43 2019

@author: surpandey
"""
import print_module

name=''
age=''
mobile_num=''
city=''

print('Welcome Telsa is coming to your town, Book your tickets now and enjoy!!')

name=input('Please enter your name')
if(not name):
    name=input('oooPs you can not proceed without name')

age=input('Please enter your age')
if(not age):
    name=input('Sorry you need to specify your age ')

mobile_num=input('Please enter your mobile number')
if(not mobile_num):
    name=input('Entering mobile number is must')

city=input('Please enter your city')
if(not city):
    name=input('Its mandatory to specify where you are coming from')
print("How do you want to get your booking details?")
dist_data={
        'name':name,
          'age':age,
       'mobile num':mobile_num,
          'city':city
        }
f_in = open("config.txt", "r")
for component in f_in:
  print(component.lower())
report_type=input()
report_type=report_type.lower()
print_module.print_report(report_type,dist_data)

