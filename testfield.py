import cv2
from matplotlib import image
import numpy as np
import face_recognition
import os
from datetime import datetime
from PIL import Image


path = "C:\\Users\Tanmay pandey\OneDrive\Pictures\Photo\My Photos"
images = []
classNames = []
myList = os.listdir(path)
#face_recognition.api.load_image_file(images, mode='RGB')
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images=(curImg)
    classNames.append(os.path.splitext(cl)[0])
    print(images)

'''
def findEncodings(images):
    encodeList = []
    for img in images:
        if isinstance(img, np.ndarray):
            encode = face_recognition.face_encodings(img)[0]

    if len(encode) > 0:
        encodeList.append(encode)
    else:
        print("Warning: No face encoding found in image")
    for encode in encode:
        encodeList.append(encode)
    
    return encodeList
'''

'''
def findEncodings(images, model="hog", num_jitters=1):
    encodeList = []
    for img_path in images:
        try:
            # Load image in RGB format
            img = face_recognition.load_image_file(img_path)
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Ensure RGB if using OpenCV

            # Detect faces (adjust parameters as needed)
            face_locations = face_recognition.face_locations(img_rgb, model=model, num_jitters=num_jitters)

            # Handle multiple faces (optional, modify as needed)
            encode = face_recognition.face_encodings(img_rgb, face_locations)

            if len(encode) > 0:
                encodeList.append(encode)
            else:
                print(f"Warning: No face encoding found in image: {img_path}")

        except Exception as e:
            print(f"Error processing image {img_path}: {e}")

    return encodeList
'''

'''
def findEncodings(loaded_images):
    encodeList = []
    for img in loaded_images:
        if isinstance(img, np.ndarray):
            encode = face_recognition.face_encodings(img)

            if len(encode) > 0:
                encodeList.append(encode)
            else:
                print("Warning: No face encoding found in image")

    return encodeList
'''

def findEncodings(images):
    encodeList = []
    for img_path in images:
        try:
            # Open image with Pillow
            img = Image.open(img_path)

            # Convert to NumPy array in RGB format
            img_array = np.array(img)

            # Ensure RGB format (Pillow might load as BGR in some cases)
            if img_array.shape[2] == 4:  # Alpha channel present
                img_array = img_array[:, :, :3]  # Remove alpha channel

            # Generate face encodings
            encode = face_recognition.face_encodings(img_array)

            if len(encode) > 0:
                encodeList.append(encode)
            else:
                print(f"Warning: No face encoding found in image: {img_path}")

        except Exception as e:
            print(f"Error processing image {img_path}: {e}")

    return encodeList