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
 # Last modified: 2016-01-06 21:10
 #
 # Filename: login_sched.py
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
import os
import sys
import platform as pf
from scheduler import sched_tasks

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

def update_linux():
    "CDM `update -l` for updating Linux Packages."
    os.system('update -l')

def update_path(path):
    "CMD `update -p $path` for update repositories in $path."
    os.system('update -p ' + path)

def update_git():
    "CMD `update -g` for update repositories in default path."
    os.system('update -g')

def weather():
    "CMD `update -w` for checking the weather info in 24h."
    os.system('update -w')

def update_mac():
    "CMD `update -g` for update repositories in Mac default path."
    os.system('update -m')

def login_sched(sysinput, path=None):
    """
    Login default scheduler actions.
    """
    jobs = [update_path, update_git, weather]
    kwargs = {update_path.__name__:[path],\
            update_git.__name__:None, weather.__name__:None}
    if pf.system() == 'Darwin':
        jobs.append(update_mac)
        kwargs[update_mac.__name__] = None
    if pf.system() == 'Linux':
        jobs.append(update_linux)
        kwargs[update_linux.__name__] = None
    sched_tasks(jobs, timestr=sysinput, **kwargs)

if __name__ == '__main__':
    # default login action
    login_sched(os.system('date +%Y-%m-%d-%H-%M-%S'), path='~/.vim/bundle/')

