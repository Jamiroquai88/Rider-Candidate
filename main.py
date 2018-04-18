import argparse


TEST_OUTPUT_FILE = 'test.txt'
TRAIN_OUTPUT_FILE = 'train.txt'


def load_data():
    """ Load input data. """
    pass


def transform_data():
    """ Transform input data as written in documentation. """
    pass


def cluster_data():
    """ Cluster transformed data. """
    pass


def dump_output():
    """ Dump output of clustering to output file. """
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Python clustering of embeddings.')
    parser.add_argument('-i', type=str, required=True, help='path to input embeddings in cPickle format')
    parser.add_argument('-o', type=str, required=True, help='path to output directory')
    parser.add_argument('--lda', type=str, required=False, help='path to LDA model in .npy format')

    args = parser.parse_args()

    load_data()
    transform_data()
    cluster_data()
    dump_output()