import streamlit as st

def app():
    st.write("# Module: Image processing")
    st.write("""
        __Find me at:__ [Twitter](https://twitter.com/nainia_ayoub) | [LinkedIn](https://www.linkedin.com/feed/) | [GitHub](https://github.com/nainiayoub)

        This project represents my solution for the image processing module's assignement, 
        in which you can access each project at a time with the navbar.

        
    
    """)
    st.write("""
        #### Table of contents
        * [Image Filtering](#image-filtering-101)
            * [Linear Filtering](#linear-filtering)
            * [Non-linear filtering](#non---linear-filtering)
        * [Image Compression](#image-compression-101)
            * [JPEG](#jpeg)
            * [MPEG](#mpeg)

    """)
    st.write("## Image Filtering 101")
    st.write("""

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
    """)


    st.write("""

    

    """)




    