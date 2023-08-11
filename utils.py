# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 09:49:18 2022

@author: 15308
"""
from pptx.util import Inches


#A Tool Converting cm to emu
def cm2emu(cm):
    return Inches(cm/2.54)

