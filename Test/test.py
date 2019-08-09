import os
dir_path = os.path.dirname(os.path.realpath(__file__))
print(os.getcwd())
print(dir_path)
dir_path = os.path.dirname(dir_path)
print(dir_path)
