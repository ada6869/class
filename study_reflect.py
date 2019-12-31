# -*- coding: utf-8 -*-
# @Time    : 2019/12/6 10:15
# @Software: PyCharm Community Edition
# @Author  : Ada
# @File    : study_reflect.py

class People:

    number_eye = 2

    def __init__(self,name,age):
        self.name=name
        self.age=age

if __name__ == '__main__':
    p = People('mongo',18)
    print(People.number_eye)
    print(p.number_eye)
    print(p.name)

    #添加属性(给类添加属性)
    setattr(People,'number_leg',2)
    print(hasattr(People,'number_leg'))
    print(People.number_leg)
    setattr(p,"name","huahua")
    print(getattr(p,"name"))


    # 添加属性(给实例添加属性)
    setattr(p,'dance',True)
    print(p.dance)

    #获取实例属性
    getattr(People,'number_leg')#获取类属性
    getattr(p,'dance')#获取实例属性

    #删除实例属性
    delattr(p,'dance')
    getattr(p,'dance')#获取实例属性



