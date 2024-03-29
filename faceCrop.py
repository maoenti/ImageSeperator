from mtcnn.mtcnn import MTCNN
from matplotlib import pyplot
import os
import re

def make_newdir(dir):
    os.mkdir(dir + '\\crop')

def crop_face(filename, name):
    # load image from file
    pixels = pyplot.imread(filename)
    # detect faces in the image
    result_list = detector.detect_faces(pixels)
    # plot each face as a subplot
        # get coordinates
    if len(result_list) == 1:
        for i in range(len(result_list)):
            x1, y1, width, height = result_list[i]['box']
            x2, y2 = x1 + width, y1 + height
            # define subplot
            pyplot.subplot(1, len(result_list), i+1)
            pyplot.axis('off')
            # plot face
            pyplot.imshow(pixels[y1:y2, x1:x2])
        # show the plot
        pyplot.savefig(cropDir + '\\' + name, bbox_inches='tight', pad_inches = 0.)
        return True
    else:
        return False

def check_file_ext(file):
    match = re.search('\.png|jpeg|jpg$', file)
    if match:
        return True


dir = '..\\jeongyeonniee'
cropDir = dir + '\\crop'
try:
    make_newdir(dir)
except:
    print('Directory is already made.')

# create the detector, using default weights
detector = MTCNN()
croppedCounter = 0
globalCounter = 0

for filename in os.listdir(dir):
    if check_file_ext(filename) == True:
        f = os.path.join(dir, filename)
        if crop_face(f, filename) == True:
            croppedCounter += 1
        # print(f'{croppedCounter}. Image {f} has been cropped successfully')
        os.system('cls')
    else:
        pass
    globalCounter += 1
    percent = (globalCounter * 100) / len(os.listdir(dir))
    print('%0.2f%% of files checked' %(percent))
    print(f'{croppedCounter} images has been cropped')
    if croppedCounter > 1200:
        break
    