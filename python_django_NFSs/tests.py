from django.test import TestCase
import os

# Create your tests here.
dir_path = "/home/mz/Documents/vimrc/"
files = os.listdir(dir_path)
print(os.getcwd())
for i in files:
    if os.path.isdir(dir_path + i):
        print(f"{i} is dir.")
    else:
        print(f"{i} is file.")
