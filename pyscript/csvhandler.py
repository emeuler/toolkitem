#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
 #        .---.         .-----------
 #       /     \  __  /    ------
 #      / /     \(  )/    -----   (`-')  _ _(`-')              <-. (`-')_
 #     //////    '\/ `   ---      ( OO).-/( (OO ).->     .->      \( OO) )     .->
 #    //// / //  :   : ---      (,------. \    .'_ (`-')----. ,--./ ,--/  ,--.'  ,-.
 #   // /   /  / `\/ '--         |  .---' '`'-..__)( OO).-. ' |   \ |  | (`-')'.'  /
 #  //          //..\\          (|  '--.  |  |  ' |( _) | | | |  . '|  |)(OO \    /
 # ============UU====UU====      |  .--'  |  |  / : \|  |)| | |  |\    |  |  /   /)
 #             '//||\\`          |  `---. |  '-'  /  '  '-' ' |  | \   |  `-/   /`
 #               ''``            `------' `------'    `-----' `--'  `--'    `--'
 # ######################################################################################
 #
 # Author: edony - edonyzpc@gmail.com
 #
 # twitter : @edonyzpc
 #
 # Last modified: 2015-10-30 23:32
 #
 # Filename: cvshandler.py
 #
 # Description: All Rights Are Reserved
 #
"""
#import scipy as sp
#import math as m
#import matplotlib as mpl
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D as Ax3
#from scipy import stats as st
#from matplotlib import cm
#import numpy as np
import csv

class PyColor(object):
    """ This class is for colored print in the python interpreter!
    "F3" call Addpy() function to add this class which is defined
    in the .vimrc for vim Editor."""
    def __init__(self):
        self.self_doc = r"""
        STYLE: \033['display model';'foreground';'background'm
        DETAILS:
        FOREGROUND        BACKGOUND       COLOR
        ---------------------------------------
        30                40              black
        31                41              red
        32                42              green
        33                43              yellow
        34                44              blue
        35                45              purple
        36                46              cyan
        37                47              white
        DISPLAY MODEL    DETAILS
        -------------------------
        0                default
        1                highlight
        4                underline
        5                flicker
        7                reverse
        8                non-visiable
        e.g:
        \033[1;31;40m   <!--1-highlight;31-foreground red;40-background black-->
        \033[0m         <!--set all into default-->
        """
        self.warningcolor = '\033[0;31m'
        self.tipcolor = '\033[0;32m'
        self.endcolor = '\033[0m'
        self._newcolor = ''
    @property
    def new(self):
        """
        Customized Python Print Color.
        """
        return self._newcolor
    @new.setter
    def new(self, color_str):
        """
        New Color.
        """
        self._newcolor = color_str
    def disable(self):
        """
        Disable Color Print.
        """
        self.warningcolor = ''
        self.endcolor = ''

__description__ = """
                  This is the rough idea about abstracting the matched date of stocks id.
                  """
# TODO(edony): this script takes lots of memory to query the matched item, it needs to optimize.
def ReadCSV(filename):
    with open(filename) as filebuf:
        csvreader = csv.reader(filebuf)
        return [item for item in csvreader]

def Date2Digit(date_str):
    if '/' in date_str:
        return [int(item) for item in date_str.split('/') if item]
    if '-' in date_str:
        return [int(item) for item in date_str.split('-') if item]

def CustomizedDateCSV(csv_ls):
    data = {}
    for item in csv_ls:
        temp = [Date2Digit(d) for d in item[1:]]
        data[item[0]] = temp
    if len(csv_ls) == len(data.keys()):
        return data
    else:
        print('Wrong input file for contains repeated keys!')

#def prePriceCSV(csv_ls):
#    return [[item[1],item[0],item[2]] for item in csv_ls]

def PriceCSV(csv_ls):
    price = [[Date2Digit(item[0]), item[1], float(item[2])] for item in csv_ls]
    price.sort(key=lambda x:x[0])
    hashprice = {}
    #[hashprice[item[1]].append([item[0],item[1]]) for item in price]
    for item in price:
        if not item[1] in hashprice.keys():
            hashprice[item[1]] = []
        if item[2] <= 0.0995:
            hashprice[item[1]].append([item[0],item[2]])
    return hashprice

def matchDP(id, hashprice):
    matched = {}
    for key in id.keys(): #股票代码
        tmp = []
        for d in id[key]: #日期
            if d:
                mems = hashprice[key]
                mems.sort(key=lambda x:x[0])
                if key == '300092':
                    print(mems)
                for item in mems:
                    if item[0] <= d:
                        continue
                    elif item[0] in tmp:
                        continue
                    else:
                        tmp.append(item[0])
        matched[key] = tmp
    return matched

def WriteCSV(ls):
    lines = [ls[key] for key in ls.keys() if not ls[key].insert(0, key)]
    with open("./test.csv",'w+') as filebuf:
        writer = csv.writer(filebuf)
        for line in lines:
            writer.writerow(line)

if __name__ == '__main__':
    date = ReadCSV('./CodeDate.csv')
    dig_date = CustomizedDateCSV(date)
    #print(len(dig_date.keys()))
    price = ReadCSV('./PriceLimit.csv')
    #price_ = prePriceCSV(price)
    hashprice = PriceCSV(price)
    for i, key in enumerate(hashprice.keys()):
        if i == 0:
            hashprice[key]
        else:
            break
    ls = matchDP(dig_date, hashprice)
    WriteCSV(ls)
    #WriteCSV(hashprice)
    #print(hashprice['000030'])
    #print(dig_price[0:1000])
    #print(price[0])
    #date.sort()
    #print(set(date))
