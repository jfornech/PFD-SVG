# Projet
Créer un module python qui modifie la balise XML matrix du fichier SVG. 

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
 
