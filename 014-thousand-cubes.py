# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 16:55:02 2025

@author: ABDUL JABBAR KHAN
"""
from vpython import *

bigCube = []
redColor = 0
greenColor = 0
blueColor = 0
colorInc = 0.1   
for xPos in range(-10,10,2):
    greenColor = 0
    for yPos in range(-10,10,2):
        redColor = 0
        for zPos in range (-10,10,2):
            cube = box(size = vector(1,1,1),
                       pos = vector(xPos,yPos,zPos),
                       color = vector(redColor, greenColor, blueColor)
                       )
            bigCube.append(cube)
            redColor += colorInc
        greenColor += colorInc
    blueColor += colorInc

rAngle=0.01
while True:
    rate(500)
    for cube in bigCube:
        cube.rotate(angle = rAngle , axis = vector(0,1,0), origin = cube.pos )