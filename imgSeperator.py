from mtcnn.mtcnn import MTCNN
from matplotlib import pyplot
import os
import shutil
import re

def face_detection(file):
    # load image from file
    pixels = pyplot.imread(file)
    # detect faces in the image
    faces = detector.detect_faces(pixels)
    return len(faces)

def make_newdir(dir):
    os.mkdir(dir + '\\noface')
    os.mkdir(dir + '\\more')

def check_file_ext(file):
    match = re.search('\.png|jpeg|jpg$', file)
    if match:
        return True

# Hyperparameters
dir = '..\\tzuyutwicee_'
nofaceDir = dir + '\\noface'
moreDir = dir + '\\more'
cwd = os.getcwd()
# make_newdir(dir)

# create the detector, using default weights
detector = MTCNN()
counter = 1
check = 0
for filename in os.listdir(dir):
    if check_file_ext(filename) == True:
        f = os.path.join(dir, filename)
        if os.path.isfile(f) and face_detection(f) == 1:     # If the image doesn't contain any face
            shutil.move(f, nofaceDir)
            check += 1
            # print(f'{len(os.listdir(dir)) - counter}. Image {filename} has been moved successfully')
        elif os.path.isfile(f) and face_detection(f) > 1:      # If the image contain more than one faces
            shutil.move(f, moreDir)
            # print(f'{len(os.listdir(dir)) - counter}. Image {filename} has been moved successfully')
        else:
            # print(f'{len(os.listdir(dir)) - counter} files left')
            counter += 1
    else:
        pass
    print(f'{1200 - check} files left')
    if check > 1200:
        break