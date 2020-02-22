# -*- encoding: utf-8 -*-

from discret import *

def vtrim(img):
    """
    Returns vertical trimmed image
    >>> vtrim(('1',[[255,255,0],[255,0,255],[0,255,255]]))
    ('1', [[255, 255, 0], [255, 0, 255], [0, 255, 255]])
    >>> vtrim(('1',[[255,255,255],[255,0,255],[0,255,255]]))
    ('1', [[255, 0, 255], [0, 255, 255]])
    """
    new_m = []

    for element in img[1]:
        c = 0
        for pixel in element:
            if pixel == 255:
                c += 1

        if c != len(element):
            new_m.append(element)

    #matrix2img(new_m,'vtrim.jpeg', '1')
    return ('1',new_m)


def TransMatrix(img):
    #Creació matriu per columnes
    n = 0
    new_m = []
    img_transposed = []
    while True:
        for element in img[1]:

            new_m.append(element[n])

        img_transposed.append(new_m)
        n += 1
        new_m = []

        if n == len(element):
            break

    return img_transposed


def whiteElim(img_transposed):
    #Eliminació part blanca de l'esquerra
    index = 0
    c = 0
    for col in img_transposed:
        index += 1
        for pixel in col:
            if pixel == 255:
                c += 1

        if c != len(col):

            del img_transposed[:index]
            break

        c = 0

    return img_transposed


def rotateMatrix(img_transposed):
    new_m = []
    n = len(img_transposed)-1

    for element in range(len(img_transposed)):
        new_m.append(img_transposed[n])

        n -= 1

        if n < 0:
            break

    return new_m

def htrim(img):

    img = rotateMatrix(whiteElim(rotateMatrix(whiteElim(TransMatrix(img)))))
    img = ('1', img)
    img = TransMatrix(img)
    #matrix2img(img[1],'htrim.jpeg', '1')

    return ('1',img)



def trim(img):

    img = vtrim(htrim(rgb_to_bn(img)))
    
    #matrix2img(img[1],'trim.jpeg', '1')

    return img



def scale(img, h):
    """
    Scale image img taking into account height h preserving ratio aspect

    El pixel de coordenades (a, b) de la imatge escalada es projecta sobre el pixel
    (a*fh, b*fh) de la imatge original.

    >>> scale(('RGB', [[(255, 255, 255), (255, 255, 255), (255, 255, 255)], [(255, 255, 255),(255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255)]]), 2)
    ('RGB', [[(255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255)]])
    >>> scale(('RGB', [[(0, 0, 0), (255, 255, 255), (255, 0, 0)], [(255, 255, 255), (0, 255, 0),(255, 255, 255)], [(0, 0, 255), (255, 255, 255), (255, 255, 255)]]), 2)
    ('RGB', [[(0, 0, 0), (255, 0, 0)], [(0, 0, 255), (255, 255, 255)]])
    """

    H = get_h(img)
    W = get_w(img)
    m = matrix(img)

    fh = float(H) / h
    w = int(W / fh)


    if fh == 1:
        #save(img, 'scale_'+img)
        return (mode(img), m)

    else:
        #if H < h:
        new_m = []
        for x in range(h):
            f =[]
            for y in range(w):
                f.append(m[int(x*fh)][int(y*fh)])
            new_m.append(f)

        #matrix2img(new_m, img, mode(img))
        return (mode(img), new_m)


if __name__ =='__main__':
    scale('anass.jpeg', 1080)
    #trim('m4.jpeg')
