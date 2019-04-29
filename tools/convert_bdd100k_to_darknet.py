#to do
import json
json_file = "/home/data4t/huaijian/data/bdd100k/labels/bdd100k_labels_images_train.json"
output_dir = "/home/data4t/huaijian/data/bdd100k/darknet_label/bdd100k_train"
 
__categories__ = ["bike","bus","car","motor","person","rider","traffic light","traffic sign","train","truck"]
frames = json.load(open(json_file, "r"))

test = 0
for frame in frames:
    test += 1
    print "processing ... " + str(test) + " image"
    print frame['name']
    output_file = open(output_dir + "/" + str(frame['name']).strip(".jpg") + ".txt", "w")
    for label in frame['labels']:
        if 'box2d' not in label:
            continue
        xy = label['box2d']
        if xy['x1'] >= xy['x2'] or xy['y1'] > xy['y2']:
            continue
        category = label['category']
        x1 = int(xy['x1'])
        y1 = int(xy['y1'])
        x2 = int(xy['x2'])
        y2 = int(xy['y2'])
        print str(__categories__.index(category)) + " " + str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2) + "\n"
        output_file.write(str(__categories__.index(category)) + " " + str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2) + "\n")
    output_file.close()


    
#print frames
