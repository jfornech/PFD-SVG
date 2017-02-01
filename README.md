# PFD-SVG
Sources SVG qui vont permettre construire l'interface de contrôle. 

# Projet
Créer un module python qui permettra de modifier la balise XML matrix du fichier SVG. 

##Test depuis l'éditeur XML deInkscape
Rotation de 60° -> notation XML : matrix(0.5,-0.8660254,0.8660254,0.5,0,0)

##Explication
matrix(a,b,c,d,e,f);
a : cos(60) = 0,5;
b : -sin(60 = -0.8660254;
c : sin(60) = -0.8660254;
d : cos(60) = 0,5;
e : 0 = origine x (donc au centre de la forme);
f : 0 = origine y (donc au centre de la forme);

L’utilisation de « matrix » permet de conserver le centre de rotation au milieu de la forme contrairement à « transform(rotate(60)) » qui utilise un autre centre de rotation (pas encore déterminer pourquoi). 

