"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import user as components_user
from typing import Optional


@dataclasses.dataclass
class UpdateUserRequest:
    username: str = dataclasses.field(metadata={'path_param': { 'field_name': 'username', 'style': 'simple', 'explode': False }})
    r"""name that needs to be updated"""
    user: Optional[components_user.User] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Update an existent user in the store"""
    



@dataclasses.dataclass
class UpdateUserResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    
