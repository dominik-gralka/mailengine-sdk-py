"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import pet as components_pet
from typing import Optional


@dataclasses.dataclass
class AddPetResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    pet: Optional[components_pet.Pet] = dataclasses.field(default=None)
    r"""Successful operation"""
    

