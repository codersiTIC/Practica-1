
================
Llistes a python
================
|

:Autors: Anass Anhari, Marcel Compte i Daniel Alamillo
	 
|

Definició
=========


	   * Una llista és un conjunt ordenat de dades en que cadascun dels
	     seus element està relacionat amb un índex, corresponent a la
	     posició que ocupa.

	   * Al contrari que les cadenes de caràcters (*strings*), admeten
	     qualsevol tipus de paràmetre (incloent-hi els propis strings,
	     a part de lletres, enters, decimals, tuples, altres llistes...).
	     Tant les llistes com els *strings* (entre altres conjunts ordenats
	     de dades), formen part de les anomenades *seqüències* (dins
	     l'argot de *Python*).

|

Creació d'una llista
====================
	   * Les llistes s'identifiquen amb els símbols *[* i *]* i els seus
	     element van separats per comes ( *,* ). Així doncs, per crear-les
	     necessitarem introduïr elements entre claudàtors separats per
	     comes, de la següent forma:


	     .. code-block:: python

		>>> l = [10, 4, 6, 7]
		>>> i = ['a', 'e', 'i', 'o', 'u']
		>>> s = [ ]
		>>> t = [25, 65, 'a', (8,9), ('a',5), ['patata', 25]]

		
* L'exemple anterior mostra quatre casos de llistes, d'elements de tot tipus
  (incloent-hi l'anomenada *llista buida* que no conté cap element) i com podem
  assignar-li una variable.

|

Accés als elements, indexació de les llistes
============================================

	   * Per accedir als elements de les llistes, hem de tenir en compte
	     quin índex tenen associat. Els índex s'assignen als elements
	     d'una llista en funció de l'ordre que tenen en aquesta (començant
	     des de 0 (primer element), comptant fins acabar-la). Tenint
	     clar quin index correspon a cada element, podem invocar-los
	     de la següent forma:


	     .. code-block:: python

		>>> llista = [2, 'a', 4, 'patata']
		>>> llista[0] #Primer element
		2
		>>> llista[1] #Segon element
		a
		>>> llista[2] #Tercer element
		4
		>>> llista[3] #Últim element (en aquest cas el quart)
		patata

|

* A més a més, també tenim la possiblitat d'invocar un segment d'una
  llista. Per fer-ho, indicarem l'index de l'element amb el que
  volem iniciar la seqüència i el de l'últim sumant-li u (col·locats
  entre dos punts ( *:* )).

  .. code-block:: python

		  >>> llista = [2, 'a', 4, 'patata']
		  >>> llista[1:3]
		  ['a', 4]
		  >>> llista[0:4] #Retorna la llista sencera
		  [2, 'a', 4, 'patata']
		  >>> llista[2:3] #Retorna una llista amb l'element d'índex 2
		  [4] 


Iteració sobre llistes
======================
	   * Per iterar en una llistar i recòrrer cadascun dels seus elements
	     un per un, tenim dos estructures perfectament vàlides: *for* i
	     *while*. 


	   
		
