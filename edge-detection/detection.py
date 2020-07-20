from PIL import Image,ImageFilter
import numpy as np
import matplotlib.pyplot as plt
import matplotlib 

from skimage.filters import roberts, sobel, sobel_h, sobel_v, scharr, \
    scharr_h, scharr_v, prewitt, prewitt_v, prewitt_h


class MyImage:

    def __init__(self,path):
        self.original = Image.open(path)
        self.image = self.original.convert(mode='L')
        self.image.save('./gray_saved.jpg') 
        self.gray_path = './gray_saved.jpg'

    def return_tupled_image(self):
        return self.original,self.image,self.gray_path


    def apply_detector(self,detector_name):
        '''
        takes the type of the edge detector and the image 
        returns ndarray of the image after applying the detector
        '''
        self.detected_img = detector_name(self.image)
        #self.detected_pil = Image.fromarray(self.detected_img)
        matplotlib.image.imsave('./detected.jpg',self.detected_img,cmap=plt.cm.gray)
        #self.detected_path = self.detected_pil.save('./detedted.png')
        return self.detected_img,'./detected.jpg'
        

    def noise_removal(self):
        '''
        returns a noise-free image(an image without noise)
        blur an image then apply minimum filter to it
        '''
        im1 = self.original.filter(ImageFilter.BLUR)
        im2 = self.original.filter(ImageFilter.MinFilter(3))
        saved = im2.save('noise-free.png')
        return './noise-free.png'

    



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



