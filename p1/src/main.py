import csv
from collections import defaultdict


with open("../in/tests/my_sample.txt") as t:
    in_text = t.read()

# f = open("a.txt", "a")    
# f.write(in_text)
s = ""
persian_words = []
i = 0
step = 1
with open("../in/ha.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    # print(readCSV)
    for row in readCSV:
        i = 0
        for each_data in row:
            if i%5 == 1:
                persian_words.append(each_data)
            i += 1
split_text = in_text.split()


visited = []
flag = True
i = 0
forms_counter = 0
parts_found = defaultdict(list) 
total_counter = 0

for j in range()
while (flag):
    total_counter += 1
    s += split_text[0][i]

    wc = 0
    for word in persian_words:
        wc += 1
    
        if s == word and s not in visited:
            visited.append(s)
            parts_found[forms_counter].append(s)
            print(parts_found[1])
            if i == (len(split_text[0])-1):
                # print("tahe jomle")
                # flag = False
                print(forms_counter)
                print(parts_found)
                for i in range(forms_counter-1):
                    if parts_found[forms_counter] == parts_found[i]:
                        flag = False
                # if parts_found[forms_counter] not in 
                forms_counter += 1
                s = ""
                i = 0
                break
            s = ""

        else:
            # print("miad to else")
            
            if i == (len(split_text[0])-1) and wc == len(persian_words):
                
                parts_found[forms_counter] = []
                s = ""
                i = -1
    if total_counter > 200 :
        flag = False


    i += 1

print(visited)
print(parts_found)
