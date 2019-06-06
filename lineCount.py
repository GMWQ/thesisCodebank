count = 0

file = open(r"C:\Users\u180530\Desktop\FYP\Data\Final\MEX-20.txt", encoding = 'ansi')
    
for line in file:
    count += 1
    print("Counting Line ", count)

print("Complete")  