# coding=utf-8
from __future__ import absolute_import, division, print_function, \
  unicode_literals

from pack001 import *
from unittest import TestCase

from iota import Address
from iota.crypto.types import Digest
from iota.multisig.crypto.addresses import MultisigAddressBuilder
from iota.multisig.types import MultisigAddress


class MultisigAddressBuilderTestCase(TestCase):
  """
  Generating values for this test case using the JS lib:

  .. code-block:: javascript

     // Define digests to use to create the multisig addy.
     var digests = ['...', ...];
     ...

     var Multisig = require('./lib/multisig/address.js');

     var addy = new Multisig(digests);
     console.log(addy.finalize());
  """
  # noinspection SpellCheckingInspection
  def setUp(self):
    super(MultisigAddressBuilderTestCase, self).setUp()

    # Define some tryte sequences that we can reuse between tests.
    self.digest_1 =\
      Digest(
        trytes =
          b'FWNEPVJNGUKTSHSBDO9AORBCVWWLVXC9KAMKYYNKPYNJDKSAUURI9ELKOEEYPKVTYP'
          b'CKOCJQESYFEMINIFKX9PDDGRBEEHYYXCJW9LHGWFZGHKCPVDBGMGQKIPCNKNITGMZT'
          b'DIWVUB9PCHCOPHMIWKSUKRHZOJPMAY',

        key_index = 0,
      )

    print_var_type_n_val(var001 = self.digest_1, pointer = "#3456gfdscv7654zer")#3456gfdscv7654zer
# Value: FWNEPVJNGUKTSHSBDO9AORBCVWWLVXC9KAMKYYNKPYNJDKSAUURI9ELKOEEYPKVTYPCKOCJQESYFEMINIFKX9PDDGRBEEHYYXCJW9LHGWFZGHKCPVDBGMGQKIPCNKNITGMZTDIWVUB9PCHCOPHMIWKSUKRHZOJPMAY
# Type: <class 'iota.crypto.types.Digest'>

    self.digest_2 =\
      Digest(
        trytes =
          b'PAIRLDJQY9XAUSKIGCTHRJHZVARBEY9NNHYJ9UI9HWWZXFSDWEZEGDCWNVVYSYDV9O'
          b'HTR9NGGZURISWTNECFTCMEWQQFJ9VKLFPDTYJYXC99OLGRH9OSFJLMEOGHFDHZYEAF'
          b'IMIZTJRBQUVCR9U9ZWTMUXTUEOUBLC',

        key_index = 0,
      )
    print_var_type_n_val(var001 = self.digest_1, pointer = "#234HGFxctr")#234HGFxctr
# Value: FWNEPVJNGUKTSHSBDO9AORBCVWWLVXC9KAMKYYNKPYNJDKSAUURI9ELKOEEYPKVTYPCKOCJQESYFEMINIFKX9PDDGRBEEHYYXCJW9LHGWFZGHKCPVDBGMGQKIPCNKNITGMZTDIWVUB9PCHCOPHMIWKSUKRHZOJPMAY
# Type: <class 'iota.crypto.types.Digest'>

    self.digest_3 =\
      Digest(
        trytes =
          b'KBNYOFY9HJSPBDBFSTIEMYJAAMNOXLVXBDUKJRBUGAPIIZNDARXEWDZRBCIYFQCBID'
          b'HXIQFIDFPNGIFN9DDXQUGYZGDML9ZIELDSVICFUOPWEPCUWEDUFKXKSOZKTSHIMEIR'
          b'HOXKPJFRWWCNYPXR9RI9SMBFSDQFWM',

        key_index = 0,
      )
    print_var_type_n_val(var001 = self.digest_3, pointer = "#3456gfdCVByt")#3456gfdCVByt
# Value: KBNYOFY9HJSPBDBFSTIEMYJAAMNOXLVXBDUKJRBUGAPIIZNDARXEWDZRBCIYFQCBIDHXIQFIDFPNGIFN9DDXQUGYZGDML9ZIELDSVICFUOPWEPCUWEDUFKXKSOZKTSHIMEIRHOXKPJFRWWCNYPXR9RI9SMBFSDQFWM
# Type: <class 'iota.crypto.types.Digest'>
  def test_success_multiple_digests(self):
    """
    Generating a multisig address from multiple digests.
    """
    builder = MultisigAddressBuilder()
    print_var_type_n_val(var001 = builder, pointer = "#345gfdsXCVB0000442")#345gfdsXCVB0000442
# Value: 
# # <iota.multisig.crypto.addresses.MultisigAddressBuilder object at 0x000001307407A240>

# Type: <class 'iota.multisig.crypto.addresses.MultisigAddressBuilder'>
    builder.add_digest(self.digest_1)
    builder.add_digest(self.digest_2)
    addy = builder.get_address()
    print_var_type_n_val(var001 = addy, pointer = "#2345gfdXCVNBVaaaa")#2345gfdXCVNBVaaaa
