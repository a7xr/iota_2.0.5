# coding=utf-8
from __future__ import absolute_import, division, print_function, \
  unicode_literals

from pack001 import *

# TestCase is going to be defined in: Python_Path\Lib\unittest\case.py
from unittest import TestCase

# the file below is going to be in:
# # site-packages/filters/test.py
# # just notice that "filters" is a folder, not a file
import filters as f
from filters.test import BaseFilterTestCase

from iota import Address, Iota, TryteString
from iota.adapter import MockAdapter
from iota.commands.core.get_balances import GetBalancesCommand
from iota.filters import Trytes


# just a simple reminder for the line below:
# # "BaseFilterTestCase" is set in 
# # # site-packages/filters/test.py
#
# "BaseFilterTestCase" is going to extend from "TestCase"
class GetBalancesRequestFilterTestCase(BaseFilterTestCase):
  filter_type = GetBalancesCommand(MockAdapter()).get_request_filter
  # print('type(filter_type)001: ', type(filter_type))
  # # <class 'method'>
  # print('filter_type 001: ', filter_type)
  # # <bound method GetBalancesCommand.get_request_filter of <iota.commands.core.get_balances.GetBalancesCommand object at 0x0000029B415C8F60>>
  skip_value_check = True

  # noinspection SpellCheckingInspection
  def setUp(self):
    # U should know this already, due the line below
    # # this is going to run "def setUp()" which is defined in "BaseFilterTestCase"
    super(GetBalancesRequestFilterTestCase, self).setUp()

    # Define a few valid values that we can reuse across tests.
    self.trytes1 = (
      'TESTVALUE9DONTUSEINPRODUCTION99999EKJZZT'
      'SOGJOUNVEWLDPKGTGAOIZIPMGBLHC9LMQNHLGXGYX'
    )

    self.trytes2 = (
      'TESTVALUE9DONTUSEINPRODUCTION99999FDCDTZ'
      'ZWLL9MYGUTLSYVSIFJ9NGALTRMCQVIIOVEQOITYTE'
    )

  def test_pass_happy_path(self):
    """
    Typical invocation of ``getBalances``.
    """
    request = {
      # Raw trytes are extracted to match the IRI's JSON protocol.
      'addresses': [self.trytes1, self.trytes2],

      'threshold': 80,
    }

    # once again, iota is going to use filters/test.py and "unittest" for testing
    #
    # 
    # "def _filter()" below is going to be defined in 
    # # site-packages/filters/test.py
    filter_ = self._filter(request)
    print_var_type_n_val(var001 = filter_, pointer = "#XCVBFFbvvbf234")#XCVBFFbvvbf234
# Value: 
# # GetBalancesRequestFilter(FilterChain(Type(Mapping, allow_subclass=True) | FilterMapper(addresses=FilterChain(Required(allow_none=False) | Array(Sequence, allow_subclass=True) | FilterRepeater(FilterChain(Required(allow_none=False) | AddressNoChecksum() | Unicode(encoding='ascii')))), threshold=FilterChain(Type(int, allow_subclass=True) | Min(0, exclusive=False) | Max(100, exclusive=False) | Optional(default=100)))))

# Type: <class 'filters.handlers.FilterRunner'>
    # the function below (assertFilterPasses()) is going to be defined in 
    # # site-packages/filters/test.py
    # # 
    # # the function below Asserts that the FilterRunner returns the specified value,
    # # # without errors.
    self.assertFilterPasses(filter_) #assertFilterPasses()
    self.assertDictEqual(filter_.cleaned_data, request)

  def test_pass_compatible_types(self):
    """
    The incoming request contains values that can be converted to the
    expected types.
    """
    request = {
      'addresses': [
        Address(self.trytes1),
        bytearray(self.trytes2.encode('ascii')),
      ],

      'threshold': 80,
    }

    filter_ = self._filter(request)
    print_var_type_n_val(var001 = request, pointer = "#EDFEsdfr345")#EDFEsdfr345
# Value: 
# # {'addresses': [Address(b'TESTVALUE9DONTUSEINPRODUCTION99999EKJZZTSOGJOUNVEWLDPKGTGAOIZIPMGBLHC9LMQNHLGXGYX'), bytearray(b'TESTVALUE9DONTUSEINPRODUCTION99999FDCDTZZWLL9MYGUTLSYVSIFJ9NGALTRMCQVIIOVEQOITYTE')], 'threshold': 80}

# Type: <class 'dict'>
    print_var_type_n_val(var001 = filter_, pointer = "#XCVBFFbvvbf234")#XCVBFFbvvbf234
# Value: 
# # GetBalancesRequestFilter(FilterChain(Type(Mapping, allow_subclass=True) | FilterMapper(addresses=FilterChain(Required(allow_none=False) | Array(Sequence, allow_subclass=True) | FilterRepeater(FilterChain(Required(allow_none=False) | AddressNoChecksum() | Unicode(encoding='ascii')))), threshold=FilterChain(Type(int, allow_subclass=True) | Min(0, exclusive=False) | Max(100, exclusive=False) | Optional(default=100)))))

