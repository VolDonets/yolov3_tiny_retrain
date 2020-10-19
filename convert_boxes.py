import glob
import os
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import shutil


box_file_path = "boxes_h.txt"
train_labels_dir_path = "train_labels"
test_labels_dir_path = "test_labels"
train_images_dir_path = "train_images"

image_indexes = [int(image_name.split('.')[0]) for image_name in os.listdir(train_images_dir_path)]

np.random.shuffle(image_indexes)
f = open(box_file_path, "r")
box_content = f.read()
box_dict = eval("{" + box_content + "}")
f.close()

if not os.path.exists(test_labels_dir_path):
    os.mkdir(test_labels_dir_path)

if not os.path.exists(train_labels_dir_path):
    os.mkdir(train_labels_dir_path)

IM_WIDTH = 640.0
IM_HEIGHT = 480.0

ff = open("aaa.txt", "w")

for inx in image_indexes:
    line_for_file = "/home/biba_bo/Documents/yolov3_tiny_train/darknet/whole_data_for_training/train_images/" + str(inx) + ".png\n"
    ff.write(line_for_file)

ff.close()
    #train_label_file = open(train_labels_dir_path + "/" + str(inx) + ".txt", "w")
    #test_label_file = open(test_labels_dir_path + "/" + str(inx) + ".txt", "w")
    #x = box_dict[inx][0]
    #y = box_dict[inx][1]
    #width = box_dict[inx][2] - x
    #height = box_dict[inx][3] - y
    #x_center = x + (width / 2)
    #y_center = y + (height / 2)
    #x_center_norm = float(x_center) / IM_WIDTH
    #y_center_norm = float(y_center) / IM_HEIGHT
    #width_norm = float(width) / IM_WIDTH
    #height_norm = float(height) / IM_HEIGHT
    #info_line = "0 " + str("{0:.6f}".format(x_center_norm)) \
    #            + " " + str("{0:.6f}".format(y_center_norm)) \
    #            + " " + str("{0:.6f}".format(width_norm)) \
    #            + " " + str("{0:.6f}".format(height_norm))
    #print(info_line)
    #train_label_file.write(info_line)
    #test_label_file.write(info_line)
    #train_label_file.close()
    #test_label_file.close()
