===============================
Documentació de codi font
===============================



Documentació de funcions
========================

Podem fer-ho aixÃ­:

.. function:: suma2(a, b)

   Retorna la suma d'a i b

   :param a: Un enter
   :type a:  int
   :param b: Un altre enter
   :type b:  int
   :returns:   Un enter resultat de sumar a i b
   :rtype: int


Una vegada documentada, la funció es pot referenciar des de qualsevol
lloc del text usant una construcció com aquesta :py: func:'suma2'.
D'aquesta manera es facilita notablement a l'usuari la consulta de la
documentació, especialment si ho fa on-line.

De forma automÃ tica la funció s'afegeix a l'Ã­ndex.



Documentació de mòduls
======================

TambÃ© tenim facilitats per documentar mòduls. En aquest cas l'estratègia Ã©s:


Mòdul  Sumador
--------------
.. module:: sumador
   :platform: GNU/Linux
   :synopsis: El mòdul sumador contè diverses operacions.

.. moduleauthor:: Sebas Vila

Aquest mòdul contÃ© una llista extensa de funcions que permeten fer sumes
amb diverses possibilitats mes o menys recargolades.

.. function:: suml(l)

   :param list l: Una llista d'enters
   :return int: La suma dels enters d'l


.. function:: suml2(l)

   :param list l: Una llista d'enters
   :return: La suma dels enters d'l
   :rtype: int

i mes




