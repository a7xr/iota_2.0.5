# coding=utf-8
from __future__ import absolute_import, division, print_function, \
  unicode_literals

from csv import DictReader
from os.path import dirname, join
from random import randrange
from unittest import TestCase

from sha3 import keccak_384

from iota.crypto.kerl import Kerl
from iota.crypto.kerl.conv import convertToBytes, convertToTrits, \
  trits_to_trytes, trytes_to_trits
from pack001 import *

class TestKerl(TestCase):
    def test_correct_hash_function(self):
        k = keccak_384()
        print_var_type_n_val(var001 = k, pointer = "#YTRFGDFGHDFGHFDGH")#YTRFGDFGHDFGHFDGH
# Value: 
# # <_pysha3.keccak_384 object at 0x0000018FAA5536F8>

# Type: <class '_pysha3.keccak_384'>
        # print('k001: ', k)
        # # <_pysha3.keccak_384 object at 0x0000028B370AF600>
        k.update('Message'.encode('utf-8'))
        print_var_type_n_val(var001 = k, pointer = "#SDFGHytre2345cd345")#SDFGHytre2345cd345
# Value: 
# # <_pysha3.keccak_384 object at 0x0000018FAA5536F8>

# Type: <class '_pysha3.keccak_384'>
        # print('k_update: ', k)
        # # <_pysha3.keccak_384 object at 0x0000028B370AF600>

        self.assertEqual(
          k.hexdigest(), # <<<<<<<<<<<<<<<

          '0c8d6ff6e6a1cf18a0d55b20f0bca160d0d1c914a5e842f3'
          '707a25eeb20a279f6b4e83eda8e43a67697832c7f69f53ca',
        )

    def test_correct_first(self):
        # noinspection SpellCheckingInspection
        inp = (
          'EMIDYNHBWMBCXVDEFOFWINXTERALUKYYPPHKP9JJ'
          'FGJEIUY9MUDVNFZHMMWZUYUSWAIOWEVTHNWMHANBH'
        )

        trits = trytes_to_trits(inp)
        print_var_type_n_val(var001 = trits, pointer = "#SDFGHhgfdAZER1234765555")#SDFGHhgfdAZER1234765555
# Value: 
# # [-1, -1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, -1, 0, -1, -1, -1, -1, 0, 1, -1, 1, 0, -1, -1, 0, 1, 1, 1, -1, 1, 0, 0, 1, 0, 0, -1, 0, 1, 1, -1, 1, 1, 0, -1, -1, 1, 0, -1, 1, 0, -1, -1, 0, -1, 1, -1, -1, 0, 0, 0, 1, -1, -1, -1, 0, -1, 0, -1, 1, -1, -1, -1, 1, 0, 0, -1, 1, 0, 0, 0, 1, 1, 0, 1, -1, -1, 1, 1, 1, -1, 0, 1, -1, 0, 1, -1, -1, 1, -1, -1, -1, 0, 1, -1, 1, 1, 1, -1, -1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, -1, 1, 1, -1, 1, 1, 0, 1, -1, -1, 1, 0, 0, 1, 0, 1, -1, 1, -1, 0, 0, 0, 0, 1, 1, 1, 0, 1, -1, 1, 1, 0, 1, 1, -1, -1, -1, -1, 0, -1, 1, -1, 0, 0, -1, 0, 1, 1, 1, 1, 1, 1, 1, -1, -1, 0, -1, 0, 0, 0, 1, -1, 1, -1, 0, 0, 1, -1, 1, 0, -1, -1, -1, 0, 1, 0, 0, 0, 0, 1, 0, -1, -1, -1, -1, 0, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1, 0, 1, -1, -1, -1, -1, -1, 0, 1, 1, 1, -1, 0, 1, 1, 0, 0, -1, -1, -1, -1, 1, 0, -1, 0, 1]

