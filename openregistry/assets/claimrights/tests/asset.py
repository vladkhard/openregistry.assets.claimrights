# -*- coding: utf-8 -*-
import unittest

from openregistry.api.tests.base import snitch
from openregistry.api.tests.blanks.mixins import ResourceTestMixin

from openregistry.assets.core.tests.blanks.asset import patch_decimal_item_quantity
from openregistry.assets.core.tests.blanks.mixins import AssetResourceTestMixin

from openregistry.assets.claimrights.models import Asset as AssetClaimRights
from openregistry.assets.claimrights.tests.base import (
    test_asset_claimrights_data, BaseAssetWebTest
)


class AssetClaimRightsResourceTest(BaseAssetWebTest, ResourceTestMixin, AssetResourceTestMixin):
    asset_model = AssetClaimRights
    initial_data = test_asset_claimrights_data
    initial_status = 'pending'

    test_19_patch_decimal_witt_items = snitch(patch_decimal_item_quantity)


def suite():
    tests = unittest.TestSuite()
    tests.addTest(unittest.makeSuite(AssetClaimRightsResourceTest))
    return tests


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
