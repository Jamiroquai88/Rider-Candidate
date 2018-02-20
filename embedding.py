#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Phonexia
# Author: Jan Profant <jan.profant@phonexia.com>
# All Rights Reserved


class Embedding(object):
    """ Class for basic embedding operations. """

    def __init__(self):
        self.data = None
        self.window_start = None
        self.window_end = None


class EmbeddingSet(object):
    """ Keep embeddings in one set. """

    def __init__(self):
        self.embeddings = []

    def __iter__(self):
        current = 0
        while current < len(self.embeddings):
            yield self.embeddings[current]
            current += 1

    def __getitem__(self, key):
        return self.embeddings[key]

    def __setitem__(self, key, value):
        self.embeddings[key] = value

    def add(self, embedding):
        """ Add embedding to the set.

        Args:
            embedding (Embedding): embedding to be added
        """
        self.embeddings.append(embedding)
