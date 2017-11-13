from PIL import Image
import numpy as np
import os
import pandas as pd


def get_target(filename):
    """Returns the first 3 letters of filename ie. cat or dog"""
    return os.path.basename(filename)[:3]


def get_label(target):
    """Returns 1 if target is dog and 0 if it's cat"""
    if target == 'dog':
        label = 1
    elif target == 'cat':
        label = 0
    else:
        raise Exception("Can't determine label !")
    return label


def to_grayscale(filename, save_path):
    """converts an image into grayscale and saves it in save_path"""
    img = Image.open(filename).convert('1')
    save_name = '{}_grey.jpg'.format(os.path.basename(filename)[:-4])
    img.save(os.path.join(save_path, save_name))


def convert_images(path, save_path=None):
    """Goes through all files in directory and converts them into grayscale
        images then saves them in (save_path) directory """
    if save_path is None:
        directory = os.path.dirname(path)
        save_path = os.path.join(directory, "{}_preprocessed".format(
            os.path.basename(path)))
        os.makedirs(save_path)
    elif not os.path.isdir(save_path):
        os.makedirs(save_path)
    files = os.listdir(path)
    for f in files:
        filename = os.path.join(path, f)
        print(filename)
        to_grayscale(filename, save_path)


def target_distribution(path):
    """Prints the number of dog and cat pictures in directory"""
    files = os.listdir(path)
    dogs = 0
    cats = 0
    for f in files:
        target = get_target(f)
        if target == 'dog':
            dogs += 1
        elif target == 'cat':
            cats += 1
    print("Cats : {}".format(cats))
    print("Dogs : {}".format(dogs))
