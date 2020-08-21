# Polymer properties

## Viscosity

### Compute the viscosity as a function of the temperature and the shear stress  

<img src="https://latex.codecogs.com/gif.latex?\eta&space;=&space;B&space;exp(\frac{E_{\tau&space;}}{RT}-b\tau&space;^{s})" title="\eta = B exp(\frac{E_{\tau }}{RT}-b\tau ^{s})" />


&nbsp;


<img src="https://latex.codecogs.com/gif.latex?\eta" title="\eta" /> : Melt viscosity (Pa.s)

<img src="https://latex.codecogs.com/gif.latex?\tau" title="\tau" /> : Shear stress

<img src="https://latex.codecogs.com/gif.latex?E_{\tau&space;}" title="E_{\tau }" /> : activation energy of viscous-elastic flow under condition of <img src="https://latex.codecogs.com/gif.latex?\tau" title="\tau" /> = constant

R : gas constant in J/(mol.K)

T : temperature of experiment in K

B, b, s : Constants of the material (in this case : s=1/2)



### How this code works ?

**Classes**
- Deck : get the value in deck.yaml (in the folder common_classes)
- Polymer : stock the values of deck concerning the polymer in variables that will be reuse (in the folder common_classes)
- GraphFeatures : stock the values of deck concerning graphic features in variables that will be reuse (in the folder viscosity)
- Model : contain the equation to predict the viscosity (in the folder viscosity)
- Graph : calculate the data with the model, draw the graphic and save it in the folder Graphics (in the folder viscosity)


**What the user have to do ?**
- Adapt the values in the file deck.yaml :

```yaml
Polymers:
  Name: 'PP Shell'
  Constant B: 1.5
  Constant b: 0.0043
  Activation Energy: 45522

Discretisation: 20
```

The Discretisation number is the number of points on the graphics.

- Install all required python packages listed in requirements.txt: 

```linux
pip install -r requirements.txt
```

- The only file which need to be run is the example_viscosity.py. This script brings together all classes.

```linux
python example_viscosity.py
```

## Surface tension

### Calculate a polymer surface tension with the Parachor

- Calculate the molecular weight of the polymer : 
<img src="https://latex.codecogs.com/gif.latex?M&space;=&space;N_{C}&space;M_{C}&space;&plus;&space;N_{H}&space;M_{H}&space;&plus;&space;N_{O}&space;M_{O}" title="M = N_{C} M_{C} + N_{H} M_{H} + N_{O} M_{O}" />

M : Molecular weight of the polymer (g/mol)
<img src="https://latex.codecogs.com/gif.latex?N_{C},&space;N_{H},&space;N_{O}" title="N_{C}, N_{H}, N_{O}" /> : Number of Carbon, Hydrogen and Oxygen in a monomer unit
<img src="https://latex.codecogs.com/gif.latex?M_{C},&space;M_{H},&space;M_{O}" title="M_{C}, M_{H}, M_{O}" /> : Atomic weight of Carbon, Hydrogen and Oxygen (g/mol)

- Calculate the Molar Volume :
<img src="https://latex.codecogs.com/gif.latex?V_{M}&space;=&space;\frac{M}{\rho&space;}" title="V_{M} = \frac{M}{\rho }" />

<img src="https://latex.codecogs.com/gif.latex?V_{M}" title="V_{M}" /> : Molar Volume (<img src="https://latex.codecogs.com/gif.latex?cm^{3}/mol" title="cm^{3}/mol" />)
<img src="https://latex.codecogs.com/gif.latex?\rho" title="\rho" /> : Density of the polymer (<img src="https://latex.codecogs.com/gif.latex?g/cm^{3}" title="g/cm^{3}" />)

- Calculate the Molecular Parachor
<img src="https://latex.codecogs.com/gif.latex?P&space;=&space;N_{C}&space;P_{C}&space;&plus;&space;N_{H}&space;P_{H}&space;&plus;&space;N_{O}&space;P_{O}" title="P = N_{C} P_{C} + N_{H} P_{H} + N_{O} P_{O}" />

P : Molecular Parachor (<img src="https://latex.codecogs.com/gif.latex?(cm^{3}/mol)&space;(erg/cm^{2})^{\frac{1}{4}}" title="(cm^{3}/mol) (erg/cm^{2})^{\frac{1}{4}}" />)
<img src="https://latex.codecogs.com/gif.latex?P_{C},&space;P_{H},&space;P_{O}" title="P_{C}, P_{H}, P_{O}" /> : Contribution to Parachor of Carbon, Hydrogen and Oxygen (<img src="https://latex.codecogs.com/gif.latex?(cm^{3}/mol)&space;(erg/cm^{2})^{\frac{1}{4}}" title="(cm^{3}/mol) (erg/cm^{2})^{\frac{1}{4}}" />)

- Calculate the Surface Tension
<img src="https://latex.codecogs.com/gif.latex?\sigma&space;=&space;(\frac{P}{V})^{4}" title="\sigma = (\frac{P}{V})^{4}" />

<img src="https://latex.codecogs.com/gif.latex?\sigma" title="\sigma" /> : Surface Tension (<img src="https://latex.codecogs.com/gif.latex?g/s^{2}" title="g/s^{2}" />)


### How this code works ?

**Classes**
- Deck : get the value in deck.yaml (in the folder common_classes)
- Polymer : stock the values of deck concerning the polymer in variables that will be reuse (in the folder common_classes)
- Model : contain all functions required to predict the surface tension (in the folder surface_tension)
- Result : calculate the value of the surface tension with the functions in Model and print it (in the folder surface_tension)

**What the user have to do ?**

In the deck.yaml, the user can change the polymer and adapt the required values.

```yaml
Surface Tension:
  Name: 'Polypropylene'
  Number of Carbon: 3
  Number of Hydrogen: 6
  Number of Oxygen: 0
  Density in g/cm^3: 0.9
```

- Install all required python packages listed in requirements.txt: 

```linux
pip install -r requirements.txt
```

- The only file which need to be run is the example_surface_tension.py. This script brings together all classes.

```linux
python example_surface_tension.py
```
