"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import user as components_user
from typing import Optional


@dataclasses.dataclass
class CreateUsersWithListInputResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    user: Optional[components_user.User] = dataclasses.field(default=None)
    r"""Successful operation"""
    
