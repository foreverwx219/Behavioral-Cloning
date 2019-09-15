import os
import csv
import cv2
import numpy as np
import sklearn
from sklearn.utils import shuffle
import matplotlib.image as mpimg
#from keras.utils.vis_utils import plot_model

#angle_correct = 0.20
      
samples = []
with open('data/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for line in reader:
        samples.append(line)

images = []
angles = []
for sample in samples:
    center_angle = float(sample[3])
    for i in range(1):
        name = 'data/IMG/'+sample[i].split('/')[-1]
        img = cv2.imread(name)         
        images.append(img)
        images.append(cv2.flip(img, 1))
        
        angles.append(center_angle)
        angles.append(center_angle* -1)                                     
        '''            
        if(i == 0):                        
            angles.append(center_angle)
            angles.append(center_angle* -1)
        if(i == 1):
            angles.append(center_angle + angle_correct)
            angles.append((center_angle + angle_correct)* -1)                     
        if(i == 2):
            angles.append(center_angle - angle_correct)
            angles.append((center_angle - angle_correct)* -1)
        '''                
X_train = np.array(images)
y_train = np.array(angles)

from keras.models import Sequential, Model
from keras.layers import Flatten, Dense, Lambda, Cropping2D, Lambda, Convolution2D, Dropout, MaxPooling2D

model = Sequential()
model.add(Lambda(lambda x: x / 255.0 - 0.5, input_shape=(160, 320, 3)))
model.add(Cropping2D(cropping=((70, 25), (0, 0))))

# End to End Learning Model for Self-Driving Cars
model.add(Convolution2D(24, (5, 5), subsample=(2, 2), activation="relu"))
model.add(Dropout(0.7))
model.add(Convolution2D(36, (5, 5), subsample=(2, 2), activation="relu"))
model.add(Convolution2D(48, (5, 5), subsample=(2, 2), activation="relu"))
model.add(Convolution2D(64, (3, 3), activation="relu"))
model.add(Convolution2D(64, (3, 3), activation="relu"))
model.add(Dropout(0.8))
model.add(Flatten())
model.add(Dense(100))
model.add(Dense(50))
model.add(Dense(10))
model.add(Dense(1))
          
model.compile(loss = 'mse', optimizer = 'adam')
history_object = model.fit(X_train, y_train, batch_size=32, nb_epoch=10, shuffle=True, verbose=1, validation_split = 0.2)       
model.save('model.h5')