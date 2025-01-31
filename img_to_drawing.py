from sketchify import sketch
import os
import cv2



def fetch_sketch(inpu_img_path,output_img_path):
        
    output = sketch.dreamsketch(inpu_img_path)
    cv2.imwrite(output_img_path,output)
    if os.path.exists(output_img_path):
        return True 
