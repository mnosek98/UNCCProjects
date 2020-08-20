#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:58:21 2019
@author: mnosek
"""

#import math
#import numpy

def predict(mean1, variance1, mean2, variance2):    
    meanPrime = mean1 + mean2
    variancePrime = variance1 + variance2 
    
    print("Mean Predict: " + meanPrime)
    print("Variance Predict: " + variancePrime)
    
def update(mean1, variance1, mean2, variance2):
    meanPrime = (1 / (variance1 + variance2)) * ((variance2 * mean1) + (variance1 * mean2))
    variancePrime = 1/((1/variance1) + (1/variance2))
    
    print("Mean Update: " + meanPrime)
    print("Variance Update: " + variancePrime)
    
def main():
    motion = [1.0, 1.0, 2.0, 1.0, 1.0]
    measurements = [5.0, 6.0, 7.0, 9.0, 10.0]
    measurementUncertainty = 4.0
    motionUncertainty = 2.0
    
    initialBelief = [0.0, 1000.0]
    
    for ()
    
    predict(mean1,variance1, mean2, variance2)
    
    update(mean1, variance1, mean2, variance2)
    
    

if __name__ == '__main__':
    main()

