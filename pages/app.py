import streamlit as st
import numpy
import cv2
import matplotlib.pyplot as plt
import scipy.misc
from scipy import ndimage

st.write("# Module: Image processing")
st.write("## Image Filtering 101")
st.write("""

Filtering is a neighborhood operation, in which the value of any given pixel in the output image is determined
 by applying some algorithm to the values of the pixels in the neighborhood of the corresponding input pixel.

_http://www.ece.northwestern.edu/local-apps/matlabhelp/toolbox/images/linfilt3.html_

For this implementation exrecise, the goal is to apply and compare different image filtering algorithms, 
`linear and non-linear`, on the default input images shown below.

""")
img_or = ['images/175032.jpg', 'images/189080.jpg', 'images/295087.jpg', 'images/3096.jpg', 'images/42049.jpg']


with st.expander("View default input images"):
  col1, col2, col3 = st.columns(3)
  with col1:
    st.image(img_or[0], caption='Image view 1')
  with col2:
    st.image(img_or[1], caption="Image plan view")
  with col3:
    st.image(img_or[2], caption="Image vird view")
  col4, col5 = st.columns(2)

  with col4:
    st.image(img_or[3], caption="Image snake")
  with col5:
    st.image(img_or[4], caption='Image man')

st.write('### Linear Filtering')
st.write("""

  Linear filtering is filtering in which the value of an output pixel is a linear combination 
  of the values of the pixels in the input pixel's neighborhood. 

""")
    
################### Linear ###################
#################### Mean ####################
# st.write("#### Mean Filter")

image1 = cv2.imread(img_or[0])
image2 = cv2.imread(img_or[1])
image3 = cv2.imread(img_or[2])
image4 = cv2.imread(img_or[3])
image5 = cv2.imread(img_or[4])
img_list = [image1, image2, image3, image4, image5]

# mean filter function
def meanFilter(images):
  filtered = [cv2.blur(i, (3,3)) for i in images]
  return filtered

# median filter function
def medianFilter(images):
  filtered = [cv2.medianBlur(i, 5) for i in images]
  return filtered

# sobel
# def sobel(images):
#   sobel_filtered = []
#   c = 0
#   for i in images:
#     c = c+1
#     im = scipy.misc.imread(i)
#     im = im.astype('int32')
#     dx = ndimage.sobel(im, 0)  # horizontal derivative
#     dy = ndimage.sobel(im, 1)  # vertical derivative
#     mag = numpy.hypot(dx, dy)  # magnitude
#     mag *= 255.0 / numpy.max(mag)  # normalize (Q&D)
#     name = 'sobel'+str(c)+'.jpg'
#     scipy.misc.imsave('images/'+name, mag)
#     sobel_filtered.append(name)
#     mag = 0
#     name = ''

#   return sobel_filtered


meanFiltered = meanFilter(img_list)
medianFiltered = medianFilter(img_list)
# sobel_images = sobel(img_or)
col1, col2, col3, col4 = st.columns(4)
with col1:
  st.write("__Original__")
  st.image(img_or[0], caption="Original image 1")
  st.image(img_or[1], caption="Original image 2")
  st.image(img_or[2], caption="Original image 3")
  st.image(img_or[3], caption="Original image 4")
  st.image(img_or[4], caption="Original image 5")

with col2:
  st.write("__Mean Filter__")
  st.image(meanFiltered[0], caption="Mean filtered image 1")
  st.image(meanFiltered[1], caption="Mean filtered image 2")
  st.image(meanFiltered[2], caption="Mean filtered image 3")
  st.image(meanFiltered[3], caption="Mean filtered image 4")
  st.image(meanFiltered[4], caption="Mean filtered image 5")

with col3:
  st.write("__Median Filter__")
  st.image(medianFiltered[0], caption="Median filtered image 1")
  st.image(medianFiltered[1], caption="Median filtered image 2")
  st.image(medianFiltered[2], caption="Median filtered image 3")
  st.image(medianFiltered[3], caption="Median filtered image 4")
  st.image(medianFiltered[4], caption="Median filtered image 5")

# with col4:
#   st.write("__Sobel Filter__")
#   st.image(sobel_images[0], caption="Sobel filtered image 1")
#   st.image(sobel_images[1], caption="Sobel filtered image 2")
#   st.image(sobel_images[2], caption="Sobel filtered image 3")
#   st.image(sobel_images[3], caption="Sobel filtered image 4")
#   st.image(sobel_images[4], caption="Sobel filtered image 5")