# Type: <class 'filters.handlers.FilterRunner'>

    self.assertFilterPasses(filter_)
    self.assertDictEqual(
      filter_.cleaned_data,

      {
        'addresses': [self.trytes1, self.trytes2],
        'threshold': 80,
      },
    )

  def test_pass_threshold_optional(self):
    """
    The incoming request does not contain a ``threshold`` value, so the
    default value is assumed.
    """
    request = {
      'addresses': [Address(self.trytes1)],
    }

    filter_ = self._filter(request)

    self.assertFilterPasses(filter_)
    self.assertDictEqual(
      filter_.cleaned_data,

      {
        'addresses': [Address(self.trytes1)],
        'threshold': 100,
      },
    )

  def test_fail_empty(self):
    """
    The incoming request is empty.
    """
    self.assertFilterErrors(
      {},

      {
        'addresses': [f.FilterMapper.CODE_MISSING_KEY],
      },
    )

  def test_fail_unexpected_parameters(self):
    """
    The incoming request contains unexpected parameters.
    """
    self.assertFilterErrors(
      {
        'addresses': [Address(self.trytes1)],

        # I've had a perfectly wonderful evening.
        # But this wasn't it.
        'foo': 'bar',
      },

      {
        'foo': [f.FilterMapper.CODE_EXTRA_KEY],
      },
    )

  def test_fail_addresses_wrong_type(self):
    """
    ``addresses`` is not an array.
    """
    self.assertFilterErrors(
      {
        'addresses': Address(self.trytes1),
      },

      {
        'addresses': [f.Type.CODE_WRONG_TYPE],
      },
    )

  def test_fail_addresses_empty(self):
    """
    ``addresses`` is an array, but it's empty.
    """
    self.assertFilterErrors(
      {
        'addresses': [],
      },

      {
        'addresses': [f.Required.CODE_EMPTY],
      },
    )

  def test_fail_addresses_contents_invalid(self):
    """
    ``addresses`` is an array, but it contains invalid values.
    """
    self.assertFilterErrors(
      {
        'addresses': [
          b'',
          True,
          None,
          b'not valid trytes',

          # This is actually valid; I just added it to make sure the
          # filter isn't cheating!
          TryteString(self.trytes2),

          2130706433,
          b'9' * 82,
        ],
      },

      {
        'addresses.0':  [f.Required.CODE_EMPTY],
        'addresses.1':  [f.Type.CODE_WRONG_TYPE],
        'addresses.2':  [f.Required.CODE_EMPTY],
        'addresses.3':  [Trytes.CODE_NOT_TRYTES],
        'addresses.5':  [f.Type.CODE_WRONG_TYPE],
        'addresses.6':  [Trytes.CODE_WRONG_FORMAT],
      },
    )

  def test_fail_threshold_float(self):
    """
    `threshold` is a float.
    """
    self.assertFilterErrors(
      {
        # Even with an empty fpart, floats are not accepted.
        'threshold': 86.0,

        'addresses': [Address(self.trytes1)],
      },

      {
        'threshold': [f.Type.CODE_WRONG_TYPE],
      },
    )

  def test_fail_threshold_string(self):
    """
    ``threshold`` is a string.
    """
    self.assertFilterErrors(
      {
        'threshold': '86',

        'addresses': [Address(self.trytes1)],
      },

      {
        'threshold': [f.Type.CODE_WRONG_TYPE],
      },
    )

  def test_fail_threshold_too_small(self):
    """
    ``threshold`` is less than 0.
    """
    self.assertFilterErrors(
      {
        'threshold': -1,

        'addresses': [Address(self.trytes1)],
      },

      {
        'threshold': [f.Min.CODE_TOO_SMALL],
      },
    )

  def test_fail_threshold_too_big(self):
    """
    ``threshold`` is greater than 100.
    """
    self.assertFilterErrors(
      {
        'threshold': 101,

        'addresses': [Address(self.trytes1)],
      },

      {
        'threshold': [f.Max.CODE_TOO_BIG],
      },
    )


# noinspection SpellCheckingInspection
class GetBalancesResponseFilterTestCase(BaseFilterTestCase):
  filter_type = GetBalancesCommand(MockAdapter()).get_response_filter
  skip_value_check = True

  def test_balances(self):
    """
    Typical ``getBalances`` response.
    """
    filter_ = self._filter({
      'balances':       ['114544444', '0', '8175737'],
      'duration':       42,
      'milestoneIndex': 128,

      'milestone':
        'INRTUYSZCWBHGFGGXXPWRWBZACYAFGVRRP9VYEQJ'
        'OHYD9URMELKWAFYFMNTSP9MCHLXRGAFMBOZPZ9999',
    })

    self.assertFilterPasses(filter_)
    self.assertDictEqual(
      filter_.cleaned_data,

      {
        'balances':       [114544444, 0, 8175737],
        'duration':       42,
        'milestoneIndex': 128,

        'milestone':
          Address(
            b'INRTUYSZCWBHGFGGXXPWRWBZACYAFGVRRP9VYEQJ'
            b'OHYD9URMELKWAFYFMNTSP9MCHLXRGAFMBOZPZ9999',
          ),
      },
    )


class GetBalancesCommandTestCase(TestCase):
  def setUp(self):
    # the line below is going to run the "def setup()" which is set in
    # # 
    super(GetBalancesCommandTestCase, self).setUp()

    self.adapter = MockAdapter()

  def test_wireup(self):
    """
    Verify that the command is wired up correctly.
    """

    # just a comment of the line below
    # # it is possible to set the error which is going to be shown when
    # # the test is NOT fulfilled... Like this next_one
    # # # self.assertIsInstance(dict001, dict, 'First argument is not a dictionary')
    # #
    # it is possible to do the same as below with this next_command
    # # self.assertTrue(isinstance(obj001, cls))
    # # just remember, with the method below, it is possible to print an error_msg when
    # # # the assertion is false
    self.assertIsInstance(
      Iota(self.adapter).getBalances,
      GetBalancesCommand,
    )
