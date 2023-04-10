# JPG World File Resizer

## Do you have a set of JPG world files (.JGW files) you'd like to resize?

Say you have a georeferenced JPG in a lower resolution and another non-georeferenced JPG in a higher resolution which has the same geographic extent as the georeferenced JPG. Georeferencing the higher res JPG alone is simple enough as you can use a world file calculator. 

But having a set of JPGs complicates things and that's where this Python script comes in to automate the process. This Python script reads in a list of world files (JGW files) located in a local directory of your choosing and then outputs a new "resized" world file for each input file according to your desired image size.

For each input world file, the script reads in its parameters, which include pixel size in both x and y directions, coordinates of the upper left corner of the image in world coordinates, and the dimensions of the image in pixels. The script then calculates new world coordinates for the lower right corner of the image using the specified original image size.

Next, the script converts these new world coordinates to latitude and longitude using the desired output image size. The script then creates a new JGW file with the updated pixel size, the new lower left corner coordinates, and the latitude and longitude coordinates of the new upper left corner.

The new JGW file is then saved in the 'output/' directory with the same name as the original file, but with the added suffix '_hd.jgw'. The script repeats this process for all input JGW files.

In summary, this script resizes a set of JGW files to a new image size and updates the associated coordinates to ensure that the image is still georeferenced correctly.
