#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import exp


class Model:

    # Initializer Attributes
    def __init__(self, deck, polymer):
        self.deck = deck
        self.polymer = polymer


    # from [abhinandan_surface_2005] see biblio.bib
    def molecular_weight(self, number_C, number_H, number_O, molecular_weight_C, molecular_weight_H, molecular_weight_O):
        """ 
        Calculation of the molecular weight of polymer
        
        :Input:  
        - *number_C* : Number of Carbon in a monomer unit
        - *number_H* : Number of Hydrogen in a monomer unit
        - *number_O* : Number of Oxygen in a monomer unit
        - *molecular_weight_C* : Atomic weight of Carbon (g/mol)
        - *molecular_weight_H* : Atomic weight of Hydrogen (g/mol)
        - *molecular_weight_O* : Atomic weight of Oxygen (g/mol)

        :Returns:
        Molecular weight of the polymer (g/mol)

        """
        return number_C * molecular_weight_C + number_H * molecular_weight_H + number_O * molecular_weight_O


    # from [abhinandan_surface_2005] see biblio.bib
    def molar_volume(self, molecular_weight, density):
        """ 
        Calculation of the Molar Volume
        
        :Input:  
        - *molecular_weight* : Molecular weight of the polymer (g/mol)
        - *density* : Density of the polymer (g/cm^3)

        :Returns:
        Molar Volume (cm^3/mol)

        """
        return molecular_weight / density 


    # from [abhinandan_surface_2005] see biblio.bib
    def molecular_parachor(self, number_C, number_H, number_O, parachor_C, parachor_H, parachor_O):
        """ 
        Calculation of the Molecular Parachor
        
        :Input:  
        - *number_C* : Number of Carbon in a monomer unit
        - *number_H* : Number of Hydrogen in a monomer unit
        - *number_O* : Number of Oxygen in a monomer unit
        - *parachor_C* : Contribution to Parachor of Carbon ((cm^3/mol)*(erg/cm^2)^(1/4))
        - *parachor_H* : Contribution to Parachor of Hydrogen ((cm^3/mol)*(erg/cm^2)^(1/4))
        - *parachor_O* : Contribution to Parachor of Oxygen ((cm^3/mol)*(erg/cm^2)^(1/4))

        :Returns:
        Molecular Parachor ((cm^3/mol)*(erg/cm^2)^(1/4))

        """
        return number_C * parachor_C + number_H * parachor_H + number_O * parachor_O


    # from [abhinandan_surface_2005] see biblio.bib
    def surface_tension(self, parachor, molar_volume):
        """ 
        Calculation of the Surface Tension
        
        :Input:  
        - *parachor* : Parachor ((cm^3/mol)*(erg/cm^2)^(1/4))
        - *molar_volume* : Molar Volume (cm^3/mol)
        
        :Returns:
        Surface Tension (g/s^2)

        """
        return (parachor / molar_volume)**4
