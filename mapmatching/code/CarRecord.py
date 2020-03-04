# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 21:15:27 2020

@author: 86189
"""

class CarRecord:
    def __init__(self, argv):
        self.car_id = int(argv[0])
        self.time = argv[1]
        self.geo = [float(ele) for ele in argv[2:4]]
        self.speed = float(argv[4])
        self.direction = float(argv[5])