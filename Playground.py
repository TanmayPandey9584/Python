#python f string magic
'''
var:str='python'
print(f'{ var:-^20}')
print(f'{ var:-<20}')
print(f'{ var:->20}')'''
'''     
def miniMaxSum(arr):
    # Write your code here
    arr = sorted(arr)
    print(sum(arr[:-1]),sum(arr[1:]))

if __name__ == '__main__': 

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
'''
'''
l = print([i for i in range(10) if i%3==0]) # noqa: E741
#print(l)
'''
'''
dic={i:f"item {i}" for i in range(20)}

dic={value:key for key,value in dic.items()}
print(dic)
'''
'''
def fun():
    a=44
    global b
    b=6.28
    print(locals())
    print(globals())
a=20
b=55
s='abc'
print(locals())
print(globals())
'''
'''
n = int(input())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
print(arr)
'''
'''
print(10/3)
'''
'''
cap = cv2.VideoCapture(0)
success, img = cap.read()
imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
'''
'''
first=input()
last=input()
print(f"Hello {first, last}")
'''
'''
def f(x):
  d=0
  while x > 1:
    (x,d) = (x/2,d+1)
  return(d)
x=f(27182818)
print(x)
'''
'''
def h(n):
    s = 0
    for i in range(2,n):
        if n%i == 0:
           s = s+i
    return(s)
x=h(60)-h(45)
print(x)
'''
'''
def g(m,n):
    res = 0
    while m >= n:
        (res,m) = (res+1,m/n)
    return(res)
x= g(375,4)
print(x)
'''
'''
def mys(m):
    if m == 1:
        return(1)
    else:
        return(m*mys(m-1))
    
x=mys(5)
print(x)
'''
'''
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
'''
'''

def findEncodings(images):
    encode_list = []
    for img in images:
        if isinstance(img, str):
            try:
                img = cv2.imread(img)

            except Exception as e:
                print(f"Error loading image: {img}, {e}")
                continue

        if isinstance(img, np.ndarray):
            try:
                face_locations = face_recognition.face_locations(img)
                if face_locations:
                    print(f"Found {len(face_locations)} faces in {img}")
                    encode = face_recognition.face_encodings(img)[0]  # Get first face
                    encode_list.append(encode)
                else:
                    print(f"Warning: No face found in image: {img}")
            except Exception as e:
                print(f"Error processing image: {img}, {e}")

    return encode_list
'''
'''
def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = ['Tanmay']
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')

encodeListKnown = findEncodings(images)
print('Encoding Complete')

'''
'''
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    if facesCurFrame:
        try:
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
            matches = face_recognition.compare_faces(encodeListKnown, facesCurFrame)
            faceDis = face_recognition.face_distance(encodeListKnown, facesCurFrame)
            matchIndex = np.argmin(faceDis)
        except Exception as e:
            print(f"Error during face encoding: {e}")
        continue  # Skip to next frame

    else:
        print("No faces detected in the frame.")
        continue  # Skip to next frame if no faces
'''
'''
    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)
'''
'''
class car:
    color = "black"
    @staticmethod
    def start():
        print( "{car} started...")
    @staticmethod
    def stop():
        return "{car} stopped..."

class toyotacar (car):
    def __init__(self,name):
        self.name=name

car1=toyotacar("fortuner")
car2=toyotacar("name")

print(car1.start())
print(car1.stop())

print(car2.start())
print(car2.stop())

print(car2.color)
'''
'''
import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text="Hello, tkinter!")
label.pack()
root.mainloop()
'''
'''
input_strings = ["flower", "flow", "flight"]
prefix=input_strings[0]
print(input_strings.find(prefix))
'''
#import sys
#sys.setrecursionlimit(100)
'''
def binary_search(n):
    if n==0 or n==1:
        return True


    high=n
    low=0
    while low<=high:
        mid=low+(high-low)//2

        if n==mid*mid:
            return True
        elif n<mid*mid:
            high=mid-1
        else:
            low=mid+1

n = int(input(""))
print(binary_search(n))
'''
'''
from math import sqrt
n=int(input())
a=sqrt(n)
if float(n)==a*a:
    print(sqrt(n))
    print((a*a))
    print(True)
else:
    print(sqrt(n))
    print(int(a*a))
    print(False)
'''
'''
def is_perfect_square(num):
    # Edge case for negative numbers
    if num < 0:
        return False

    # Base cases for 0 and 1
    if num == 0 or num == 1:
        return True

    # Binary search within the range [1, num]
    left, right = 1, num
    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid

        if square == num:
            return True
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1

    return False


# Test cases

if is_perfect_square(16):
    print(True)
'''
'''
n=int(input(""))
i=1
while i<=n//2:
    if i*i==n:
        print(True)
        break
    i+=1
else:
    print(False)
'''
'''
a=1,2,3,4,5
print(a)
'''
'''
from typing import List


class RemoveDuplicatesFromSortedArray:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Length of the update array
        count = 0
        # Loop for all the elements in the array
        for i in range(len(nums)):
            # If the current element is equal to the next element, we skip
            if i < len(nums) - 2 and nums[i] == nums[i + 1]:
                continue
            # We will update the array in place
            nums[count] = nums[i]
            count += 1
        return count


if __name__ == '__main__':
    r = RemoveDuplicatesFromSortedArray()
    print(r.removeDuplicates([1, 1, 2]))
    print(r.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

'''
# Nth Sorted Element
'''
def nele(nums):
    for i in range(0,len(nums)-1):
        print(nums)
        j=i+1
        print(f"num[i] is {nums[i]} and nums[j] is {nums[j]}")
        if nums[i]>nums[j]:
            nums[i], nums[j] = nums[j], nums[j]
            print(f"num[i] is {nums[i]} and nums[j] is {nums[j]}")


        #print(nums)
        for j in range(i+1,len(nums)):
            #print(f"num[i] is {nums[i]} and nums[j] is {nums[j]}")
            if nums[i]>nums[j]:
                nums[i], nums[j] = nums[j], nums[i]


    if n>len(nums):
        raise IndexError
    return nums[n]

'''
'''
nums=[1,3,4,2,5]
print(nele(nums))
f=[-1,-2,-3]
print(nele(f))
print(1,2)
'''
'''
def large(nums):
    max=nums[0]
    sec=nums[1]
    third=nums[2]
    print(max,sec,third)
    for i in range(len(nums)):
        print("all three inside loop",max,sec,third)
        if nums[i]>max:
            max=nums[i]
            print("max is",max)
        elif nums[i]>sec:
            third=sec
            sec=nums[i]
            print("sec is",sec)
        elif nums[i]>third:
            third=nums[i]
            print("third is",third)

    print(max,sec,third)

large([1,
2,9,50,20,30])
'''

"""
def sum(a,c):
    num=[]
    for i in range(a):
        num.append(c)
    print(num)

a=int(input("enter range "))
b=int(input("enter elements"))
sum(a,b)
"""
print(2//2)
