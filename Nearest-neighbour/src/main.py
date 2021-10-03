from nearest import Nearest

IMGS_FILE = 'mnist-x.data'
CHARS_FILE = 'mnist-y.data'


def main():
    near = Nearest(IMGS_FILE, CHARS_FILE)
    near.training_data(5000)
    print(near.test('1', '5', 5000))


if __name__ == '__main__':
    main()
