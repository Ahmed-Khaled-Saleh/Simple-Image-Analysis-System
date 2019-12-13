from PIL import Image,ImageFilter
import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import roberts, sobel, sobel_h, sobel_v, scharr, \
    scharr_h, scharr_v, prewitt, prewitt_v, prewitt_h

class MyImage:

    def __init__(self,path):
        self.original = Image.open(path)
        self.image = self.original.convert(mode='L')

    def return_tupled_image(self):
        return self.original,self.image


    def apply_detector(self,detector_name):
        '''
        takes the type of the edge detector and the image 
        returns ndarray of the image after applying the detector
        '''
        self.detected_img = detector_name(self.image)
        return self.detected_img

    def noise_removal(self):
        im1 = self.original.filter(ImageFilter.BLUR)
        im2 = self.original.filter(ImageFilter.MinFilter(3))
        return im2



def plot_img(img_list,titles):
    '''
        Takes a list of images and a list of titles for every image
        plot the images on a single page titled as ordered
    '''
    fig,ax = plt.subplots(ncols=len(img_list), sharex=True, sharey=True, figsize=(8, 4))
    for i,img in enumerate(img_list):
        ax[i].imshow(img, cmap=plt.cm.gray)
        ax[i].set_title(titles[i])
    for a in ax:
        a.axis('off')

    plt.tight_layout()
    plt.show()



