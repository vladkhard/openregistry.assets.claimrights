# -*- coding: utf-8 -*-
from openregistry.assets.core.views.mixins import AssetResource
from openregistry.assets.core.utils import opassetsresource


@opassetsresource(name='claimRights:Asset',
                  path='/assets/{asset_id}',
                  assetType='claimRights',
                  description="Open Contracting compatible data exchange format.")
class AssetClaimRightsResource(AssetResource):
    pass
