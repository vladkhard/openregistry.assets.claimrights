# -*- coding: utf-8 -*-
import unittest

from openregistry.api.tests.blanks.mixins import ResourceTestMixin

from openregistry.assets.core.tests.blanks.mixins import AssetResourceTestMixin

from openregistry.assets.claimrights.models import Asset as AssetClaimRights
from openregistry.assets.claimrights.tests.base import (
    test_asset_claimRights_data, BaseAssetWebTest
)


class AssetClaimRightsResourceTest(BaseAssetWebTest, ResourceTestMixin, AssetResourceTestMixin):
    asset_model = AssetClaimRights
    initial_data = test_asset_claimRights_data
    initial_status = 'pending'


def suite():
    tests = unittest.TestSuite()
    tests.addTest(unittest.makeSuite(AssetClaimRightsResourceTest))
    return tests


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
