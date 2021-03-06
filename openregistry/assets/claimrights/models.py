# -*- coding: utf-8 -*-
from schematics.types import StringType
from schematics.types.compound import ListType, ModelType
from zope.interface import implementer

from openregistry.assets.core.models import (
    IAsset, Asset as BaseAsset, Item, Debt
)


class IClaimRightsAsset(IAsset):
    """ Marker interface for claimRights assets """


@implementer(IClaimRightsAsset)
class Asset(BaseAsset):
    _internal_type = "claimRights"
    assetType = StringType(default="claimRights")
    items = ListType(ModelType(Item))
    debt = ModelType(Debt)
