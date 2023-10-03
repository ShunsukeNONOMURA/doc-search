import logging
import os

import jaconv
from sentence_transformers import SentenceTransformer


class TextEncoder:
    def __init__(self, model_path=None):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.NullHandler()
        handler.setLevel(logging.DEBUG)
        self.logger.addHandler(handler)
        self.model = SentenceTransformer('stsb-xlm-r-multilingual')
        # self.model = SentenceTransformer('./pytorch_model.bin')

    def encode(self, text, normalize=True):
        if normalize:
            text = jaconv.normalize(text, "NFKC")

        vector = self.model.encode(text)
        self.logger.debug(vector.shape)

        return vector
