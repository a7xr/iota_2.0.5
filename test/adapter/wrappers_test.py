# coding=utf-8
from __future__ import absolute_import, division, print_function, \
  unicode_literals

from pack001 import *
from unittest import TestCase

from iota.adapter import HttpAdapter, MockAdapter
from iota.adapter.wrappers import RoutingWrapper


class RoutingWrapperTestCase(TestCase):
  def test_routing(self):
    """
    Routing commands to different adapters.
    """
    default_adapter = MockAdapter()
    pow_adapter     = MockAdapter()

    wrapper = (RoutingWrapper(default_adapter) .add_route('attachToTangle', pow_adapter) .add_route('interruptAttachingToTangle', pow_adapter) )
    print_var_type_n_val(var001 = wrapper, pointer = "#ZERTYSDdfg236")#ZERTYSDdfg236
# Value: 
# # <iota.adapter.wrappers.RoutingWrapper object at 0x000001E406CE30B8>

# Type: <class 'iota.adapter.wrappers.RoutingWrapper'>

    
    default_adapter.seed_response('getNodeInfo', {'id': 'default1'})
    print_var_type_n_val(var001 = wrapper, pointer = "#2345gfdsSDFG")#2345gfdsSDFG
# Value: 
# # <iota.adapter.wrappers.RoutingWrapper object at 0x000001E406CE30B8>

# Type: <class 'iota.adapter.wrappers.RoutingWrapper'>
    pow_adapter.seed_response('attachToTangle', {'id': 'pow1'})
    print_var_type_n_val(var001 = wrapper, pointer = "#34TgfdXCVBgfd111111")#34TgfdXCVBgfd111111
# Value: 
# # <iota.adapter.wrappers.RoutingWrapper object at 0x000001E406CE30B8>

# Type: <class 'iota.adapter.wrappers.RoutingWrapper'>
    pow_adapter.seed_response('interruptAttachingToTangle', {'id': 'pow2'})

    self.assertDictEqual(
      wrapper.send_request({'command': 'attachToTangle'}),
      {'id': 'pow1'},
    )

    self.assertDictEqual(
      wrapper.send_request({'command': 'interruptAttachingToTangle'}),
      {'id': 'pow2'},
    )

    # Any commands that aren't routed go to the default adapter.
    self.assertDictEqual(
      wrapper.send_request({'command': 'getNodeInfo'}),
      {'id': 'default1'},
    )

  def test_router_aliasing(self):
    """
    The router will try to re-use existing adapter instances.
    """
    wrapper1 = RoutingWrapper('http://localhost:14265')
    print_var_type_n_val(var001 = wrapper1, pointer = "#2345trezGH-(")#2345trezGH-(
# Value: 
# # <iota.adapter.wrappers.RoutingWrapper object at 0x0000024C271B17B8>

# Type: <class 'iota.adapter.wrappers.RoutingWrapper'>
    adapter_default = wrapper1.adapter
    print_var_type_n_val(var001 = adapter_default, pointer = "#SDFGnbvc1234098QSDnbe")#SDFGnbvc1234098QSDnbe
# Value: 
# # <iota.adapter.HttpAdapter object at 0x0000024C25E7AB70>

# Type: <class 'iota.adapter.HttpAdapter'>

    # The router will try to minimize the number of adapter instances
    # that it creates from URIs.
    wrapper1\
      .add_route('alpha', 'http://localhost:14265')\
      .add_route('bravo', 'http://localhost:14265')\

    print_var_type_n_val(var001 = wrapper1, pointer = "#2345trezGH2345YTRE")#2345trezGH2345YTRE
# Value: 
# # <iota.adapter.wrappers.RoutingWrapper object at 0x000001601AD6FD68>

# Type: <class 'iota.adapter.wrappers.RoutingWrapper'>
    # Two routes with the same URI => same adapter instance.
    self.assertIs(
      wrapper1.get_adapter('bravo'),
      wrapper1.get_adapter('alpha'),
    )

    # "127.0.0.1" != "localhost", so separate adapters created.
    wrapper1.add_route('charlie', 'http://127.0.0.1:14265')
    self.assertIsNot(
      wrapper1.get_adapter('charlie'),
      wrapper1.get_adapter('alpha'),
    )

    # Providing an adapter instance bypasses the whole setup.
    wrapper1.add_route('delta', HttpAdapter('http://localhost:14265'))
    self.assertIsNot(
      wrapper1.get_adapter('delta'),
      wrapper1.get_adapter('alpha'),
    )

    # The default adapter is always kept separate, even if it URI
    # matches a routing adapter.
    self.assertIsNot(
      wrapper1.get_adapter('foo'),
      wrapper1.get_adapter('alpha'),
    )

    # Aliased adapters are not shared between routers.
    wrapper2 = RoutingWrapper(adapter_default)

    wrapper2.add_route('echo', 'http://localhost:14265')
    self.assertIsNot(
      wrapper2.get_adapter('echo'),
      wrapper1.get_adapter('alpha'),
    )
