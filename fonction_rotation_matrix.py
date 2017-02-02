#!/usr/bin/env python
# coding: utf-8

import math

def rotate(degre,posX,posY,largeur,hauteur):
	'''
	Besoins de la fonction
	degre : angle en degré de la rotation souhaitée 
	posX : Position initiale de x de la forme
	posy : Position initiale de y de la forme
	largeur : largeur de la forme
	hauteur : hauteur de la forme
	'''
	angle = degre
	centre_posX = posX + largeur/2
	centre_posY = posY + hauteur/2

	print ("transform=\"rotate({0},{1},{2})\"").format(degre, centre_posX, centre_posY)
	print (""Fonction rotate")
	       
rotate(60,0,0,500,500)
	       
def matrix(degre,posX,posY,largeur,hauteur):
	'''
	Besoins de la fonction matrix:
	degre : angle en degré de la rotation souhaitée 
	posX : Position initiale de x de la forme
	posy : Position initiale de y de la forme
	largeur : largeur de la forme
	hauteur : hauteur de la forme
	'''
	angle = degre
	OrigineX = posX + largeur/2
	OrigineY = posY + hauteur/2
	a = math.cos(math.radians(angle))
	b = -math.sin(math.radians(angle))
	c = math.sin(math.radians(angle))
	d = math.cos(math.radians(angle))
	e = OrigineX      
	f = OrigineY
	       
	print (""Fonction Matrix")	       
	print("matrix({0},{1},{2},{3},{4},{5})").format(a,b,c,d,e,f)
      
matrix(60,0,0,500,500)
