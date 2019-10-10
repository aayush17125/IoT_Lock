'''Made by:
Devishi Kesar(2015024)
Hemant Rattey(2015040)'''

import time
start_time = time.time()
metadata=["ID","Status","Price"]
with open('testFile.txt', 'r') as f:
        puzzle = [list(line.split()) for line in f]

for i in range(0,len(puzzle)):
    for j in range (0,len(puzzle[i])):
        print(str(puzzle[i][j] + " "),end="")
    print()

print("--- %s seconds ---" % (time.time() - start_time))
find=input("Enter data to sum: ")
sum=0
if find in metadata:
    j=metadata.index(find)
    if j==0 :
        for i in range(0,len(puzzle)):
            sum+=int(puzzle[i][j])
        print(sum)
    elif j==2:
        for i in range(0,len(puzzle)):
            sum+=float(puzzle[i][j])
        print(sum)
    else:
        print("Cannot sum")
else:
    print("Not found")

