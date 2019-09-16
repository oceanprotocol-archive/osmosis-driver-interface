#  Copyright 2018 Ocean Protocol Foundation
#  SPDX-License-Identifier: Apache-2.0

from osmosis_driver_interface.osmosis import Osmosis


def test_parse_url_azure():
    assert Osmosis.parse_url(
        'https://testocnfiles.blob.core.windows.net/testfiles/testzkp.pdf') == 'azure'


def test_parse_url_aws():
    assert Osmosis.parse_url('s3://my_bucket') == 'aws'


def test_parse_url_on_premise():
    assert Osmosis.parse_url('http://www.example.com') == 'on_premise'


def test_parse_url_ipfs():
    assert Osmosis.parse_url('ipfs://ZmOfotxMWnLTXKKW0GPV9NgtEugghgD8HgzSF4gSrp7mL9') == 'ipfs'
