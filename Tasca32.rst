
----------------
Llistes a python
----------------

.. topic:: Definició

	   * Una llista és un conjunt ordenat de dades en que cadascun dels
	     seus element està relacionat amb un índex, corresponent a la
	     posició que ocupa.

	   * Al contrari que les cadenes de caràcters (*strings*), admeten
	     qualsevol tipus de paràmetre (incloent-hi els propis *strings*,
	     a part de lletres, enters, decimals, tuples, altres llistes...)
	     i són de tipus mutable (que, a grans trets, vol dir que poden ser
	     modificades sense canviar la seva identitat, la variable amb que
	     les hem assignat). La classe predefinida *list* conté métodes
	     modificadors, capaços d'alterar el contingut d'una llista.

	     
	   * Tant les llistes com els *strings* (entre altres conjunts ordenats
	     de dades), formen part de les anomenades *seqüències* (dins
	     l'argot de *Python*).

|

.. topic:: Creació d'una llista

	   * Les llistes s'identifiquen amb els símbols *[* i *]* i els seus
	     element van separats per comes ( *,* ). Així doncs, per crear-les
	     necessitarem introduïr elements entre claudàtors separats per
	     comes, de la següent forma:


	     .. code-block:: python

		>>> l = [10, 4, 6, 7]
		>>> i = ['a', 'e', 'i', 'o', 'u']
		>>> s = [ ]
		>>> t = [25, 65, 'a', (8,9), ('a',5), ['patata', 25]]

		
* L'exemple anterior mostra quatre casos de llistes d'elements de tot tipus
  (incloent-hi l'anomenada *llista buida* que no en conté cap) i com podem
  assignar-les a una variable.

|

.. topic:: Accés als elements, indexació de les llistes

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

|

.. topic:: Iteració sobre llistes

	* Per iterar sobre una llista i recòrrer cadascun dels seus elements
	  un per un, tenim dos estructures perfectament vàlides: *for* i
	  *while*.

        * El bucle *for* permet iterar sobre una llista d'una forma
          senzilla i elegant, sense haver d'utilitzar cap comptador extern.
          La sintaxi d'aquest bucle és la següent:


	 .. code-block:: python

		#Estructura general
		for VARIABLE in LLISTA: 
		   INSTRUCCIONS

	* Seguint aquesta estructura, podem manipular les llistes d'una manera
	  molt versàtil, afegint instruccions de tota mena. A continuació,
	  alguns exemples:


	 .. code-block:: python

		>>> ll = [2, 3, 4, 's']
		>>> for element in ll:
		...     print element,
		...
		2 3 4 s
		>>> for number in range(5): #range(5) = [0,1,2,3,4]
		...     if number % 2 == 0:
                ...        print number,
		...     else:
		...        print '@',
		...
		0 @ 2 @ 4
		  

	* L'iterador *while*, tot i fer la mateixa funció que *for*, precisa
	  d'un comptador extern que controli les vegades que s'efectua el bucle.
	  La seva estructura general és:

	  .. code-block:: python

		i = 0 #El comptador
		while i < len(LLISTA):
		    NOM_VARIABLE = LLISTA[i] #Pas no estrictament necessari 
		    INSTRUCCIONS             
		    i += 1

	* Per demostrar que *while* i *for* són totalment equivalents (respecte
	  a la seva funció) realitzatem els exemples anteriors pel bucle
	  *while*. 


	  .. code-block:: python
			  
	  	>>> ll = [2, 3, 4, 's']
		>>> i = 0
		>>> while i < len(ll):
		...     p = ll[i] # O bé directament print ll[i]
		...     print p,
		...     i += 1
		...
		2 3 4 s
		>>> i = 0
		>>> while i < 5:
		...     if i % 2 == 0:
                ...        print i,
		...     else:
		...        print '@',
		...     i += 1
		...
		0 @ 2 @ 4
