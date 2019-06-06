"""
Created on Wed Mar 20 13:52:07 2019

@author: u180530

Script to Parse out Half sets.
"""
count = 0

file = open(r"C:\Users\u180530\Desktop\FYP\Data\NoNews\Pass3\RemovedNews3TIJ.txt", encoding = 'ansi')
file_object = open(r"C:\Users\u180530\Desktop\FYP\Data\Final\MEX2.txt", "+w")
for line in file:
    count += 1
    
    if(count%2==0):
       file_object.write(line)
    else:
        print(count)