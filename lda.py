#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Phonexia
# Author: Jan Profant <jan.profant@phonexia.com>
# All Rights Reserved

from abc_transform import ABCTransformation


class LDA(ABCTransformation):
    """ Linear Discriminant Analysis """

    model = None

    def __init__(self, model_path):
        # load model from file to variable model
        pass

    def transform(self, data):
        """ Perform LDA transformation on input data - dot product with model.

            Args:
                data (numpy.array): input data

            Returns:
                numpy.array: transformed data
        """
        pass