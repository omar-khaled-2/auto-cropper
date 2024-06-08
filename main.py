import os
from PIL import Image, ImageOps
import numpy as np
import datetime
from tqdm import tqdm


directory_path = input("Enter the directory path: ")


if os.path.isdir(directory_path):

    files = os.listdir(directory_path)



    script_directory = os.path.dirname(__file__)

    new_folder_path = os.path.join(script_directory, "output_" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    progress_bar = tqdm(total=len(files), desc="Cropping images", unit="file")

    os.makedirs(new_folder_path)
    for file in files:
        img = Image.open(os.path.join(directory_path, file))
        img = ImageOps.exif_transpose(img)
      
        img_array = np.array(img)
        width, height = img.size


        
        x1 = width - 1
        x2 = 0
        y1 = height - 1
        y2 = 0
        for y in range(height):
            for x in range(width):
                pixel_value = img_array[y, x]
                for i in range(4):
                    if(pixel_value[i] != 255):
                        x1 = min(x1, x)
                        x2 = max(x2, x)
                        y1 = min(y1, y)
                        y2 = max(y2, y)
                    break
                        
  

        cropped_img = img.crop((x1, y1, x2, y2))

        cropped_img.save(os.path.join(new_folder_path, file),format="PNG")
        progress_bar.update(1)
else:
    print("Invalid directory path. Please enter a valid directory.")