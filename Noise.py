# -*- coding: utf-8 -*-
"""Noise.py: Adding differents noises to an image"""

__author__ = "CERVERA Maxime and SABATHE Lucas"
__copyright__ = "Copyright 2020"
__version__ = "1.3.2"


""" IMPORTS """
import numpy as np


""" ADDING Gaussian Noise """
def addGaussianNoise(img):
    noise = np.random.normal(0, 20, img.shape)
    for y in range(noise.shape[1]):
        for x in range(noise.shape[0]):
            noise[y, x] = int(noise[y, x])
    noisy_img = img + noise
    noisy_img[noisy_img < 0] = 0
    noisy_img[noisy_img > 255] = 255
    return np.uint8(noisy_img)


""" ADDING Salt & Pepper Noise """
def addSaltNPepper(img):
    prob = 0.05
    rnd = np.random.rand(img.shape[0], img.shape[1])
    noisy_img = img.copy()
    noisy_img[rnd < prob] = 255
    noisy_img[rnd > 1 - prob] = 0
    return noisy_img


""" ADDING Multiplicative Noise """
def addMultiplicativeNoise(img):
    noise = np.random.randint(0, 10, img.shape)/10
    noisy_img = img / (1 + noise)
    noisy_img[noisy_img < 0] = 0
    noisy_img[noisy_img > 255] = 255
    return np.uint8(noisy_img)