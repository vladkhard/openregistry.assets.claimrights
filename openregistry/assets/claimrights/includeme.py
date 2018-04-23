# -*- coding: utf-8 -*-
from pyramid.interfaces import IRequest
from openregistry.assets.core.includeme import IContentConfigurator
from openregistry.assets.claimrights.models import Asset, IClaimRightsAsset
from openregistry.assets.claimrights.adapters import ClaimRightsAssetConfigurator


def includeme(config, plugin_config=None):
    config.add_assetType(Asset)
    config.scan("openregistry.assets.claimrights.views")
    config.scan("openregistry.assets.claimrights.subscribers")
    config.registry.registerAdapter(ClaimRightsAssetConfigurator,
                                    (IClaimRightsAsset, IRequest),
                                    IContentConfigurator)