# Type: <class 'list'>
        # print('trits001: ', trits)
        # # [-1, -1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, -1, 0, -1, -1, -1, -1, 0, 1, -1, 1, 0, -1, -1, 0, 1, 1, 1, -1, 1, 0, 0, 1, 0, 0, -1, 0, 1, 1, -1, 1, 1, 0, -1, -1, 1, 0, -1, 1, 0, -1, -1, 0, -1, 1, -1, -1, 0, 0, 0, 1, -1, -1, -1, 0, -1, 0, -1, 1, -1, -1, -1, 1, 0, 0, -1, 1, 0, 0, 0, 1, 1, 0, 1, -1, -1, 1, 1, 1, -1, 0, 1, -1, 0, 1, -1, -1, 1, -1, -1, -1, 0, 1, -1, 1, 1, 1, -1, -1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, -1, 1, 1, -1, 1, 1, 0, 1, -1, -1, 1, 0, 0, 1, 0, 1, -1, 1, -1, 0, 0, 0, 0, 1, 1, 1, 0, 1, -1, 1, 1, 0, 1, 1, -1, -1, -1, -1, 0, -1, 1, -1, 0, 0, -1, 0, 1, 1, 1, 1, 1, 1, 1, -1, -1, 0, -1, 0, 0, 0, 1, -1, 1, -1, 0, 0, 1, -1, 1, 0, -1, -1, -1, 0, 1, 0, 0, 0, 0, 1, 0, -1, -1, -1, -1, 0, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1, 0, 1, -1, -1, -1, -1, -1, 0, 1, 1, 1, -1, 0, 1, 1, 0, 0, -1, -1, -1, -1, 1, 0, -1, 0, 1]
        kerl = Kerl()
        kerl.absorb(trits)
        # print('kerl001: ', kerl)
        # # <iota.crypto.kerl.pykerl.Kerl object at 0x000002740CFA5BA8>
        trits_out = []
        kerl.squeeze(trits_out)
        # print('kerl002: ', kerl)
        # # <iota.crypto.kerl.pykerl.Kerl object at 0x000002740CFA5BA8>

        trytes_out = trits_to_trytes(trits_out)
        print_var_type_n_val(var001 = trytes_out, pointer = "#QSEZEzZERTYsder23434")#QSEZEzZERTYsder23434
# Value: EJEAOOZYSAWFPZQESYDHZCGYNSTWXUMVJOVDWUNZJXDGWCLUFGIMZRMGCAZGKNPLBRLGUNYWKLJTYEAQX
# Type: <class 'str'>

        # noinspection SpellCheckingInspection
        self.assertEqual(
          trytes_out,

          'EJEAOOZYSAWFPZQESYDHZCGYNSTWXUMVJOVDWUNZ'
          'JXDGWCLUFGIMZRMGCAZGKNPLBRLGUNYWKLJTYEAQX',
        )

    def test_output_greater_243(self):
        # noinspection SpellCheckingInspection
        inp = (
          '9MIDYNHBWMBCXVDEFOFWINXTERALUKYYPPHKP9JJ'
          'FGJEIUY9MUDVNFZHMMWZUYUSWAIOWEVTHNWMHANBH'
        )

        trits = trytes_to_trits(inp)
        print_var_type_n_val(var001 = trits, pointer = "#XCVBNbvcSDF23458765")#XCVBNbvcSDF23458765
# Value: 
# # [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, -1, 0, -1, -1, -1, -1, 0, 1, -1, 1, 0, -1, -1, 0, 1, 1, 1, -1, 1, 0, 0, 1, 0, 0, -1, 0, 1, 1, -1, 1, 1, 0, -1, -1, 1, 0, -1, 1, 0, -1, -1, 0, -1, 1, -1, -1, 0, 0, 0, 1, -1, -1, -1, 0, -1, 0, -1, 1, -1, -1, -1, 1, 0, 0, -1, 1, 0, 0, 0, 1, 1, 0, 1, -1, -1, 1, 1, 1, -1, 0, 1, -1, 0, 1, -1, -1, 1, -1, -1, -1, 0, 1, -1, 1, 1, 1, -1, -1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, -1, 1, 1, -1, 1, 1, 0, 1, -1, -1, 1, 0, 0, 1, 0, 1, -1, 1, -1, 0, 0, 0, 0, 1, 1, 1, 0, 1, -1, 1, 1, 0, 1, 1, -1, -1, -1, -1, 0, -1, 1, -1, 0, 0, -1, 0, 1, 1, 1, 1, 1, 1, 1, -1, -1, 0, -1, 0, 0, 0, 1, -1, 1, -1, 0, 0, 1, -1, 1, 0, -1, -1, -1, 0, 1, 0, 0, 0, 0, 1, 0, -1, -1, -1, -1, 0, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1, 0, 1, -1, -1, -1, -1, -1, 0, 1, 1, 1, -1, 0, 1, 1, 0, 0, -1, -1, -1, -1, 1, 0, -1, 0, 1]

# Type: <class 'list'>

        kerl = Kerl()
        print_var_type_n_val(var001 = kerl, pointer = "#SDFG345tredff")#SDFG345tredff
# Value: 
# # <iota.crypto.kerl.pykerl.Kerl object at 0x0000018FAA7C6780>

# Type: <class 'iota.crypto.kerl.pykerl.Kerl'>
        kerl.absorb(trits)
        print_var_type_n_val(var001 = kerl, pointer = "#ERERdfgfdrtre2345665777")#ERERdfgfdrtre2345665777
# Value: 
# # <iota.crypto.kerl.pykerl.Kerl object at 0x0000018FAA7C6780>

