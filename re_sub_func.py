#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Function:
【整理】详解Python中re.sub
http://www.crifan.com/python_re_sub_detailed_introduction
 
Version:    2013-05-02
Author:     Crifan
Contact:    admin (at) crifan.com
"""
 
import re;
 
def pythonReSubDemo():
    """
        demo Pyton re.sub
    """
    inputStr = "hello 123 world 456 nihao 789";
     
    def _add111(matched):
        intStr = matched.group("number"); #123
        intValue = int(intStr);
        addedValue = intValue + 111; #234
        addedValueStr = str(addedValue);
        return addedValueStr;
         
    replacedStr = re.sub("(?P<number>\d+)", _add111, inputStr,2);
    print "replacedStr=",replacedStr; #hello 234 world 567 nihao 789
 
###############################################################################
if __name__=="__main__":
    pythonReSubDemo();
