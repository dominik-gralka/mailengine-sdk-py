"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from typing import Dict, Optional


@dataclasses.dataclass
class GetInventoryResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    object: Optional[Dict[str, int]] = dataclasses.field(default=None)
    r"""successful operation"""
    
