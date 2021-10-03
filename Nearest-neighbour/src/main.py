from nearest import Nearest

IMGS_FILE = 'mnist-x.data'
CHARS_FILE = 'mnist-y.data'


def main():
    """
    Implement the perceptron algorithm in the Perceptron class. After that you can try out the
    values of different number pairs by changing the values of the 'target_char' and
    'opposite_char' variables.
    """
    near = Nearest(IMGS_FILE, CHARS_FILE)
    near.train('1', '5', 5000)
    print(near.test('1', '5'))
    near.save_weights('weights.bmp')


if __name__ == '__main__':
    main()
