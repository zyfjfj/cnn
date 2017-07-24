#-*- coding: UTF-8 -*-
import os
import keras
import numpy as np
from PIL import Image
model = keras.models.load_model('all_sgd_try11.h5')
count=0
for filename in os.listdir(r"preimage"):
    imgdir = 'preimage/'+str(filename)
    temp = Image.open(imgdir)
    temp = temp.resize((150, 150))
    temp = np.array(temp)
    temp = temp/255
    classes=model.predict(temp[None, :, :, :])
    if classes>=0.5:
        print(filename,classes)
        count += 1
print(count)