# Type: <class 'iota.crypto.kerl.pykerl.Kerl'>
        trits_out = []
        kerl.squeeze(trits_out, length=486)
        print_var_type_n_val(var001 = kerl, pointer = "#2345gDFRER")#2345gDFRER
# Value: 
# # <iota.crypto.kerl.pykerl.Kerl object at 0x0000018FAA7C6780>

# Type: <class 'iota.crypto.kerl.pykerl.Kerl'>

        trytes_out = trits_to_trytes(trits_out)
        print_var_type_n_val(var001 = trytes_out, pointer = "#23458765SDFfffFGH")#23458765SDFfffFGH
# Value: G9JYBOMPUXHYHKSNRNMMSSZCSHOFYOYNZRSZMAAYWDYEIMVVOGKPJBVBM9TDPULSFUNMTVXRKFIDOHUXXVYDLFSZYZTWQYTE9SPYYWYTXJYQ9IFGYOLZXWZBKWZN9QOOTBQMWMUBLEWUEEASRHRTNIQWJQNDWRYLCA
# Type: <class 'str'>
        # noinspection SpellCheckingInspection
        self.assertEqual(
          trytes_out,

          'G9JYBOMPUXHYHKSNRNMMSSZCSHOFYOYNZRSZMAAYWDYEIMVVOGKPJB'
          'VBM9TDPULSFUNMTVXRKFIDOHUXXVYDLFSZYZTWQYTE9SPYYWYTXJYQ'
          '9IFGYOLZXWZBKWZN9QOOTBQMWMUBLEWUEEASRHRTNIQWJQNDWRYLCA',
        )

    def test_input_greater_243(self):
        # noinspection SpellCheckingInspection
        inp = (
          'G9JYBOMPUXHYHKSNRNMMSSZCSHOFYOYNZRSZMAAYWDYEIMVVOGKPJB'
          'VBM9TDPULSFUNMTVXRKFIDOHUXXVYDLFSZYZTWQYTE9SPYYWYTXJYQ'
          '9IFGYOLZXWZBKWZN9QOOTBQMWMUBLEWUEEASRHRTNIQWJQNDWRYLCA'
        )

        trits = trytes_to_trits(inp)

        kerl = Kerl()
        kerl.absorb(trits)
        trits_out = []
        kerl.squeeze(trits_out, length=486)

        trytes_out = trits_to_trytes(trits_out)

        # noinspection SpellCheckingInspection
        self.assertEqual(
          trytes_out,

          'LUCKQVACOGBFYSPPVSSOXJEKNSQQRQKPZC9NXFSMQNRQCGGUL9OHVV'
          'KBDSKEQEBKXRNUJSRXYVHJTXBPDWQGNSCDCBAIRHAQCOWZEBSNHIJI'
          'GPZQITIBJQ9LNTDIBTCQ9EUWKHFLGFUVGGUWJONK9GBCDUIMAYMMQX',
        )


    def test_all_bytes(self):
        for i in range(-128, 128):
            in_bytes = [i] * 48
            trits = convertToTrits(in_bytes)
            out_bytes = convertToBytes(trits)

            self.assertEqual(in_bytes, out_bytes)

    def test_random_trits(self):
        in_trits = [randrange(-1,2) for _ in range(243)]
        print(in_trits)
        input('stop vet2')
        in_trits[242] = 0
        in_bytes = convertToBytes(in_trits)
        out_trits = convertToTrits(in_bytes)

        self.assertEqual(in_trits, out_trits)

    def test_generate_trytes_hash(self):
        filepath =\
          join(
            dirname(__file__),
            'test_vectors/generate_trytes_and_hashes.csv',
          )

        with open(filepath,'r') as f:
            reader = DictReader(f)
            for count, line in enumerate(reader):
                trytes = line['trytes']
                hashes = line['Kerl_hash']

                trits = trytes_to_trits(trytes)

                kerl = Kerl()
                kerl.absorb(trits)
                trits_out = []
                kerl.squeeze(trits_out)

                trytes_out = trits_to_trytes(trits_out)

                self.assertEqual(
                  hashes,
                  trytes_out,

                  msg =
                    'line {count}: {hashes} != {trytes}'.format(
                      count = count + 2,
                      hashes = hashes,
                      trytes = trytes_out,
                    ),
                )

    def test_generate_multi_trytes_and_hash(self):
        filepath =\
          join(
            dirname(__file__),
            'test_vectors/generate_multi_trytes_and_hash.csv',
          )

        with open(filepath,'r') as f:
            reader = DictReader(f)
            for count, line in enumerate(reader):
                trytes = line['multiTrytes']
                hashes = line['Kerl_hash']

                trits = trytes_to_trits(trytes)

                kerl = Kerl()
                kerl.absorb(trits)
                trits_out = []
                kerl.squeeze(trits_out)

                trytes_out = trits_to_trytes(trits_out)

                self.assertEqual(
                  hashes,
                  trytes_out,

                  msg =
                    'line {count}: {hashes} != {trytes}'.format(
                      count = count + 2,
                      hashes = hashes,
                      trytes = trytes_out,
                    ),
                )

    def test_generate_trytes_and_multi_squeeze(self):
        filepath =\
          join(
            dirname(__file__),
            'test_vectors/generate_trytes_and_multi_squeeze.csv',
          )

        with open(filepath,'r') as f:
            reader = DictReader(f)
            for count, line in enumerate(reader):
                trytes = line['trytes']
                hashes1 = line['Kerl_squeeze1']
                hashes2 = line['Kerl_squeeze2']
                hashes3 = line['Kerl_squeeze3']

                trits = trytes_to_trits(trytes)
                # print(trits)
                # # [-1, 0, 1, 1, -1, 0, -1, 0, 0, 1, -1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, -1, -1, 1, -1, -1, -1, -1, 0, -1, 1, -1, 0, -1, 0, 1, 0, 1, 1, 0, 1, -1, 0, 0, -1, 1, 0, 1, -1, -1, 0, 1, 1, 0, 0, 1, 0, -1, -1, 0, 0, -1, 0, 0, -1, 0, 1, 1, 0, 0, 0, 0, -1, 0, -1, 1, -1, -1, -1, 0, 0, 1, 0, 0, 1, 1, -1, 1, 1, -1, 0, 1, -1, 1, 0, -1, 1, 0, 1, 1, -1, 0, 1, 0, 1, 1, -1, -1, -1, 1, 1, 1, -1, 0, 1, -1, 0, -1, -1, -1, -1, 1, 0, 0, 0, -1, -1, -1, -1, -1, -1, 0, 1, -1, -1, -1, 0, 1, 1, 0, -1, -1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, -1, 1, 0, -1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 0, -1, 1, 1, -1, 1, 0, 0, 0, 1, 1, 1, -1, -1, 0, 0, -1, -1, 1, -1, -1, 0, -1, -1, 1, 0, 0, 1, 1, -1, -1, 1, 1, -1, -1, 0, 1, 1, 1, -1, -1, -1, 0, -1, -1, -1, -1, 0, 1, 1, 1, -1, -1, 0, 0, 1, 0, -1, 0, 1, -1, 0, -1, 1, -1, 1, -1, -1, -1, 0, 0, 1, 1, 0, 1, 0]
                kerl = Kerl()
                kerl.absorb(trits)

                trits_out = []
                kerl.squeeze(trits_out)
                trytes_out = trits_to_trytes(trits_out)

                # print('hashes1: ', hashes1)
                # # IWDWJCUUE9EBBYAEDXPDNAKTJAVY9IFOUZBNRIHMZ9NWOGOL9GYKZZ9ZLXHAI9PVPSLEAUGX9TQKMIUAX
                # print('trytes_out: ', trytes_out)
                # # IWDWJCUUE9EBBYAEDXPDNAKTJAVY9IFOUZBNRIHMZ9NWOGOL9GYKZZ9ZLXHAI9PVPSLEAUGX9TQKMIUAX


                self.assertEqual(
                  hashes1,
                  trytes_out,

                  msg =
                    'line {count}: {hashes} != {trytes}'.format(
                      count = count + 2,
                      hashes = hashes1,
                      trytes = trytes_out,
                    ),
                )

                trits_out = []
                kerl.squeeze(trits_out)
                trytes_out = trits_to_trytes(trits_out)

                # print('line {count}: {hashes} != {trytes}'.format(
                #       count = count + 2,
                #       hashes = hashes2,
                #       trytes = trytes_out,
                #     ))
                # # ANLYSAFQ9RJKFEADAZDTLPMYCYSGTRIOUWFKZPWJIEQHDTREOPHSUMAGIZLVIRMZGAVKODZAYBUISSQNX != ANLYSAFQ9RJKFEADAZDTLPMYCYSGTRIOUWFKZPWJIEQHDTREOPHSUMAGIZLVIRMZGAVKODZAYBUISSQNX

                self.assertEqual(
                  hashes2,
                  trytes_out,

                  msg =
                    'line {count}: {hashes} != {trytes}'.format(
                      count = count + 2,
                      hashes = hashes2,
                      trytes = trytes_out,
                    ),
                )

                trits_out = []
                kerl.squeeze(trits_out)
                trytes_out = trits_to_trytes(trits_out)

                self.assertEqual(
                  hashes3,
                  trytes_out,

                  msg =
                    'line {count}: {hashes} != {trytes}'.format(
                      count = count + 2,
                      hashes = hashes3,
                      trytes = trytes_out,
                    ),
                )
