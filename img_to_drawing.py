import os
import cv2


def dreamsketch(path):  
    original_img = cv2.imread(path)
    gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    gray_inverse = 255 - gray_img
    blurred_img = cv2.GaussianBlur(gray_inverse, (21, 21), sigmaX=100, sigmaY=100)
    output = cv2.divide(gray_img, blurred_img, scale=256.0)
    return output



def fetch_sketch(inpu_img_path,output_img_path):
        
    output = dreamsketch(inpu_img_path)
    cv2.imwrite(output_img_path,output)
    if os.path.exists(output_img_path):
        return True 


