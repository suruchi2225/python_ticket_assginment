# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 15:33:42 2019

@author: surpandey
"""


import json
import pdfkit
def print_report(content_type, dist_dat):
    if(content_type=='text'):
        with open('ticket_details.txt', 'w') as outfile:  
            outfile.write("Find your details below")
            json.dump(dist_dat, outfile)
        print("your details are successfully placed to text file ticket_details")
    if(content_type=='pdf'):
        with open('ticket_details.pdf', 'w') as outfile:  
            outfile.write("Find your details below")
            json.dump(dist_dat, outfile)
        print("your details are successfully placed to text file ticket_details")
        
    