# -*- coding: utf-8 -*-
"""Filter.py: Removing differents noises to an image"""

__author__ = "CERVERA Maxime and SABATHE Lucas"
__copyright__ = "Copyright 2020"
__version__ = "1.2.4"


""" IMPORTS """
import numpy as np


""" Removing Gaussian Noise """
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


""" Removing Salt & Pepper Noise """
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