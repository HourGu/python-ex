#mydict,change the way of calling a dict
class Dict(dict):
    def __init__(self,**kw):
        super(Dict,self).__init__(**kw)

    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'dict'object has no attribuate '%S'"%key)

    def __setattr__(self,key,value):
        self[key]=value


'''
>>> d=Dict(a=1,b=2,c=3)
>>> d.c
3
>>> 
>>> d['a']
1
>>> 
'''
