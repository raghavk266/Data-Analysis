import os
file = open('./os/reader.txt',mode='r')
# file_contents = file.read()
# print(file_contents) 
with open('./os/reader.txt','r') as f:
    # file_contents = f.read()
    # print(file_contents)
    f_lines = f.readlines()
    print(f_lines[0].strip().split(','))