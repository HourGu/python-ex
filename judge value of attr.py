##judge value of attribute
class Student(object):
    def set_score(self,score):
        if 0<=score<=100:
            self.score=score
        else:
            raise ValueError('score should be 0~100')

    def get_score(self):
        return self.score


'''
>>> s=Student()
>>> s.set_score(23)
>>> s.get_score()
23
>>> s.set_score (133)

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    s.set_score (133)
  File "E:/Python27/python ex/judge value of attr.py", line 7, in set_score
    raise ValueError('score should be 0~100')
ValueError: score should be 0~100
'''

##@property  @score.setter
class Student(object):
    @property  #getter method is changged to an attr,making a @score_setter
    def score(self):
        return self.score

    @score.setter
    def score(self,score):
        if not isinstance(score,int):
            raise ValueError('score must be an integer!')
        if score<0 or score>100:
            raise ValueError('score must between 0~100')
        self.score=score


'''
>>> s = Student()
>>> s.score = 60
>>> s.score
60
>>> s.score = 60.6

Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    s.score = 60.6
  File "E:\Python27\temporary.py", line 9, in score
    raise ValueError('score must be an integer!')
ValueError: score must be an integer!
'''
