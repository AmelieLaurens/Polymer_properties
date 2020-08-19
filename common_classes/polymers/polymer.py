#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Polymer:

    # Initializer Attributes
    def __init__(self, deck, constants):
        self.name = deck.doc['Polymers']['Name']
        self.constantB = float(deck.doc['Polymers']['Constant B'])
        self.constantb = float(deck.doc['Polymers']['Constant b'])
        self.energy = float(deck.doc['Polymers']['Activation Energy'])
        self.name_bird = deck.doc['Polymers']['Constants for Carreau-Arrhenius model']['Name']
        self.constant_k1 = float(deck.doc['Polymers']['Constants for Carreau-Arrhenius model']['Constant k1'])
        self.constant_k2 = float(deck.doc['Polymers']['Constants for Carreau-Arrhenius model']['Constant k2'])
        self.constant_k3 = float(deck.doc['Polymers']['Constants for Carreau-Arrhenius model']['Constant k3'])
        self.activation_energy = float(deck.doc['Polymers']['Constants for Carreau-Arrhenius model']['Activation Energy'])
        self.ref_temperature = float(deck.doc['Polymers']['Constants for Carreau-Arrhenius model']['Reference Temperature'])
        self.gas_constant = float(constants.doc['Viscosity Constants']['Gas Constant'])
        self.name = deck.doc['Surface Tension']['Name']
        self.number_C = int(deck.doc['Surface Tension']['Number of Carbon'])
        self.number_H = int(deck.doc['Surface Tension']['Number of Hydrogen'])
        self.number_O = int(deck.doc['Surface Tension']['Number of Oxygen'])
        self.parachor_C = float(constants.doc['Surface Tension Constants']['Contribution to Parachor of Carbon in (cm^3/mol)*(erg/cm^2)^(1/4)'])
        self.parachor_H = float(constants.doc['Surface Tension Constants']['Contribution to Parachor of Hydrogen in (cm^3/mol)*(erg/cm^2)^(1/4)'])
        self.parachor_O = float(constants.doc['Surface Tension Constants']['Contribution to Parachor of Oxygen in (cm^3/mol)*(erg/cm^2)^(1/4)'])
        self.molecular_weight_C = float(constants.doc['Surface Tension Constants']['Molecular Weight of Carbon in g/mol'])
        self.molecular_weight_H = float(constants.doc['Surface Tension Constants']['Molecular Weight of Hydrogen in g/mol'])
        self.molecular_weight_O = float(constants.doc['Surface Tension Constants']['Molecular Weight of Oxygen in g/mol'])
        self.density = float(deck.doc['Surface Tension']['Density in g/cm^3'])

    
