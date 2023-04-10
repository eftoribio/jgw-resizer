import glob
import os
from pathlib import Path
from PIL import Image

folder_path = '.' # assumes JGWs are in the same folder as the .py script

# Get a list of all the files in the folder
file_list = os.listdir(folder_path)

# Create two variables to store the dimensions of the smallest and largest JPG images
smallest_dimensions = None
largest_dimensions = None

for filename in file_list:
    # Check if the file has a ".jpg" extension
    if filename.lower().endswith(".jpg"):
        # Open the image file
        with Image.open(os.path.join(folder_path, filename)) as img:
            # Get the dimensions of the image
            width, height = img.size
            # Check if this is the smallest or largest image we've seen so far
            if smallest_dimensions is None or width * height < smallest_dimensions[0] * smallest_dimensions[1]:
                smallest_dimensions = (width, height)
            if largest_dimensions is None or width * height > largest_dimensions[0] * largest_dimensions[1]:
                largest_dimensions = (width, height)

# Print the dimensions of the smallest and largest JPG images
print("Smaller JPG image dimensions:", smallest_dimensions)
print("Larger JPG image dimensions:", largest_dimensions)

suffix = input("Input suffix (with underscore) of larger JPGs")

# This script accepts a world file and desired image size as input and outputs a new world file

xsize_old = smallest_dimensions[0]
ysize_old = smallest_dimensions[1]

xsize_new = largest_dimensions[0]
ysize_new = largest_dimensions[1]

jgwFiles = glob.glob('*.jgw')
    
for index, worldfile in enumerate(jgwFiles):
    txt = Path(worldfile).read_text().splitlines()
    ppx = float(txt[0])
    ppy = float(txt[3])
    worldx = float(txt[4])
    worldy = float(txt[5])
    
    xmin = worldx - (ppx / 2)
    ymax = worldy - (ppy / 2)
    
    xmax = (worldx + (xsize_old * ppx)) - (ppx / 2)
    ymin = (worldy + (ysize_old * ppy)) - (ppy / 2)

    print(f'{xmin}, {ymin} : {xmax}, {ymax}\n')
    
    lat1 = ymin
    lon1 = xmin
    lat2 = ymax
    lon2 = xmax
    
    # now the script computes the world file parameters
    
    if (lon1 < lon2):
        t = +lon1
        lon1 = lon2
        lon2 = t

    ppx = (lon1 - lon2) / xsize_new

    if (lat1 > lat2):
        t = +lat1
        lat1 = lat2
        lat2 = t

    ppy = (lat1 - lat2) / ysize_new

    lon2 += (ppx / 2) # x center of pixel
    lat2 += (ppy / 2) # y center of pixel

    wf = str(ppx) + "\n" + "0.00000\n0.00000\n" + str(ppy) + "\n" + str(lon2) + "\n" + str(lat2)
    path = ''
    print(wf)
    print('\n')
    filename = os.path.basename(worldfile)
    
    print(filename)
    new_filename = filename[:-4] + suffix + '.jgw'
    newpath = r'/output' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    path = worldfile.replace(filename,'output/' + new_filename)
    
    text_file = open(path, 'w')
    text_file.write(wf)
    text_file.close()
    print(f'New JGW file saved to {path}\n')