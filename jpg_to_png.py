import sys
import os
from PIL import Image

#grab first and second arguement
file_name = sys.argv[1]
new_file_name = sys.argv[2]

#check if new exists, if not create
cwd = os.getcwd()
file_exists = os.path.exists('cwd/new_file_name')
if file_exists == False:
    os.mkdir('cwd')
print(os.path.exists('cwd/new_file_name'))
#loop through Pokedex

#convert images to png

#save to the new folder
