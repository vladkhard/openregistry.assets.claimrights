# -*- coding: utf-8 -*-
import logging

from pyramid.interfaces import IRequest
from openregistry.assets.core.includeme import IContentConfigurator
from openregistry.assets.core.interfaces import IAssetManager
from openregistry.assets.claimrights.models import Asset, IClaimRightsAsset
from openregistry.assets.claimrights.adapters import ClaimRightsAssetConfigurator, ClaimRightsAssetManagerAdapter
from openregistry.assets.claimrights.constants import DEFAULT_ASSET_CLAIMRIGHTS_TYPE

LOGGER = logging.getLogger(__name__)


def includeme(config, plugin_config=None):
    config.scan("openregistry.assets.claimrights.views")
    config.scan("openregistry.assets.claimrights.subscribers")
    config.registry.registerAdapter(ClaimRightsAssetConfigurator,
                                    (IClaimRightsAsset, IRequest),
                                    IContentConfigurator)
    config.registry.registerAdapter(ClaimRightsAssetManagerAdapter,
                                    (IClaimRightsAsset, ),
                                    IAssetManager)

    asset_types = plugin_config.get('aliases', [])
    if plugin_config.get('use_default', False):
        asset_types.append(DEFAULT_ASSET_CLAIMRIGHTS_TYPE)
    for at in asset_types:
        config.add_assetType(Asset, at)

    LOGGER.info("Included openregistry.assets.claimrights plugin", extra={'MESSAGE_ID': 'included_plugin'})
