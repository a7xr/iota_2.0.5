# coding=utf-8
from __future__ import absolute_import, division, print_function, \
  unicode_literals

from unittest import TestCase
from pack001 import *
import filters as f
from filters.test import BaseFilterTestCase

from iota import Iota, TransactionHash, TryteString
from iota.adapter import MockAdapter
from iota.commands.core.check_consistency import CheckConsistencyCommand
from iota.filters import Trytes


class CheckConsistencyRequestFilterTestCase(BaseFilterTestCase):
  filter_type = CheckConsistencyCommand(MockAdapter()).get_request_filter
  print_var_type_n_val(var001 = filter_type, pointer = "#ZERTGFDzdfcx1234876666")#ZERTGFDzdfcx1234876666
# Value: 
# # <bound method CheckConsistencyCommand.get_request_filter of <iota.commands.core.check_consistency.CheckConsistencyCommand object at 0x000001AD00D58908>>

# Type: <class 'method'>
  skip_value_check = True

  # noinspection SpellCheckingInspection
  def setUp(self):
    super(CheckConsistencyRequestFilterTestCase, self).setUp()

    self.hash1 = (
      'TESTVALUE9DONTUSEINPRODUCTION99999DXSCAD'
      'YBVDCTTBLHFYQATFZPYPCBG9FOUKIGMYIGLHM9NEZ'
    )

    self.hash2 = (
      'TESTVALUE9DONTUSEINPRODUCTION99999EMFYSM'
      'HWODIAPUTTFDLQRLYIDAUIPJXXEXZZSBVKZEBWGAN'
    )

  def test_pass_happy_path(self):
    """
    Request is valid.
    """
    request = {
      # Raw trytes are extracted to match the IRI's JSON protocol.
      'tails': [self.hash1, self.hash2],
    }

    filter_ = self._filter(request)
    print_var_type_n_val(var001 = filter_, pointer = "#SDFGazerg123BV")#SDFGazerg123BV
# Value: 
# # CheckConsistencyRequestFilter(FilterChain(Type(Mapping, allow_subclass=True) | FilterMapper(tails=FilterChain(Required(allow_none=False) | Array(Sequence, allow_subclass=True) | FilterRepeater(FilterChain(Required(allow_none=False) | Trytes()))))))

# Type: <class 'filters.handlers.FilterRunner'>
    print_var_type_n_val(var001 = request, pointer = "#SDFGbvcERTRFGF1239876555555")#SDFGbvcERTRFGF1239876555555
# Value: 
# # {'tails': ['TESTVALUE9DONTUSEINPRODUCTION99999DXSCADYBVDCTTBLHFYQATFZPYPCBG9FOUKIGMYIGLHM9NEZ', 'TESTVALUE9DONTUSEINPRODUCTION99999EMFYSMHWODIAPUTTFDLQRLYIDAUIPJXXEXZZSBVKZEBWGAN']}

# Type: <class 'dict'>

    self.assertFilterPasses(filter_)
    self.assertDictEqual(filter_.cleaned_data, request)

  def test_pass_compatible_types(self):
    """
    Request contains values that can be converted to the expected
    types.
    """
    filter_ = self._filter({
      'tails': [
        # Any TrytesCompatible value can be used here.
        TransactionHash(self.hash1),
        bytearray(self.hash2.encode('ascii')),
      ],
    })

    self.assertFilterPasses(filter_)
    self.assertDictEqual(
      filter_.cleaned_data,

      {
        # Raw trytes are extracted to match the IRI's JSON protocol.
        'tails': [self.hash1, self.hash2],
      },
    )

  def test_fail_empty(self):
    """
    Request is empty.
    """
    self.assertFilterErrors(
      {},

      {
        'tails': [f.FilterMapper.CODE_MISSING_KEY],
      },
    )

  def test_fail_unexpected_parameters(self):
    """
    Request contains unexpected parameters.
    """
    self.assertFilterErrors(
      {
        'tails': [TransactionHash(self.hash1)],
        'foo': 'bar',
      },

      {
        'foo': [f.FilterMapper.CODE_EXTRA_KEY],
      },
    )

  def test_fail_tails_null(self):
    """
    ``tails`` is null.
    """
    self.assertFilterErrors(
      {
        'tails': None,
      },

      {
        'tails': [f.Required.CODE_EMPTY],
      },
    )

  def test_fail_tails_wrong_type(self):
    """
    ``tails`` is not an array.
    """
    self.assertFilterErrors(
      {
        # It's gotta be an array, even if there's only one hash.
        'tails': TransactionHash(self.hash1),
      },

      {
        'tails': [f.Type.CODE_WRONG_TYPE],
      },
    )

  def test_fail_tails_empty(self):
    """
    ``tails`` is an array, but it is empty.
    """
    self.assertFilterErrors(
      {
        'tails': [],
      },

      {
        'tails': [f.Required.CODE_EMPTY],
      },
    )

  def test_fail_tails_contents_invalid(self):
    """
    ``tails`` is a non-empty array, but it contains invalid values.
    """
    self.assertFilterErrors(
      {
        'tails': [
          b'',
          True,
          None,
          b'not valid trytes',

          # This is actually valid; I just added it to make sure the
          #   filter isn't cheating!
          TryteString(self.hash1),

          2130706433,
          b'9' * 82,
        ],
      },

      {
        'tails.0':  [f.Required.CODE_EMPTY],
        'tails.1':  [f.Type.CODE_WRONG_TYPE],
        'tails.2':  [f.Required.CODE_EMPTY],
        'tails.3':  [Trytes.CODE_NOT_TRYTES],
        'tails.5':  [f.Type.CODE_WRONG_TYPE],
        'tails.6':  [Trytes.CODE_WRONG_FORMAT],
      },
    )


