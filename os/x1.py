import os
print(os.getcwd())
print(os.listdir('.'))
print(os.listdir('..'))
os.makedirs('./data',exist_ok=True)
