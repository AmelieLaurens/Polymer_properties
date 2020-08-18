#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy
import matplotlib.pyplot as plt
from math import *


class Result:
    
    def __init__(self, deck, polymer, model):
        
        self.deck = deck
        self.polymer = polymer
        self.model = model
        self.calculation_of_surface_tension(deck, polymer, model)
    
        

    def calculation_of_surface_tension(self, deck, polymer, model):
        molar_mass = model.molecular_weight(polymer.number_C, polymer.number_H, polymer.number_O, polymer.molecular_weight_C, polymer.molecular_weight_H, polymer.molecular_weight_O)
        molar_vol = model.molar_volume(molar_mass, polymer.density)
        parachor = model.molecular_parachor(polymer.number_C, polymer.number_H, polymer.number_O, polymer.parachor_C, polymer.parachor_H, polymer.parachor_O)
        surf_tension = model.surface_tension(parachor, molar_vol)
        return surf_tension
