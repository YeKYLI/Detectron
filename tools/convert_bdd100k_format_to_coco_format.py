##https://github.com/touchsunshine/convert_bdd100k_to_coco_format/blob/master/convert_to_coco_format.py
##copy from above and i modify something
import os
import json
import cv2

input_file = "/home/data4t/huaijian/data/bdd100k/labels/bdd100k_labels_images_val.json"
input_image_dir = "/home/data4t/huaijian/data/bdd100k/images/100k/val/"
output_file = "/home/data4t/huaijian/data/bdd100k/coco_format_label/bdd100k_train.json"
category_names = ["bike","bus", "car", "motor", "person", "rider", "traffic light", "traffic sign", "train", "truck"]
filenames = []

def coco_categories():
    categorieslist = []
    for i in range(len(category_names)):
        per_category_dict = {}
        per_category_dict['supercategory'] = 'none'
        per_category_dict['id'] = i + 1
        per_category_dict['name'] = category_names[i]
        categorieslist.append(per_category_dict)
    return categorieslist

def coco_images():
    imagelist = []
    global filenames
    test = 1
    for i in range(len(input_json)):
        test += 1
        if test > 3:
            break
        per_anno = input_json[i]
        filename = per_anno['name']
        filenames.append(filename)
    filenames = list(set(filenames))
    for index in range(len(filenames)):
        per_image = dict()       
        filename = filenames[index]
        image = input_image_dir + filename
        print image
        image = cv2.imread(image)
        height, width, _ = image.shape
        per_image['height'] = height
        per_image['width'] = width
        per_image['id'] = index
        per_image['file_name'] = filename
        imagelist.append(per_image)
        cv2.imshow("img", image)
        cv2.waitKey(0)
    return imagelist

def coco_annotations():
    count = 0
    global filenames
    annotationlist = []
    test = 1
    for i in range(len(input_json)):
        test += 1
        if test > 3:
            break
        anno = input_json[i]
        filename = anno['name']
        print filename
        for label in anno['labels']:
            if 'box2d' not in label:
                continue
            per_anno = dict()
            bbox = label['box2d']
            if bbox['x1'] >= bbox['x2'] or bbox['y1'] > bbox['y2']:
                continue
            category = label['category']
            box = [bbox['x1'], bbox['y1'], bbox['x2'] - bbox['x1'], bbox['y2'] - bbox['y1']]
            per_anno['image_id'] = filenames.index(filename)
            per_anno['bbox'] = box
            per_anno['category_id'] = category_names.index(category) + 1
            per_anno['segmentation'] = [[0, 0]]
            per_anno['area'] = 1
            per_anno['id'] = count
            per_anno['iscrowd'] = 0
            count += 1
            annotationlist.append(per_anno)
    return annotationlist

# to do
input_json = json.load(open(input_file))
output_info = dict()
output_info['categories'] = coco_categories()
output_info['images'] = coco_images()
print output_info['categories']
output_info['images'] = coco_images()
print output_info['images']
output_info['annotation'] = coco_annotations()
print output_info['annotation']

with open(output_file, "w") as writer:
    json.dump(output_info, writer)

