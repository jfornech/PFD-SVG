# Projet
Créer un module python qui accède et modifie les noeuds XML d'un fichier SVG.

## Contenu du repository
Sources SVG qui vont permettre construire l'interface de contrôle. 

#Tests
##Test de rotation depuis Inkscape
Rotation de 60° -> notation XML : matrix(0.5,-0.8660254,0.8660254,0.5,0,0)

###Explication
matrix(a,b,c,d,e,f);
- a : cos(60) = 0,5
- b : -sin(60) = -0.8660254
- c : sin(60) = -0.8660254 
- d : cos(60) = 0,5
- e : 0 = origine x (donc au centre de la forme) 
- f : 0 = origine y (donc au centre de la forme)

L’utilisation de « matrix » permet de conserver le centre de rotation au milieu de la forme contrairement à « transform(rotate(60)) » qui utilise un autre centre de rotation (pas encore déterminer pourquoi). 
 
 ## Noeud XML script Python 
```
import math
def rotate(degre):
	angle = degre
	print "angle en degre : {0}".format(angle)
	a = math.cos(math.radians(angle))
	b = -math.sin(math.radians(angle))
	c = math.sin(math.radians(angle))
	d = math.cos(math.radians(angle))
	e = 0
	f = 0
	print ("matrix ({0},{1},{2},{3},{4},{5}),").format(a,b,c,d,e,f)

rotate(60)
```
