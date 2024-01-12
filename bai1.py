import cv2 as cv
from cv2 import imshow
from scipy.signal import convolve2d
import numpy as np
img = cv.imread('img/bai1.png')
fft_c1 = np.fft.fftshift(np.fft.fft2(img[:,:,0]))
fft_c2 = np.fft.fftshift(np.fft.fft2(img[:,:,1]))
fft_c3 = np.fft.fftshift(np.fft.fft2(img[:,:,2]))
fft_img = np.dstack((fft_c1, fft_c2, fft_c3))
fft_img = np.log(abs(fft_img))