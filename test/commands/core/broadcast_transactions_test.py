# coding=utf-8
from __future__ import absolute_import, division, print_function, \
  unicode_literals
from pack001 import *
from unittest import TestCase

import filters as f
from filters.test import BaseFilterTestCase
from six import binary_type, text_type

from iota import Iota, TransactionTrytes, TryteString
from iota.adapter import MockAdapter
from iota.commands.core.broadcast_transactions import \
  BroadcastTransactionsCommand
from iota.filters import Trytes


class BroadcastTransactionsRequestFilterTestCase(BaseFilterTestCase):
  filter_type = BroadcastTransactionsCommand(MockAdapter()).get_request_filter
  print_var_type_n_val(var001 = filter_type, pointer = "#23456FESDFDdsdfd")#23456FESDFDdsdfd
# Value: 
# # <bound method BroadcastTransactionsCommand.get_request_filter of <iota.commands.core.broadcast_transactions.BroadcastTransactionsCommand object at 0x00000173E70A88D0>>

# Type: <class 'method'>
  skip_value_check = True

  # noinspection SpellCheckingInspection
  def setUp(self):
    super(BroadcastTransactionsRequestFilterTestCase, self).setUp()

    # Define a few valid values that we can reuse across tests.
    self.trytes1 = TransactionTrytes('RBTC9D9DCDQAEASBYBCCKBFA')
    self.trytes2 =\
      TransactionTrytes(
        'CCPCBDVC9DTCEAKDXC9D9DEARCWCPCBDVCTCEAHDWCTCEAKDCDFD9DSCSA'
      )
    print_var_type_n_val(var001 = self.trytes2, pointer = "#R43EDFdfsSDFDtre")#R43EDFdfsSDFDtre
# Value: CCPCBDVC9DTCEAKDXC9D9DEARCWCPCBDVCTCEAHDWCTCEAKDCDFD9DSCSA99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
# Type: <class 'iota.transaction.types.TransactionTrytes'>

  def test_pass_happy_path(self):
    """
    The incoming request is valid.
    """
    request = {
      'trytes': [
        text_type(self.trytes1),
        text_type(self.trytes2),
      ],
    }

    filter_ = self._filter(request)

    self.assertFilterPasses(filter_)
    self.assertDictEqual(filter_.cleaned_data, request)

  def test_pass_compatible_types(self):
    """
    The incoming request contains values that can be converted into the
    expected types.
    """
    # Any values that can be converted into TryteStrings are accepted.
    filter_ = self._filter({
      'trytes': [
        binary_type(self.trytes1),
        self.trytes2,
      ],
    })
    print_var_type_n_val(var001 = filter_, pointer = "#SDFTREzertg123498xcvb")#SDFTREzertg123498xcvb
# Value: 
# # BroadcastTransactionsRequestFilter(FilterChain(Type(Mapping, allow_subclass=True) | FilterMapper(trytes=FilterChain(Required(allow_none=False) | Array(Sequence, allow_subclass=True) | FilterRepeater(FilterChain(Required(allow_none=False) | Trytes() | Unicode(encoding='ascii')))))))

# Type: <class 'filters.handlers.FilterRunner'>

    self.assertFilterPasses(filter_)
    self.assertDictEqual(
      filter_.cleaned_data,

      {
        'trytes': [
          # Raw trytes are extracted to match the IRI's JSON protocol.
          text_type(self.trytes1),
          text_type(self.trytes2),
        ],
      },
    )

  def test_fail_empty(self):
    """
    The incoming request is empty.
    """
    self.assertFilterErrors(
      {},

      {
        'trytes': [f.FilterMapper.CODE_MISSING_KEY],
      },
    )

  def test_fail_unexpected_parameters(self):
    """
    The incoming value contains unexpected parameters.
    """
    self.assertFilterErrors(
      {
        'trytes': [TryteString(self.trytes1)],

        # Alright buddy, let's see some ID.
        'foo': 'bar',
      },

      {
        'foo': [f.FilterMapper.CODE_EXTRA_KEY],
      },
    )

  def test_fail_trytes_null(self):
    """
    ``trytes`` is null.
    """
    self.assertFilterErrors(
      {
        'trytes': None,
      },

      {
        'trytes': [f.Required.CODE_EMPTY],
      },
    )

  def test_fail_trytes_wrong_type(self):
    """
    ``trytes`` is not an array.
    """
    self.assertFilterErrors(
      {
        # ``trytes`` has to be an array, even if there's only one
        # TryteString.
        'trytes': TryteString(self.trytes1),
      },

      {
        'trytes': [f.Type.CODE_WRONG_TYPE],
      },
    )

  def test_fail_trytes_empty(self):
    """
    ``trytes`` is an array, but it's empty.
    """
    self.assertFilterErrors(
      {
        'trytes': [],
      },

      {
        'trytes': [f.Required.CODE_EMPTY],
      },
    )

  def test_trytes_contents_invalid(self):
    """
    ``trytes`` is an array, but it contains invalid values.
    """
    self.assertFilterErrors(
      {
        'trytes': [
          b'',
          True,
          None,
          b'not valid trytes',

          # This is actually valid; I just added it to make sure the
          # filter isn't cheating!
          TryteString(self.trytes2),

          2130706433,

          b'9' * (TransactionTrytes.LEN + 1),
        ],
      },

      {
        'trytes.0': [f.NotEmpty.CODE_EMPTY],
        'trytes.1': [f.Type.CODE_WRONG_TYPE],
        'trytes.2': [f.Required.CODE_EMPTY],
        'trytes.3': [Trytes.CODE_NOT_TRYTES],
        'trytes.5': [f.Type.CODE_WRONG_TYPE],
        'trytes.6': [Trytes.CODE_WRONG_FORMAT],
      },
    )


class BroadcastTransactionsCommandTestCase(TestCase):
  def setUp(self):
    super(BroadcastTransactionsCommandTestCase, self).setUp()

    self.adapter = MockAdapter()

  def test_wireup(self):
    """
    Verify that the command is wired up correctly.
    """
    self.assertIsInstance(
      Iota(self.adapter).broadcastTransactions,
      BroadcastTransactionsCommand,
    )
