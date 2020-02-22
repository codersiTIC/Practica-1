# -*- encoding: utf-8 -*-

from transf import *

def split_digits(img):

	'''
	Aquesta funció rebrà una imatge img en blanc i negre retallada
	verticalment i retorna una tupla (D,R) en la que D és una imatge
	amb el dígit de més a l'esquerra i R és la resta de la imatge. La
	imatge corresponent al dígit extret D es retorna convenientment
	retallada en la direcció horitzontal. La resta R esdevé una imatge
	nul·la quan s'han extret tots el dígits.
	'''

	if mode(img) == 'RGB':
		img = TransMatrix(trim(img))


	else:
		img = L_to_bn(img)
		img = TransMatrix(img)

	D = []
	R = []
	index = 0

	for col in img:
		c = 0
		for pixel in col:
			if pixel == 255:
				c += 1

		if c != len(col):
			D.append(col)

		else:
			break

		index += 1

	R = img[index:]
	if R == []:
		R = null() # Segons el que diu el pdf

	else:
		R = whiteElim(R)
		R = ('1', R)
		R = TransMatrix(R)
		#matrix2img(R,'R.jpeg','1')

	D = ('1', D)
	D = TransMatrix(D)
	#matrix2img(D,'D.jpeg','1')

	return (D, R)


def get_digits(img):

	j = 0
	for lletra in img:
		if lletra == '.':
			break
		j += 1

	tuple = split_digits(img)
	first_digit = tuple[0]
	next_digit = tuple[1]
	matrix2img(first_digit, 'D1.jpeg', '1')
	matrix2img(next_digit, 'R1.jpeg', '1')

	i = 1
	while True:
		tuple = split_digits('R'+str(i)+'.jpeg')
		matrix2img(tuple[0], ('D'+str(i+1)+'.jpeg'), '1')
		os.remove('R'+str(i)+'.jpeg')
		i += 1
		if tuple[1] == null():
			return (i) # per saber quans digits
			break

		matrix2img(tuple[1], ('R'+str(i)+'.jpeg'), '1')

	# matrix2img(n[0], 'hola'+str(i)+'.jpeg')
	#split_digit_L = split_digit_rgb == -> (D,R)


if __name__ == '__main__':
	get_digits('m1.jpeg')
	#split_digits('m3.jpeg')
	#split_digit_rgb('R.jpeg')
	#print split_digit_L('R2.jpeg')
	#get_digits('m1.jpeg')
	#L_to_bn ('R.jpeg')
