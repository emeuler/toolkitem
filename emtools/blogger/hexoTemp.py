#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
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
 # Last modified: 2016-08-09 14:20
 #
 # Filename: hexoTemp.py
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
import time
import sys
import os

class PyColor(object):
    """ This class is for colored print in the python interpreter!
    "F3" call Addpy() function to add this class which is defined
    in the .vimrc for vim Editor."""
    def __init__(self):
        self.self_doc = """
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

front_matter = """
date:
updated:
title:
tags:
  -
keywords:
  -
categories:
  -
clearReading: true
autoThumbnailImage: yes
thumbnailImage:
thumbnailImagePosition: //[right|left|bottom]
metaAlignment: //[right|left|center]
coverImage:
coverSize: //[partial|full]
coverCaption:
coverMeta: //[in|out]
gallery:
  -
comments:
"""
end_matter = """
---
<!-- toc -->
---
<!-- more -->
---
P.S.
{% img http://7xwwfs.com1.z0.glb.clouddn.com/8bit-dynamiclist_%28reversed%29.gif 32 32 "END" %}

---
"""

def add_time(filename):
    current_time = time.strftime("%Y/%m/%d %H:%M:%S")
    current_time = ' ' + current_time
    front_matter_ls = front_matter.split('\n')
    front_matter_ls[2] += current_time
    front_matter_ls[1] += current_time
    front_matter_ls[3] += ' ' + filename
    strbuf = '\n'.join(front_matter_ls)
    strbuf += end_matter
    with open(filename, 'w') as filebuf:
        filebuf.write(strbuf)

def update(filename):
    current_time = time.strftime("%Y/%m/%d %H:%M:%S")
    current_time = ' ' + current_time
    with open(filename, 'r+') as filebuf:
        buf = filebuf.readlines()
        if buf[2].startswith('updated:'):
            buf[2] = 'updated: ' + current_time + '\n'
            #buf[3] = 'title: ' + filename + '\n'
            filebuf.seek(0)
            filebuf.writelines(buf)

def isnew(filename):
    with open(filename, 'r') as filebuf:
        line_date = filebuf.readline(1)
        line_update = filebuf.readline(2)
        if line_date.endswith(':') and line_update.endswith(':'):
            return True
        else:
            return False

def main(filename):
    try:
        os.path.isfile(filename)
        print(os.getcwd())
        if isnew(filename):
            print('new')
            add_time(filename)
        else:
            print('old')
            update(filename)
    except:
        print('no this file')
        create = input("Create this file in current path? ")
        if create == 'yes' or create == 'Yes' or create == 'y' or create == 'Y':
            print('new file ' + os.getcwd() + '/' + filename)
            os.system('touch ' + filename)
            add_time(filename)
        else:
            print("check the file")

if __name__ == "__main__":
    #add_time('./test')
    #time.sleep(15)
    main(sys.argv[1])
