#!/bin/bash
# author: edony
echo "EDIT HTML..."
sys=$(uname)
sys_m="Darwin"
sys_l="Linux"
if [ "$sys" == "$sys_l" ] 
then
    $BROWSER /home/edony/code/github/blog/tiny.html
fi
if [ "$sys" == "$sys_m" ]
then
    open $BROWSER /Users/edony/coding/blog/tinyMac.html
fi
