#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Polymer:

    # Initializer Attributes
    def __init__(self, deck):
        self.name = deck.doc['Surface Tension']['Name']
        self.number_C = int(deck.doc['Surface Tension']['Number of Carbon'])
        self.number_H = int(deck.doc['Surface Tension']['Number of Hydrogen'])
        self.number_O = int(deck.doc['Surface Tension']['Number of Oxygen'])
        self.parachor_C = float(deck.doc['Surface Tension']['Contribution to Parachor of Carbon in (cm^3/mol)*(erg/cm^2)^(1/4)'])
        self.parachor_H = float(deck.doc['Surface Tension']['Contribution to Parachor of Hydrogen in (cm^3/mol)*(erg/cm^2)^(1/4)'])
        self.parachor_O = float(deck.doc['Surface Tension']['Contribution to Parachor of Oxygen in (cm^3/mol)*(erg/cm^2)^(1/4)'])
        self.molecular_weight_C = float(deck.doc['Surface Tension']['Molecular Weight of Carbon in g/mol'])
        self.molecular_weight_H = float(deck.doc['Surface Tension']['Molecular Weight of Hydrogen in g/mol'])
        self.molecular_weight_O = float(deck.doc['Surface Tension']['Molecular Weight of Oxygen in g/mol'])
        self.density = float(deck.doc['Surface Tension']['Density in g/cm^3'])

    
