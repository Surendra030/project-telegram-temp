import os
import cv2



def dreamsketch(path):  
    original_img = cv2.imread(path)
    gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    gray_inverse = 255 - gray_img
    blurred_img = cv2.GaussianBlur(gray_inverse, (21, 21), sigmaX=100, sigmaY=100)
    output = cv2.divide(gray_img, blurred_img, scale=230.0)
    return output


def normalsketch(input_path, output_path, scale=10):
    if scale > 10 or scale < 1:
        raise ValueError('Errno 1: Scale must be between 1 and 10')
    if not isinstance(scale, int):
        raise TypeError('Errno 2: Scale must be an integer value')
    if not isinstance(input_path, str) or not isinstance(output_path, str):
        raise TypeError('Errno 3: Path to image must be a string')
    
    original_img = cv2.imread(input_path)
    if original_img is None:
        raise FileNotFoundError(f'Errno 4: Image not found at {input_path}')
    
    gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    gray_inverse = 255 - gray_img
    sigma = scale * 1.5
    blurred_img = cv2.GaussianBlur(gray_inverse, (51, 51), sigmaX=sigma, sigmaY=sigma)
    blurred_inverse = 255 - blurred_img
    output = cv2.divide(gray_img, blurred_inverse, scale=256.0)
    
    cv2.imwrite(output_path, output)



def fetch_sketch(inpu_img_path,output_img_path):
        
    # output = dreamsketch(inpu_img_path)
    # cv2.imwrite(output_img_path,output)
    normalsketch(inpu_img_path,output_img_path)
    if os.path.exists(output_img_path):
        return True 


