from viscosity import *
from common_classes import *


cwd = os.getcwd()

os.makedirs(cwd + "/" + "graphics", exist_ok=True)

deck = Deck(cwd + "/" + "deck.yaml")

constants = Deck(cwd + "/" + "constants.yaml")

polymer = Polymer(deck, constants)

model = Model(deck, polymer)

features = GraphFeatures(deck)

graph = Graph(deck, polymer, model, features)
