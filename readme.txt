# Semantic-Segmentation
Perform Semantic Segmentation on a Batch of Images.

Before performing this experiment, we need to know what Image Segmentation actually is.

	Every image is made up of a group of pixel values. Image Segmentation is the task of classifying an image at the pixel level. 
	A machine is able to analyse an image more effectively by dividing it into different segments according to the classes assigned to each of the pixel values present in the image.


There are two major types of Image Segmentation:
Semantic Segmentation: Objects classified with the same pixel values are segmented with the same colormaps.

Instance Segmentation: It differs from semantic segmentation because different instances of the same object are segmented with different color maps.

So, in this assignment, we have to do Semantic Segmentation. We can ignore the Instance Segmentation part.

Our requirements for the experiment:
Before performing this experiment, we need to download certain libraries and packages to implement our code successfully.
tensorflow-gpu
opencv-python
scikit-image
pillow
pixellib

Install PixelLib and its dependencies:
Pixellib is a library for performing segmentation of objects in images and videos. It supports the two major types of image segmentation:

1.Semantic segmentation

2.Instance segmentation

PixelLib supports two deep learning libraries for image segmentation which are Pytorch and Tensorflow.

Install the latest version tensorflow(tensorflow 2.0) with: pip3 install tensorflow

Install opencv-python with: pip3 install opencv-python

Install scikit-image with: pip3 install scikit-image

Install Pillow with: pip3 install pillow

Install Pixellib: pip3 install pixellib

