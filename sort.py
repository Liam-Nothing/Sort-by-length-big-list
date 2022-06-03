import os
import os.path
from os.path import isfile, join
from os import listdir

temp_path = "data_sort"
final_data = ""
sorted_list = "data_base_word_shorted.txt"
db_list = "data_base_word.txt"
count = 0

if not os.path.isdir(temp_path):
    os.mkdir(temp_path)

# Count number of lines
with open(db_list, 'r') as fp:
    for count, line in enumerate(fp):
        pass

# Sorting
with open(db_list) as file:
    for idx,line in enumerate(file):
        print("["+str(idx+1)+"/"+str(count)+"] " + line.rstrip() + " => " + str(len(line.rstrip())))
        f = open(temp_path+"/"+str("{:02d}".format(len(line.rstrip())))+".txt", "a")
        f.write(line)
        f.close()

# Merge data
ls_file = [f for f in listdir(temp_path) if isfile(join(temp_path, f))]

# Wirte data
for file in ls_file:
    with open(temp_path+"/"+file) as fp:
        final_data += fp.read()
f = open(sorted_list, "a")
f.write(final_data)
f.close()
