# from tempfile import TemporaryFile
# from PyQt5.QtWidgets import QApplication
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# import pandas as pd
# import sys
# import os
# import re

# def outputnum(content):
#     if content.isnumeric():
#         return content

# a=[0,500,1000,1200,1500,1600,1700,1800,1900,1920,1940,1950,1955,1960,1965,1970,1975,1980,1982,1984,1986,1988,1990,1992,1994,1996,1998,2000,2002,2004,2006,2008,2010]
# b=[-i for i in a]
# print(b)


import random
students=[1,2,3,4,5,6,7,8]
A=[]
B=[]
C=[]
pods=[A,B,C]
def assign_pod(students:list):
    for student in students:
        podsNfull=[]
        for pod in pods:
            if len(pod)<3:
                podsNfull.append(pod)
        randompod=random.choice(podsNfull)
        randompod.append(student)

assign_pod(students)
print(pods)


