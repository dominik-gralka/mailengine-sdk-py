"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import pet as components_pet
from typing import List, Optional


@dataclasses.dataclass
class FindPetsByTagsRequest:
    tags: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'tags', 'style': 'form', 'explode': True }})
    r"""Tags to filter by"""
    



@dataclasses.dataclass
class FindPetsByTagsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    pets: Optional[List[components_pet.Pet]] = dataclasses.field(default=None)
    r"""successful operation"""
    
