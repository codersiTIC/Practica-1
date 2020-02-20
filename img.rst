
Mòdul *img*
-----------

The module *img* contain the structural functions of the project (the simpliest
elements of it), which are able to, for example, control the Image's format,
create new ones, encode a picture into a matrix...

This are the list of all of it:

.. function:: null()

   Returns an empty image: ('NULL', None)

   :returns: The null image
   :rtype: Tuple: ('NULL', None)


.. function:: is_null(img)

   Checks if an image (Type, Matrix) is null

   :param a: An image (Type, Matrix)
   :type a: tuple
   :returns: True (if it is null) or False (if not)
   :rtype: bool

.. function:: white_rgb(w,h)

   Returns an image in RGB format with all white pixel and size w * h	 

   :param w: The width of the new image
   :type w: int
   :param h: The height of the new image
   :type h: int
   :returns: An all white new image (w * h)
   :rtype: tuple, ('RGB', Matrix)
	   
.. function:: white_grey(w,h)

   Returns an image in grey format ('L') with all white pixels and size w * h

   :param w: The width of the new image
   :type w: int
   :param h: The height of the new image
   :type h: int
   :returns: An all white new image (w * h)
   :rtype: tuple, ('L', Matrix)

.. function:: white_bn(w,h)

   Returns an image in black and white ('1') with all white pixels and size w*h

   :param w: The width of the new image
   :type w: int
   :param h: The height of the new image
   :type h: int
   :returns: An all white new image (w * h)
   :rtype: tuple, ('1', Matrix)

.. function:: format(img)

   Returns the image format

   :param: An image (Type, Format)
   :type: tuple
   :returns: The image format
   :rtype: str

.. function:: mode(img)

   Returns the image mode

   :param: An image (Type, Format)
   :type: tuple
   :returns: The image mode
   :rtype: str

