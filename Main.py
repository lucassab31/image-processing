# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 14:14:24 2020

@author: CERVERA Maxime && SABATHE Lucas
"""

import numpy as np
from skimage import io

def snr(imgRef, imgBruit):
    imgRef = np.uint64(imgRef)
    imgBruit = np.uint64(imgBruit)
    return 10*np.log10(np.sum(imgBruit**2)/np.sum((imgBruit-imgRef)**2))
   
def addGaussianNoise(img):
    noise = np.random.normal(0, 20, img.shape)
    for y in range(noise.shape[1]):
        for x in range(noise.shape[0]):
            noise[y, x] = int(noise[y, x])
    noise[noise < 0] = 0
    noisy_img = img + noise
    noisy_img[noisy_img < 0] = 0
    noisy_img[noisy_img > 255] = 255
    return np.uint8(noisy_img)

def addSaltNPepper(img):
    prob = 0.05
    rnd = np.random.rand(img.shape[0], img.shape[1])
    noisy_img = img.copy()
    noisy_img[rnd < prob] = 255
    noisy_img[rnd > 1 - prob] = 0
    return noisy_img

def addMultiplicativeNoise(img):
    noise = np.random.normal(0, 5, img.shape)
    for y in range(noise.shape[1]):
        for x in range(noise.shape[0]):
            noise[y, x] = int(noise[y, x])
    noise[noise < 0] = 0
    noisy_img = img * (1 + noise)
    noisy_img[noisy_img < 0] = 0
    noisy_img[noisy_img > 255] = 255
    return np.uint8(noisy_img)

def medianfilter(imgBruit):
    image_filtre = imgBruit.copy()
    for i in range(imgBruit.shape[0]):
        for j in range(imgBruit.shape[1]):
            listePixel = list()
            for i1 in range (i-1, i+2):
                for j1 in range (j-1, j+2):
                    if (j1 >= 0 and j1<imgBruit.shape[1]
                    and i1 >= 0 and i1<imgBruit.shape[0]):
                        listePixel.append(imgBruit[i1,j1])
            image_filtre[i,j]=np.median(listePixel)
    return image_filtre

def convolutionfilter(imgBruit):
    image_filtre = imgBruit.copy()
    for i in range(imgBruit.shape[0]):
        for j in range(imgBruit.shape[1]):
            listePixel = list()
            for i1 in range (i-1, i+2):
                for j1 in range (j-1, j+2):
                    if (j1 >= 0 and j1<imgBruit.shape[1]
                    and i1 >= 0 and i1<imgBruit.shape[0]):
                        listePixel.append((1/9)*imgBruit[i1,j1])
            image_filtre[i,j]=np.sum(listePixel)
    return image_filtre


imgR = io.imread('ressources/imgR.png', as_gray=True)
imgB = io.imread('ressources/imgB.png', as_gray=True)

print ("SNR = ", snr(imgR, imgB))

imgGaussian = addGaussianNoise(imgR)
imgSNP = addSaltNPepper(imgR)
imgMultiplicative = addMultiplicativeNoise(imgR)

imgSNPFiltre = medianfilter(imgSNP)
imgGaussianFiltre = convolutionfilter(imgGaussian)

io.imsave("ressources/noise/NoiseGaussian.png", imgGaussian)
io.imsave("ressources/noise/NoiseSalt-Pepper.png", imgSNP)
io.imsave("ressources/noise/NoiseMultiplicative.png", imgMultiplicative)

io.imsave("ressources/filter/NoiseSalt-PepperFiltre.png", imgSNPFiltre)
io.imsave("ressources/filter/NoiseGaussianFilter.png", imgGaussianFiltre)
#io.imshow(imgSNP, cmap='gray')