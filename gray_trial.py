from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import roberts, sobel, sobel_h, sobel_v, scharr, \
    scharr_h, scharr_v, prewitt, prewitt_v, prewitt_h

class Gray_scale_img:

    def __init__(self,path):
        '''
        take an image path and returns an image in the grayscale mode
        '''
        self.image = Image.open(path)
        self.image = self.image.convert(mode='L')
        return self.image

    def apply_detector(self,detector_name,img):
        '''
        takes the type of the edge detector and the image 
        returns ndarray of the image after applying the detector
        '''
        self.detectedd_img = detector_name(self.image)
        return self.detectedd_img
    
def plot_img(img_list,title):
        '''
            Takes a list of images and a list of titles for every image
            plot the images on a single page titled as ordered
        '''
    fig, ax = plt.subplots(ncols=len(img_list), sharex=True, sharey=True,
                    figsize=(8, 4))
    for i,img in enumerate(img_list):
        ax[i].imshow(img, cmap=plt.cm.gray)
        ax[i].set_title(title[i])
    for a in ax:
        a.axis('off')

    plt.tight_layout()
    plt.show()

imag = Gray_scale_img('new.jpeg')
robert_detector = imag.apply_detector(roberts,img)
sobel_detector = imag.apply_detector(sobel,img)
imag.plot_img([imag,robert_detector,sobel_detector],['origina','robert detector','sobel detector'])


