# -*- coding: utf-8 -*-
from pyramid.events import subscriber
from openregistry.assets.core.events import AssetInitializeEvent
from openregistry.assets.core.utils import get_now


@subscriber(AssetInitializeEvent, _internal_type="claimRights")
def tender_init_handler(event):
    """ initialization handler for claimRights assets """
    event.asset.date = get_now()
