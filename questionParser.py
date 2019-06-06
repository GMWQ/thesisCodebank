# Question Parsing

import re

data = []
count = 0

file = open(r"C:\Users\u180530\Desktop\FYP\Data\NoNews\RemovedNews3ELP.txt", "w+")

with open(r"C:\Users\u180530\Desktop\FYP\Data\NoNews\RemovedNews2ELP.txt") as data_file:
    
    for line in data_file:
        print(line)
        if re.findall(r'Breaking News', line):
            print("Removing Line: ")
            count += 1
        else:
                print("Writing Line")
                print(line)
                file.write(line)

print("Removed " + str(count) + " lines")
print("Complete")