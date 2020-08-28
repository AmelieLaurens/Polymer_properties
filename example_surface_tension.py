from surface_tension import *
from common_classes import *


cwd = os.getcwd()

deck = Deck(cwd + "/" + "deck.yaml")

constants = Deck(cwd + "/" + "constants.yaml")

polymer = Polymer(deck, constants)

model = Model(deck, polymer)

result = Result(deck, polymer, model)

surface_tension = result.calculation_of_surface_tension(deck, polymer, model)

print('The polymer surface tension is : ' '%s (in g/s^2).' % (surface_tension))
