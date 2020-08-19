from viscosity import *
from common_classes import *


cwd = os.getcwd()

deck = Deck(cwd + "/" + "deck.yaml")

polymer = Polymer(deck)

model = Model(deck, polymer)

features = GraphFeatures(deck)

graph = Graph(deck, polymer, model, features)
