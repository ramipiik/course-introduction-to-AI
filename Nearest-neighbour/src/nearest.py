import math
import os
import numpy as np
from PIL import Image
import random

NUMBER_OF_PIXELS = 28 * 28
IMAGE_SIZE = 28


def get_chars(filename):
    """
    Reads the classes of characters
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))

    try:
        with open(os.path.join(dir_path, '..', filename)) as file:
            chars = [line[0] for line in file]

        return chars

    except FileNotFoundError:
        print("File %s was not found." % filename)
        raise
    except Exception as e:
        print("Something terrible happened: %s", str(e))
        raise


def get_images(filename):
    """
    Reads the images (black pixel is 1, white pixel is 0 in the input)
    Trasnforms (0, 1) values to (-1.0, 1.0)
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    vectors = []

    try:
        with open(os.path.join(dir_path, '..', filename)) as file:
            for line in file:
                vectors.append([1.0 if float(v) == 1 else -1.0 for v in line.strip().split(',')])

        return vectors

    except FileNotFoundError:
        print("File %s was not found." % filename)
        raise
    except Exception as e:
        print("Something terrible happened: %s", str(e))
        raise


class Nearest:
    """ Perceptron
        :attr data: list of objects that represent images
    """

    def __init__(self, images, chars):
        idata = get_images(images)
        cdata = get_chars(chars)

        self.data = [{'vector': v, 'char': c} for (v, c) in zip(idata, cdata)]
        random.seed()

    def training_data(self, steps):
        self.training_data = self.data[:steps]

    def test(self, target_char, opposite_char, steps):
        success = 0
        examples = self.data[steps:]

        # examples = [e for e in examples if e['char'] in (target_char, opposite_char)]

        for e in examples:
            lowest_dist = 784
            nearest_neighbour='x'
            for t in self.training_data:
                dist=np.subtract(t['vector'], e['vector'])
                dist=[abs(d) for d in dist]
                sum_dist=sum(dist)
                if sum_dist<lowest_dist:
                    lowest_dist=sum_dist
                    nearest_neighbour=t['char']   
            if (e['char'] == nearest_neighbour):
                success += 1
            # print ("lowest_dist", lowest_dist)
            # print("nearest_neighbour", nearest_neighbour)
        print("successes", success)
        print("examples", len(examples))
        return float(success) / len(examples)