class CheckConsistencyCommandTestCase(TestCase):
  # noinspection SpellCheckingInspection
  def setUp(self):
    super(CheckConsistencyCommandTestCase, self).setUp()

    self.adapter = MockAdapter()
    self.command = CheckConsistencyCommand(self.adapter)

    # Define some tryte sequences that we can re-use across tests.
    self.milestone =\
      TransactionHash(
        b'TESTVALUE9DONTUSEINPRODUCTION99999W9KDIH'
        b'BALAYAFCADIDU9HCXDKIXEYDNFRAKHN9IEIDZFWGJ'
      )
    print_var_type_n_val(var001 = self.milestone, pointer = "#SDFGhgfd1234598764444")#SDFGhgfd1234598764444
# Value: TESTVALUE9DONTUSEINPRODUCTION99999W9KDIHBALAYAFCADIDU9HCXDKIXEYDNFRAKHN9IEIDZFWGJ
# Type: <class 'iota.transaction.types.TransactionHash'>

    self.hash1 =\
      TransactionHash(
        b'TESTVALUE9DONTUSEINPRODUCTION99999TBPDM9'
        b'ADFAWCKCSFUALFGETFIFG9UHIEFE9AYESEHDUBDDF'
      )

    self.hash2 =\
      TransactionHash(
        b'TESTVALUE9DONTUSEINPRODUCTION99999CIGCCF'
        b'KIUFZF9EP9YEYGQAIEXDTEAAUGAEWBBASHYCWBHDX'
      )
    print_var_type_n_val(var001 = self.hash2, pointer = "#SDFGDFERTRTRnnnnbc1111")#SDFGDFERTRTRnnnnbc1111
# Value: TESTVALUE9DONTUSEINPRODUCTION99999CIGCCFKIUFZF9EP9YEYGQAIEXDTEAAUGAEWBBASHYCWBHDX
# Type: <class 'iota.transaction.types.TransactionHash'>

  def test_wireup(self):
    """
    Verify that the command is wired up correctly.
    """
    self.assertIsInstance(
      Iota(self.adapter).checkConsistency,
      CheckConsistencyCommand,
    )

  def test_happy_path(self):
    """
    Successfully checking consistency.
    """

    self.adapter.seed_response('checkConsistency', {
      'state': True,
    })

    response = self.command(tails=[self.hash1, self.hash2])
    print_var_type_n_val(var001 = response, pointer = "#QSDFGHbvc12347777")#QSDFGHbvc12347777
# Value: 
# # {'state': True}

# Type: <class 'dict'>

    self.assertDictEqual(
      response,

      {
        'state': True,
      }
    )

  def test_info_with_false_state(self):
    """
    `info` field exists when `state` is False.
    """

    self.adapter.seed_response('checkConsistency', {
      'state': False,
      'info': 'Additional information',
    })

    response = self.command(tails=[self.hash1, self.hash2])
    print_var_type_n_val(var001 = response, pointer = "#SDFGazer1234765555bbbb")#SDFGazer1234765555bbbb
# Value: 
# # {'state': False, 'info': 'Additional information'}

# Type: <class 'dict'>
    self.assertDictEqual(
      response,

      {
        'state': False,
        'info': 'Additional information',
      }
    )
