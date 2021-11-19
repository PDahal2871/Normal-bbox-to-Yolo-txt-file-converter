import cv2, os, shutil

"""
-->  This function takes each line of txt file 
-- > returns actual bbox and class from that line. (Converted from Yolo format to OpenCV format)
--> cls is the integer form of yolo class, bbox is (x1,y1,x2,y2) where (x1,y1) represents top left position of image and (x2,y2) represents bottom right position.
"""

def convert_to_normal(dt,dh,dw):

    # Split string to float
    cls = int(dt.split(' ')[0])
    x = float(dt.split(' ')[1])
    y = float(dt.split(' ')[2])
    w = float(dt.split(' ')[3])
    h = float(dt.split(' ')[4])

    l = int((x - w / 2) * dw)
    r = int((x + w / 2) * dw)
    t = int((y - h / 2) * dh)
    b = int((y + h / 2) * dh)

    if l < 0:
        l = 0
    if r > dw - 1:
        r = dw - 1
    if t < 0:
        t = 0
    if b > dh - 1:
        b = dh - 1


    return cls, (l,t,r,b)


im = cv2.imread(os.path.join('test.png'))
dh, dw, _ = im.shape

with open(os.path.join('test.txt'),'r') as f:
    for lines in f.readlines():
        cls, bbox = convert_to_normal(lines, dh,dw)
        print('class index -->', cls)
        print('Bounding box -->',bbox)
#         img_crop = im[bbox[1]:bbox[3], bbox[0]:bbox[2]]

