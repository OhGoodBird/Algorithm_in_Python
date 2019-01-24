#!/bin/env python3

import os
import numpy as np


class MNIST_Loader():
'''
    Load MNIST dataset (http://yann.lecun.com/exdb/mnist/)
'''
    
    def __init__(self, path='.'):
        self.path = path
    
    def load_imgs(self, file_path):
        with open(file_path, 'rb') as fp:
            fp.read(4)  # skip magic number
            num_img = int.from_bytes(fp.read(4), byteorder='big')
            rows = int.from_bytes(fp.read(4), byteorder='big')
            cols = int.from_bytes(fp.read(4), byteorder='big')
            size = rows * cols
            buf = fp.read(rows * cols * num_img)
            imgs = np.frombuffer(buf, dtype=np.uint8)
            imgs = imgs.reshape(num_img, rows, cols)
        return imgs
        
    def load_labels(self, file_path):
        with open(file_path, 'rb') as fp:
            fp.read(4)  # skip magic number
            num_target = int.from_bytes(fp.read(4), byteorder='big')
            buf = fp.read(num_target)
            targets = np.frombuffer(buf, dtype=np.uint8)
            targets = targets.reshape(num_target)
        return targets
        
    def load(self):
        train_imgs = self.load_imgs(os.path.join(self.path, 'train-images-idx3-ubyte'))
        train_labels = self.load_labels(os.path.join(self.path, 'train-labels-idx1-ubyte'))
        test_imgs = self.load_imgs(os.path.join(self.path, 't10k-images-idx3-ubyte'))
        test_labels = self.load_labels(os.path.join(self.path, 't10k-labels-idx1-ubyte'))
        return train_imgs, train_labels, test_imgs, test_labels
        
        
def main():
    loader = MNIST_Loader()
    train_imgs, train_labels, test_imgs, test_labels = loader.load()
    print(len(train_imgs))
    print(len(train_labels))
    print(len(test_imgs))
    print(len(test_labels))

if(__name__ == '__main__'):
    main()
    
