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

    def train(self, target_char, opposite_char, steps):
        # Implement method
        
        self.weights=784*[0]
        self.training_data = self.data[:steps]
        # self.training_data = [t for t in self.training_data if t['char'] in (target_char, opposite_char)]
        
        # for item in training_data:
        #     for key, value in item.items():
        #         # print("key:", key)
        #         # print("value:",value)
        #         if key=='char':
        #             print(value)
        
        # error=True
        # round=0
        # while error:
        #     round+=1
        #     error=False
        #     for t in training_data:
        #         z = np.dot(t['vector'], self.weights)
        #         if z>=0 and t['char']==opposite_char:
        #             self.weights=np.subtract(self.weights, t['vector'])
        #             error=True
        #         if z<0 and t['char']==target_char:
        #             self.weights=np.add(self.weights, t['vector'])
        #             error=True
        
        # print("learning rounds:", round)

    def test(self, target_char, opposite_char):
        """Tests the learned perceptron with the last 1000 x,y pairs.
        (Note that this only counts those ones that belong either to the plus or minus classes.)

        :param target_char: the target character we are trying to distinguish
        :param opposite_char: the opposite character
        :return: the ratio of correctly classified characters
        """
        success = 0
        examples = self.data[5000:]

        examples = [e for e in examples if e['char'] in (target_char, opposite_char)]

        for e in examples:
            # z = np.dot(e['vector'], self.weights)
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
        return float(success) / len(examples)

    def save_weights(self, filename):
        """Draws a 28x28 grayscale picture of the weights

        :param filename: Name of the file where weights will be saved
        """
        pixels = [.01 + .98 / (1.0 + float(math.exp(-w))) for w in self.weights]

        Image.fromarray(np.array(pixels).reshape(IMAGE_SIZE, IMAGE_SIZE), mode = "L").save(filename)
