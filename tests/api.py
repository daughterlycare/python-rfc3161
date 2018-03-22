import unittest
import os.path

import rfc3161

class Rfc3161(unittest.TestCase):
    PUBLIC_TSA_SERVER = 'https://freetsa.org/tsr'
    CERTIFICATE = os.path.join(os.path.dirname(__file__),
            '../data/freetsa.crt')

    def test_timestamp(self):
        try:
            certificate = open(self.CERTIFICATE,"r",encoding='utf-8')
            value, substrate = rfc3161.RemoteTimestamper(
                    self.PUBLIC_TSA_SERVER, certificate=certificate)(data='xx')
        except rfc3161.TimestampingError:
            return
        self.assertNotEqual(value, None)
        self.assertEqual(substrate, '')
