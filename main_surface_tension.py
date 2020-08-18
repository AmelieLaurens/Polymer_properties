from surface_tension import *


cwd = os.getcwd()

deck = Deck(cwd + "/" + "deck.yaml")

polymer = Polymer(deck)

model = Model(deck, polymer)

result = Result(deck, polymer, model)

surface_tension = result.calculation_of_surface_tension(deck, polymer, model)

print(surface_tension)
