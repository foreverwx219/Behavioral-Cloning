# **Behavioral Cloning** 

## Writeup Template

### You can use this file as a template for your writeup if you want to submit it as a markdown file, but feel free to use some other method and submit a pdf if you prefer.

---

**Behavioral Cloning Project**

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road
* Summarize the results with a written report


[//]: # (Image References)

[image1]: ./examples/placeholder.png "Model Visualization"
[image2]: ./examples/placeholder.png "Grayscaling"
[image3]: ./examples/placeholder_small.png "Recovery Image"
[image4]: ./examples/placeholder_small.png "Recovery Image"
[image5]: ./examples/placeholder_small.png "Recovery Image"
[image6]: ./examples/placeholder_small.png "Normal Image"
[image7]: ./examples/placeholder_small.png "Flipped Image"

## Rubric Points
### Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/432/view) individually and describe how I addressed each point in my implementation.  

---
### Files Submitted & Code Quality

#### 1. Submission includes all required files and can be used to run the simulator in autonomous mode

My project includes the following files:
* model.py containing the script to create and train the model
* drive.py for driving the car in autonomous mode
* model.h5 containing a trained convolution neural network 
* writeup_report.md or writeup_report.pdf summarizing the results

#### 2. Submission includes functional code
Using the Udacity provided simulator and my drive.py file, the car can be driven autonomously around the track by executing 
```sh
python drive.py model.h5
```

#### 3. Submission code is usable and readable

The model.py file contains the code for training and saving the convolution neural network. The file shows the pipeline I used for training and validating the model, and it contains comments to explain how the code works.

### Model Architecture and Training Strategy

#### 1. An appropriate model architecture has been employed

My model is CNNs(model.py lines 18-38). After some preprocess, the images are put into the model to be trained. The model includes 5 Convolution layers(model.py lines 53&55-58), 2 Dropout layers(model.py lines 54&39), 1 Flatten layer(model.py line 60) and 4 Dense layers(model.py lines 61-64).

#### 2. Attempts to reduce overfitting in the model

The model contains 2 dropout layers in order to reduce overfitting after convolution layers(model.py lines 54&59). 

The model was trained and validated on different data sets to ensure that the model was not overfitting. The model was tested by running it through the simulator and ensuring that the vehicle could stay on the track.

#### 3. Model parameter tuning

The model used an adam optimizer, so the learning rate was not set manually (model.py line 66).

#### 4. Appropriate training data

Training data was chosen to keep the vehicle driving on the road. I tried to use camera images collected by myself, but the result is not good. So I used the data supported by this project. Then horizontally fliped images and its negative steering angles are used to increase training data and get sufficient right turn images.

For details about how I created the training data, see the next section. 

### Model Architecture and Training Strategy

#### 1. Solution Design Approach

My first step was to create model according to what I showed above. To deal with overfitting, I added 2 dropout layers. And I added lambda layers to provide suitable image size.  

Then, as initial layers have general features, the model has to learn the edges of lane. This model stoped improving validation loss after 8 epoch. The value of validation loss was 0.0101. 

The final step was to run the simulator to see how well the car was driving around track one. It works well. 

At the end of the process, the vehicle is able to drive autonomously around the track without leaving the road.

#### 2. Final Model Architecture

Here is a visualization of the architecture (note: visualizing the architecture is optional according to the project rubric)

![model architecture][https://viewhjeftibwrx.cn1-udacity-student-workspaces.com/files/home/workspace/CarND-Behavioral-Cloning-P3/netModel.png]

#### 3. Creation of the Training Set & Training Process

To capture good driving behavior, I first recorded two laps on track one using center lane driving. Here is an example image of center lane driving:
![center image][https://viewhjeftibwrx.cn1-udacity-student-workspaces.com/files/home/workspace/CarND-Behavioral-Cloning-P3/data/IMG/center_2016_12_01_13_30_48_287.jpg]

I then recorded the vehicle recovering from the left side and right sides of the road back to center so that the vehicle would learn to recover if deviated from center of lane. 
The example images to recover from left:
![left1][https://viewhjeftibwrx.cn1-udacity-student-workspaces.com/files/home/workspace/CarND-Behavioral-Cloning-P3/pic_writeup/left_center_1.jpg]
![left2][https://viewhjeftibwrx.cn1-udacity-student-workspaces.com/files/home/workspace/CarND-Behavioral-Cloning-P3/pic_writeup/left_center_2.jpg]
The example images to recover from right:
![right1][https://viewhjeftibwrx.cn1-udacity-student-workspaces.com/files/home/workspace/CarND-Behavioral-Cloning-P3/pic_writeup/right_center_1.jpg]
![right2][https://viewhjeftibwrx.cn1-udacity-student-workspaces.com/files/home/workspace/CarND-Behavioral-Cloning-P3/pic_writeup/right_center_2.jpg]

To augment the data set, I flipped images and took negative of steering angle measurnment for flipped images(model.py lines 26-30).Here is an exmple: 
![origin][https://viewhjeftibwrx.cn1-udacity-student-workspaces.com/files/home/workspace/CarND-Behavioral-Cloning-P3/pic_writeup/origin.jpg]
![flip][https://viewhjeftibwrx.cn1-udacity-student-workspaces.com/files/home/workspace/CarND-Behavioral-Cloning-P3/pic_writeup/flip.jpg]

I used this training data for training the model. The validation set helped determine if the model was over or under fitting. The ideal number of epochs was 8 as evidenced by the validation loss stopped decreasing after 8 epoch. I used an adam optimizer so that manually training the learning rate wasn't necessary.
