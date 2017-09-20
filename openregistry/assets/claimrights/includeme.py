# -*- coding: utf-8 -*-
from pyramid.interfaces import IRequest
from openregistry.api.interfaces import IContentConfigurator
from openregistry.assets.claimrights.models import Asset, IClaimRightsAsset
from openregistry.assets.claimrights.adapters import ClaimRightsAssetConfigurator


def includeme(config):
    config.add_assetType(Asset)
    config.scan("openregistry.assets.claimrights.views")
    config.scan("openregistry.assets.claimrights.subscribers")
    config.registry.registerAdapter(ClaimRightsAssetConfigurator,
                                    (IClaimRightsAsset, IRequest),
                                    IContentConfigurator)
