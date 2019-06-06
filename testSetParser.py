"""
Created on Wed Mar 20 14:05:25 2019

@author: u180530
Script to Take 20% test set
"""

count = 0

file = open(r"C:\Users\u180530\Desktop\FYP\Data\Final\TEX.txt", encoding = 'ansi')
file_object = open(r"C:\Users\u180530\Desktop\FYP\Data\Final\TEX-20.txt", "+w")
test_set = open(r"C:\Users\u180530\Desktop\FYP\Data\Final\TEX20.txt", "+w")

for line in file:
    count += 1    
    if(count%5==0):
       test_set.write(line)
       print("Writing to Test Set")
    else:
        file_object.write(line)
        print("Writing to regular set")