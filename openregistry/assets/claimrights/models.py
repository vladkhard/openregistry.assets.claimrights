# -*- coding: utf-8 -*-
from schematics.types import StringType
from schematics.types.compound import ListType, ModelType
from zope.interface import implementer

from openprocurement.api.registry_models.ocds import Item, Debt

from openregistry.assets.core.models import (
    IAsset, Asset as BaseAsset,
)


class IClaimRightsAsset(IAsset):
    """ Marker interface for claimRights assets """


@implementer(IClaimRightsAsset)
class Asset(BaseAsset):
    assetType = StringType(default="claimRights")
    items = ListType(ModelType(Item))
    debt = ModelType(Debt)