# Value: ZYKDKGXTMGINTQLUMVNBBI9XCEI9BWYF9YOPCBFTUUJZWM9YIWHNYZEWOPEVRVLKZCPRKLCQD9BR9FVLC
# Type: <class 'iota.multisig.types.MultisigAddress'>

    self.assertIsInstance(addy, MultisigAddress)

    # noinspection SpellCheckingInspection
    self.assertEqual(
      addy,

      Address(
        b'ZYKDKGXTMGINTQLUMVNBBI9XCEI9BWYF9YOPCBFT'
        b'UUJZWM9YIWHNYZEWOPEVRVLKZCPRKLCQD9BR9FVLC',
      ),
    )

    # The multisig address also keeps track of the digests used to
    # create it (mostly for troubleshooting purposes).
    self.assertListEqual(addy.digests, [self.digest_1, self.digest_2])

    print_var_type_n_val(var001 = addy.digests, pointer = "#3456gfdsXCVmlk12340")#3456gfdsXCVmlk12340
# Value: 
# # [Digest(b'FWNEPVJNGUKTSHSBDO9AORBCVWWLVXC9KAMKYYNKPYNJDKSAUURI9ELKOEEYPKVTYPCKOCJQESYFEMINIFKX9PDDGRBEEHYYXCJW9LHGWFZGHKCPVDBGMGQKIPCNKNITGMZTDIWVUB9PCHCOPHMIWKSUKRHZOJPMAY'), Digest(b'PAIRLDJQY9XAUSKIGCTHRJHZVARBEY9NNHYJ9UI9HWWZXFSDWEZEGDCWNVVYSYDV9OHTR9NGGZURISWTNECFTCMEWQQFJ9VKLFPDTYJYXC99OLGRH9OSFJLMEOGHFDHZYEAFIMIZTJRBQUVCR9U9ZWTMUXTUEOUBLC')]

# Type: <class 'list'>

  def test_success_single_digest(self):
    """
    Generating a "multisig" address from a single digest.

    This does the same thing as generating a regular address from the
    corresponding key.
    """
    builder = MultisigAddressBuilder()
    builder.add_digest(self.digest_1)
    addy = builder.get_address()

    self.assertIsInstance(addy, MultisigAddress)

    # noinspection SpellCheckingInspection
    self.assertEqual(
      addy,

      Address(
        b'TBOLOKTNJ9MFGBSJBIWDZBHWJRLMKAEGUZFJFNGS'
        b'VODKPPULLGJVHTCENCD9OOCNYPRLV9XGBGLDZNHPZ',
      ),
    )

    # The address is still designated multisig, so we keep track of the
    # digest used to generate it.
    self.assertListEqual(addy.digests, [self.digest_1])

  def test_error_no_digests(self):
    """
    Attempting to generate a multisig addresses without providing any
    digests.

    I mean, why even bother, right?
    """
    builder = MultisigAddressBuilder()
    print_var_type_n_val(var001 = builder, pointer = "#234GFDbvcsdfTR56")#234GFDbvcsdfTR56
# Value: 
# # <iota.multisig.crypto.addresses.MultisigAddressBuilder object at 0x000001A8F7E481D0>

# Type: <class 'iota.multisig.crypto.addresses.MultisigAddressBuilder'>

    with self.assertRaises(ValueError):
      builder.get_address()

  def test_success_duplicate_digest(self):
    """
    Using the same digest multiple times in the same multisig address?

    It's unconventional, admittedly, but the maths work out, so..
    """
    builder = MultisigAddressBuilder()
    builder.add_digest(self.digest_1)
    builder.add_digest(self.digest_2)

    # I have no idea why you'd want to do this, but that's why it's not
    # my job to make those kinds of decisions.
    builder.add_digest(self.digest_1)

    addy = builder.get_address()

    self.assertIsInstance(addy, MultisigAddress)

    # noinspection SpellCheckingInspection
    self.assertEqual(
      addy,

      Address(
        b'JXJLZDJENNRODT9VEIRPVDX9YRLMDYDEXCQUYFIU'
        b'XFKFJOYOGTJPEIBEKDNEFRFVVVSQFBGMNZRBGFARD',
      ),
    )

    # Note that ``digest_1`` appears twice, because we added it twice.
    self.assertListEqual(
      addy.digests,
      [self.digest_1, self.digest_2, self.digest_1],
    )

  def test_success_extract_multiple(self):
    """
    You can extract the address multiple times from the same builder
    (it's the same instance every time).
    """
    builder = MultisigAddressBuilder()
    builder.add_digest(self.digest_1)
    builder.add_digest(self.digest_2)
    addy_1 = builder.get_address()
    addy_2 = builder.get_address()

    # Same instance is returned every time.
    self.assertIs(addy_1, addy_2)

  def test_error_already_finalized(self):
    """
    Once an address is extracted from the builder, no more digests can
    be added.
    """
    builder = MultisigAddressBuilder()
    builder.add_digest(self.digest_1)
    builder.add_digest(self.digest_2)
    builder.get_address()

    with self.assertRaises(ValueError):
      builder.add_digest(self.digest_3)
