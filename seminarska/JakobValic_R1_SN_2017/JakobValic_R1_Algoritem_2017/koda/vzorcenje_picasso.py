import cv2
import random
from numpy import array, array_equal
import numpy as np
import time

ime_slike = 'picasso.jpg'
picasso = cv2.imread(ime_slike)


def pokaziSliko(picasso):

    cv2.imshow(ime_slike, picasso)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def nakljucna_izbira(slika, verjetnost):
    """
    Vrni sliko, na kateri je določen procent pikslov izbranih. Če želimo matriko
    risati, neizbrane piksle predstavimo z belo barvo. V obratnem primeru jih
    predstavimo z None.
    :param slika: Matrika vrstic, v kateri so piksli oblike [r, g, b]
    :param verjetnost: Kolikšen delež vzorčnih pikslov želimo imeti.
    :return:
    """
    for i, vrstica in enumerate(slika):
        for j, pixel in enumerate(vrstica):
            # Piksle, ki ne spadajo v vejetnost, pobarvamo v belo
            if random.randint(1, 100) > verjetnost:
                slika[i][j] = [255, 255, 255]
    return slika

def izracunaj_povprecje(obmocje_pikslov):
    """
    Izračuna povprečje pikslov v pravokotnem območju.
    :param kvadrat_pikslov:
    :return: En piksel oblike [r, g, b].
    """
    vsota = array([0, 0, 0])
    counter = 0
    for vr in obmocje_pikslov:
        for piksel in vr:
            if not array_equal(piksel, array([255, 255, 255])):
                vsota += piksel
                #print(vsota)
                counter += 1
    if counter:
        rezultat = vsota//counter
    else:
        return array([255, 255, 255], dtype='uint8') # Zaradi možnega presežka definicijskega območja
    return array(rezultat, dtype='uint8')


def vrni_obmocja_slike(slika, faktor):
    """Vrne zmanjšano in enako veliko sliko z manj različnimi piksli."""
    visina, sirina, _ = slika.shape
    manjsa_slika = np.ndarray(shape=(visina, sirina, 3), dtype='uint8')
    enako_velika = np.ndarray(shape=(visina//faktor, sirina//faktor, 3), dtype='uint8')
    for i in range(0, visina - visina%faktor, faktor):
        for j in range(0, sirina - sirina%faktor, faktor):
            obmocje = slika[i:i+faktor,j:j+faktor]
            manjsa_slika[i:i + faktor, j:j + faktor] = izracunaj_povprecje(obmocje)
            enako_velika[i//faktor, j//faktor] = izracunaj_povprecje(obmocje)
    return manjsa_slika, enako_velika


# pokaziSliko(picasso)

for verjetnost_izbranih in [70, 5]:
    t1 = time.time()

    nakljucne_tocke = nakljucna_izbira(picasso, verjetnost=verjetnost_izbranih)
    # pokaziSliko(nakljucne_tocke)

    t2 = time.time()

    print(f'Čas za izbiro naključnih {verjetnost_izbranih}% pikslov: {round(t2-t1, 1)}s')

    enako_velika, manjsa = vrni_obmocja_slike(nakljucne_tocke, 8)

    print(f'Čas za izračun pomanjšane slike: {round(time.time() - t2, 1)} s')

    # pokaziSliko(enako_velika)
    # pokaziSliko(manjsa)

    cv2.imwrite(f'picasso {verjetnost_izbranih}% enako_velika.jpg', enako_velika)
    cv2.imwrite(f'picasso {verjetnost_izbranih}% manjsa.jpg', manjsa)
    cv2.imwrite(f'picasso {verjetnost_izbranih}% izbor_tock.jpg', nakljucne_tocke)
