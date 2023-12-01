from PIL import Image
import numpy as np

image = Image.open("_.png")

image_array = np.array(image)
image_block_index = [[0 for j in range(image.width)] for i in range(image.height)]

blocks = [
    [127,178,56,"slime"],
    [247,233,163,"sand"],
    [255,0,0,"redstone_block"],
    [160,160,255,"ice"],
    [167,167,167,"iron_block"],
    [0,124,0,"leaves"]
]

for i in range(image.height):
    for j in range(image.width):
        sum = 0
        min_sum = 65535
        min_index = 0
        for k in  range(6):
            sum = sum + np.power(np.abs(image_array[i][j][0] - blocks[k][0]),2)
            sum = sum + np.power(np.abs(image_array[i][j][1] - blocks[k][1]),2)
            sum = sum + np.power(np.abs(image_array[i][j][2] - blocks[k][2]),2)
            sum = np.sqrt(sum)
            if(sum < min_sum):
                min_sum = sum
                min_index = k
        
        image_block_index[i][j] = min_index


        
        
with open("a.mcfunction","w") as file:
    for i in range(image.height):
        for j in range(image.width):
            file.write("fill ~{0}~~{1} ~{0}~~{1} {2} \n".format(i,j,blocks[image_block_index[i][j]][3]))   

