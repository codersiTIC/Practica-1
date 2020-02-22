# -*- encoding: utf-8 -*-

from PIL import Image
from img import *

def read_rgb(nomf):
    """
    Donat un nom de fitxer corresponent a una imatge RGB la llegeix
    i torna la imatge corresponent
    """
    image = Image.open(nomf)
    pix = image.load()
    X = image.size[0]
    Y = image.size[1]
    data=[]
    for y in range(Y):
        fila=[]
        for x in range(X):
            fila+=[pix[x,y]]
        data+=[fila]

    return img(data, 'RGB')


def read_bn(nomf):
    """
    Donat un nom d'arxiu corresponent a una imatge en blanc i negre,
    retorna la matriu d'imatge. Cada pixel serà 0 o 255.
    """
    image = Image.open(nomf).convert('1')
    pix = image.load()
    X = image.size[0]
    Y = image.size[1]
    data = [[pix[x,y] for x in range(X)] for y in range(Y)]
    return img(data, '1')


def show(i):
    """
    Donada una imatge, la mostra en un visualitzador a la terminal.
    Principalment serveix per a depurar el projecte.
    """
    image = Image.new(mode(i),(get_w(i),get_h(i)))
    image.putdata([pixel for F in matrix(i) for pixel in F])
    image.show()


def save(i,nomf):
    """
    Donada una imatge i un nom de fitxer, crea el fitxer imatge a
    partir de la matriu.
    """
    image = Image.new(mode(i),(get_w(i),get_h(i)))
    image.putdata([pixel for F in matrix(i) for pixel in F])
    image.save(nomf)


def matrix2img(D, name, mode):
    resultat = Image.new(mode,(len(D[0]), len(D)))
    resultat.putdata([pixel for F in D for pixel in F])
    resultat.save(name)


if __name__ == '__main__':
    print read_rgb("Patro_A.jpge")
    # save('blanc1.jpeg', 'hola')
    #white_rgb(2,2)
    #white_grey(2,2)
    #white_bn(2,2)
    #print matrix('blanc1.jpeg')
    #print matrix('blancL.jpeg')
    #print matrix('blancRGB.jpeg')
    #show('blanc1.jpeg')
    #show('blancL.jpeg')
    #show('blancRGB.jpeg')
    #show('rainbow.jpg')
    save ('rainbow.jpeg', ' marcel.jpeg')
