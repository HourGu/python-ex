# -*- coding: cp936 -*-
###collections����ģ��


##namedtuple,namedtuple��һ������������������һ���Զ����tuple����
#���ҹ涨��tupleԪ�صĸ����������������Զ���������������tuple��ĳ��Ԫ�ء�
from collections import namedtuple
P=namedtuple('Point',['x','y'])#�൱�ڴ���һ��P��class��
                    #�̳���namedtuple�����Ժ�һ��name��list
p=P(1,2)#ins
'''
>>> p.x
1
>>> p.y
2

'''
# namedtuple('����', [����list]):
Circle = namedtuple('Circle', ['x', 'y', 'r'])



##deque
#deque��Ϊ�˸�Чʵ�ֲ����ɾ��������˫���б���ʺ����ڶ��к�ջ��
>>> from collections import deque

>>> q=deque(['a','b','c'])
>>> q.append ('x')
>>> q
deque(['a', 'b', 'c', 'x'])
>>> q.appendleft ('y')
>>> q
deque(['y', 'a', 'b', 'c', 'x'])

>>> q.pop()
'x'
>>> q
deque(['y', 'a', 'b', 'c'])

>>> q.popleft()
'y'
>>> q
deque(['a', 'b', 'c'])
>>> 


##defaultdict
>>> from collections import defaultdict
>>> dd=defaultdict(lambda:'N/A')
>>> dd['key1']='abc'
>>> dd['key2']
'N/A'
>>> dd['key1']
'abc'



##OrderDict
>>> d=dict([('a',1),('b',2),('c',3)])
>>> d
{'a': 1, 'c': 3, 'b': 2}
>>> d=OrderedDict([('a',1),('b',2),('c',3)])
>>> d
OrderedDict([('a', 1), ('b', 2), ('c', 3)])
>>> 

#OrderedDict����ʵ��һ��FIFO���Ƚ��ȳ�����dict����������������ʱ����ɾ��������ӵ�Key��
from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print 'remove:', last
        if containsKey:
            del self[key]
            print 'set:', (key, value)
        else:
            print 'add:', (key, value)
        OrderedDict.__setitem__(self, key, value)



##Counter������
>>> from collections import Counter
>>> c=Counter()
>>> for ch in 'programming':
	c[ch]=c[ch]+1

	
>>> c
Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})
>>> 
