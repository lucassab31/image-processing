# -*- coding: utf-8 -*-
"""Main.py: Images processing"""

__author__ = "CERVERA Maxime and SABATHE Lucas"
__copyright__ = "Copyright 2020"
__version__ = "1.7.5"


""" IMPORTS """
import numpy as np
from skimage import io

""" PERSONNAL IMPORTS """
import Noise
import Filter

""" FUNCTION SNR """
def snr(imgRef, imgBruit):
    imgRef = np.uint64(imgRef)
    imgBruit = np.uint64(imgBruit)
    return 10*np.log10(np.sum(imgBruit**2)/np.sum((imgBruit-imgRef)**2))


""" Images reading """
imgR = io.imread('ressources/imgR.png', as_gray=True)
imgB = io.imread('ressources/imgB.png', as_gray=True)

""" SNR """
print ("SNR = ", snr(imgR, imgB))

""" Adding noises """
imgGaussian = Noise.addGaussianNoise(imgR)
imgSNP = Noise.addSaltNPepper(imgR)
imgMultiplicative = Noise.addMultiplicativeNoise(imgR)
""" Saving addded noises """
io.imsave("ressources/noise/NoiseGaussian.png", imgGaussian)
io.imsave("ressources/noise/NoiseSalt-Pepper.png", imgSNP)
io.imsave("ressources/noise/NoiseMultiplicative.png", imgMultiplicative)
# =============================================================================
# 
# """ Filtering images """
# imgSNPFiltre = Filter.medianfilter(imgSNP)
# imgGaussianFiltre = Filter.convolutionfilter(imgGaussian)
# """ Saving filtered images """
# io.imsave("ressources/filter/NoiseSalt-PepperFiltre.png", imgSNPFiltre)
# io.imsave("ressources/filter/NoiseGaussianFilter.png", imgGaussianFiltre)
# =============================================================================
