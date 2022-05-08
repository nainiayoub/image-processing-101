# Image Processing 101
__Find me at:__ [Twitter](https://twitter.com/nainia_ayoub) | [LinkedIn](https://www.linkedin.com/feed/) | [GitHub](https://github.com/nainiayoub)

This project represents my solution for the image processing module's assignement, which is a multipage streamlit app that contains image processing sub implementations.

https://user-images.githubusercontent.com/50157142/143588521-f86080c0-ddb6-474c-9284-d8bfa225c351.mp4


## Table of contents
* [Image Filtering 101](#image-filtering-101)
    * [Linear Filtering](#linear-filtering)
    * [Non-linear filtering](#non-linear-filtering)
* [Image Compression 101](#image-compression-101)
    * [JPEG standard](#jpeg)

## Image Filtering 101
Filtering is a neighborhood operation, in which the value of any given pixel in the output image is determined
by applying some algorithm to the values of the pixels in the neighborhood of the corresponding input pixel.

_http://www.ece.northwestern.edu/local-apps/matlabhelp/toolbox/images/linfilt3.html_

### Linear Filtering
Linear filtering is filtering in which the value of an output pixel is a linear combination 
of the values of the pixels in the input pixel's neighborhood. In this project, we will be implementing two linear algorithms:
* Mean (average) Filter
* Sobel Filter

### Non-linear Filtering
A Non-linear filter denotes an operator which replaces the value of each pixel by another
 value which is a non-linear combination of the values ​​of its neighboring pixels. We will implement two non-linear filters:
* Median Filter
* Spectral Filter


