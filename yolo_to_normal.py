def convert_to_normal(dt)
#     dt is line of txt files
#     fl = open(label_path, 'r')
#     data = fl.readlines()
#     fl.close()

#     for dt in data:

    # Split string to float
    classes = int(dt.split(' ')[0])
    x = float(dt.split(' ')[1])
    y = float(dt.split(' ')[2])
    w = float(dt.split(' ')[3])
    h = float(dt.split(' ')[4])

    # Taken from https://github.com/pjreddie/darknet/blob/810d7f797bdb2f021dbe65d2524c2ff6b8ab5c8b/src/image.c#L283-L291
    # via https://stackoverflow.com/questions/44544471/how-to-get-the-coordinates-of-the-bounding-box-in-yolo-object-detection#comment102178409_44592380
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


    return (l,t,r,b)
