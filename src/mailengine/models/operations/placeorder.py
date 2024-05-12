"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import order as components_order
from typing import Optional


@dataclasses.dataclass
class PlaceOrderResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    order: Optional[components_order.Order] = dataclasses.field(default=None)
    r"""successful operation"""
    
