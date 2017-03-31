# BBB-LCDDisplay
School assignment for Robotic Applied in ECAM Brussels.

Le but du laboratoire de gestion des périphériques étant de créer une librairie
python pour la gestion de différents périphériques liés à la Beaglebone Black.

Pour ce faire nous avons eut a disposition un servo moteur et un écran LCD connecté
à un circuit d'interfacage I2C.

## Members
- William Chagnot, 14151
- William De Decker, 14130
- Jonathan Petit, 13026

## Installation
Pour facilité l'utilisation de la librairie, nous avons déployé celle-ci sur pypi.

1. pip
```py
pip install BBB-LCDDisplay
```

un deuxième moyen d'installation de cette librairie est de simplement cloner ce repository.
2. Git
```
git clone https://github.com/JonathanPetit/BBB-LCDDisplay.git
```

## Utilisation
Différentes class sont présentes dans la librairie, mais toutes ne sont pas complètement
terminé et donc ne peuvent pas toutes servir. Les disponibles sont cochées:

- [ ] BBB_GPIO
- [ ] I2C
- [ ] Servo

La base de l'i2c disponible et fonctionnelle mais pas la connexion avec le lcd.
Après quelques approfondissements, plusieurs essais infructueux et quelques recherches
sur internet, nous avons découvert que la connexion i2c avec le lcd était plus ou moins
facile à mettre en oeuvre, mais la récupération des données par le lcd et l'affichage étant plus difficile
et demandant des connaissance et du temps difficile à mettre en oeuvre dans le cadre du temps
données en laboratoire.

Ensuite nous avons quelques soucis quant à gérer une pin PWM, c'est pour cela que
l'implémentation de servo.py reste incomplète.

Pour utiliser les différentes class, il suffit de l'importer dans son propre fichier
python une fois installé:

```py
from BBB-LCDDisplay import *
```

### Servo
```py
myservo = Servo(str(Pin_PWM)
```
fonctions disponibles:
- start()
- stop()
- polarity(int(polarity))
- dutycicle(int(dutycicle))
- fréquence(int(period))

### BBB_GPIO
```py
pin = BBB_GPIO(str(Pin)
```
- remove()
- value(HIGH or LOW)
- direction(INPUT or OUTPUT)

### I2C
```py
i2c = I2C(hex(address), int(port))
```
- start_i2c()
- stop_i2c()
- write(data)

## Organisation
```
BBB-LCDDisplay/
-- setup.py
-- README.md
-- BBB-LCDDisplay/
----__init__.py
---- servo.py
---- i2c.py
---- gpio.py
---- test.py
```

Le fichier test.py contient plusieurs exemple de code et d'utilisation comme une 
fonction pour faire clignoter une led avec notre librairie.

Pour plus de documentation sur la librairie, cf: Code sources!!!!

