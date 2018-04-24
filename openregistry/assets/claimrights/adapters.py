# -*- coding: utf-8 -*-
from openregistry.assets.core.adapters import AssetConfigurator, AssetManagerAdapter
from openregistry.assets.core.constants import STATUS_CHANGES


class ClaimRightsAssetConfigurator(AssetConfigurator):
    """ BelowThreshold Tender configuration adapter """

    name = "ClaimRights Asset configurator"
    available_statuses = STATUS_CHANGES


class ClaimRightsAssetManagerAdapter(AssetManagerAdapter):
    name = "Asset Manager for claimrights asset"
    context = None
    create_validation = []

    def __init__(self, context):
        self.context = context

    def create_asset(self, request):
        self._validate(request, self.create_validation)
