import os

import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
  os.makedirs(DATA_DIR)

number_of_classes = 3
data_size = 100

cap = cv2.VideoCapture(2)

for i in range(number_of_classes):
  if not os.path.exists(os.path.join(DATA_DIR, str(i))):
    os.makedirs(os.path.join(DATA_DIR, str(i)))

  print("Collecting data for class {}".format(i))

  done = True
  while True:
    ret, frame = cap.read()