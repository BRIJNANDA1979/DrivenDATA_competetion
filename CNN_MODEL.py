# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 05:29:46 2023

@author: BRIJB
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May 13 03:02:04 2021

@author: BRIJB
"""
Train_data_categorised_path ='C:\\Users\BRIJB\\Desktop\\2023 BRIJ ML\\DATAdriven First project\Train_For_CNN'
Train_features_path = 'C:\\Users\\BRIJB\\Desktop\\2023 BRIJ ML\\DATAdriven First project\\train_features'
import os
import pandas as pd
import glob
import shutil             ###### make a folder for first category 'antelope_duiker'


def label_train_images(category_name,path):
  list_image = []
  df = pd.read_csv(path)
  df1 = df[df[category_name] == 1]
  list_image = df1['id'].tolist()
  return list_image

def Populate_images_category_folder(category_name,path,list_of_files_to_copy):
  for x in glob.glob(path + '/' + str('*.*')):
     for item in list_of_files_to_copy:
      if x.find(item) != -1:
        shutil.copyfile(x, Train_data_categorised_path + '/'+category_name+'/'+item + str('.jpg'))


train_labels_path ='C:\\Users\BRIJB\\Desktop\\2023 BRIJ ML\\DATAdriven First project\\train_labels.csv'
df = pd.read_csv(train_labels_path)
category = df.columns.tolist()
print(category)
del category[0]           ########## remove first element  that is 'id'
print(category)
list_out = []

for cat in category:
  list_out.append(label_train_images(cat,train_labels_path))
#zipped_list = list(zip(category,list_out))

####################3  to make 8 folders of 8 categories    $$$$$$$$$$$$$$$$$$
for cat in category:
  directory = Train_data_categorised_path + '/' + cat #https://stackoverflow.com/questions/273192/how-do-i-create-a-directory-and-any-missing-parent-directories
  if not os.path.exists(directory):
    os.makedirs(directory)
    
for cat in category:
  list_of_category_images =label_train_images(cat,train_labels_path)
  Populate_images_category_folder(cat,Train_features_path,list_of_category_images)
