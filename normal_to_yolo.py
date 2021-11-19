import os, shutil
from PIL import Image

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


def new_bbox(img_path,bbox):
    im=Image.open(img_path)
    w= int(im.size[0])
    h= int(im.size[1])

    xmin, ymin, xmax, ymax = bbox[0],bbox[1],bbox[2],bbox[3]
    b = (xmin, xmax, ymin, ymax)
    bb = convert((w,h), b)
    return bb
    
#bbox should be in the order of (x1,y1,x2,y2) or (xmin, ymin, xmax, ymax)

new_bb = new_bbox(os.path.join('img','test.png'), bbox)

with open('test.txt','w') as file:
    file.write('0' + ' ' + str(new_bb[0]) + ' ' + str(new_bb[1]) + ' ' + str(new_bb[2]) + ' ' + str(new_bb[3]) +'\n')
