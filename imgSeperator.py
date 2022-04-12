from mtcnn.mtcnn import MTCNN
from matplotlib.patches import Rectangle
from matplotlib import pyplot
import os
import shutil

def face_detection(file):
    # load image from file
    pixels = pyplot.imread(file)
    # detect faces in the image
    faces = detector.detect_faces(pixels)
    return len(faces)

def make_newdir(dir):
    os.mkdir(dir + '\\noface')
    os.mkdir(dir + '\\more')

dir = '..\\twicetagram'
nofaceDir = dir + '\\noface'
moreDir = dir + '\\more'
cwd = os.getcwd()

# create the detector, using default weights
detector = MTCNN()
counter = 1
for filename in os.listdir(dir):
    f = os.path.join(dir, filename)
    if os.path.isfile(f) and face_detection(f) > 1:
        shutil.move(f, cwd + moredir)
        print(f'{counter}. Image {filename} has been moved successfully')
        # print(f'Image {f} has been moved successfully to {cwd + newdir}')
        counter += 1
    elif os.path.isfile(f) and face_detection(f) == 1:
        shutil.move(f, cwd + onedir)
        print(f'{counter}. Image {filename} has been moved successfully')
        # print(f'Image {f} has been moved successfully to {cwd + newdir}')
        counter += 1