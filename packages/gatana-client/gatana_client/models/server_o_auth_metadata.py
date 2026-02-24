from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_o_auth_metadata_as import ServerOAuthMetadataAs
    from ..models.server_o_auth_metadata_resource import ServerOAuthMetadataResource


T = TypeVar("T", bound="ServerOAuthMetadata")


@_attrs_define
class ServerOAuthMetadata:
    """
    Attributes:
        requires_authorization (bool):
        resource (ServerOAuthMetadataResource | Unset):
        as_ (ServerOAuthMetadataAs | Unset):
    """

    requires_authorization: bool
    resource: ServerOAuthMetadataResource | Unset = UNSET
    as_: ServerOAuthMetadataAs | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        requires_authorization = self.requires_authorization

        resource: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource, Unset):
            resource = self.resource.to_dict()

        as_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.as_, Unset):
            as_ = self.as_.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "requiresAuthorization": requires_authorization,
            }
        )
        if resource is not UNSET:
            field_dict["resource"] = resource
        if as_ is not UNSET:
            field_dict["as"] = as_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_o_auth_metadata_as import ServerOAuthMetadataAs
        from ..models.server_o_auth_metadata_resource import ServerOAuthMetadataResource

        d = dict(src_dict)
        requires_authorization = d.pop("requiresAuthorization")

        _resource = d.pop("resource", UNSET)
        resource: ServerOAuthMetadataResource | Unset
        if isinstance(_resource, Unset):
            resource = UNSET
        else:
            resource = ServerOAuthMetadataResource.from_dict(_resource)

        _as_ = d.pop("as", UNSET)
        as_: ServerOAuthMetadataAs | Unset
        if isinstance(_as_, Unset):
            as_ = UNSET
        else:
            as_ = ServerOAuthMetadataAs.from_dict(_as_)

        server_o_auth_metadata = cls(
            requires_authorization=requires_authorization,
            resource=resource,
            as_=as_,
        )

        return server_o_auth_metadata
