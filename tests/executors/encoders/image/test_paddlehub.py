import unittest

from jina.executors.encoders.image.paddlehub import ImagePaddlehubEncoder
from . import ImageTestCase


class MyTestCase(ImageTestCase):
    def _get_encoder(self):
        self.target_output_dim = 2048
        self.input_dim = 224
        return ImagePaddlehubEncoder(on_gpu=True)


if __name__ == '__main__':
    unittest.main()
