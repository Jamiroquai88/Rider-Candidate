#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Phonexia
# Author: Jan Profant <jan.profant@phonexia.com>
# All Rights Reserved


class ABCTransformation(object):
    """ Abstract class for data transformations. """

    def transform(self, data):
        """ Perform transformation on input data.

        Args:
            data (numpy.array): input data

        Returns:
            numpy.array: transformed data
        """
        raise NotImplementedError
