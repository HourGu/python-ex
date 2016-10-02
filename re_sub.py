# -*- coding: cp936 -*-
>>> inputStr = "hello crifan, nihao crifan��jhsa crifan"
>>> import re
>>> replacedStr = re.sub(r"hello (\w+), nihao \1��jhsa \1", "crifanli", inputStr)
>>> print "replacedStr=",replacedStr
replacedStr= crifanli
>>> 
inputStr = "hello crifan, nihao crifan";
replacedStr = re.sub(r"hello (\w+), nihao \1", "\g<1>", inputStr);
print "replacedStr=",replacedStr; #crifan

inputStr = "hello crifan, nihao crifan";
replacedStr = re.sub(r"hello (?P<name>\w+), nihao (?P=name)", "\g<name>", inputStr);
print "replacedStr=",replacedStr; #crifan

replacedStr = re.sub(replacePattern, orignialStr, replacedPartStr, 1, re.I); # must designate count parameter
