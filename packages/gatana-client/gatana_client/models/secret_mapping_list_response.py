from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.secret_mapping_response import SecretMappingResponse





T = TypeVar("T", bound="SecretMappingListResponse")



@_attrs_define
class SecretMappingListResponse:
    """ 
        Attributes:
            mappings (list[SecretMappingResponse]):
     """

    mappings: list[SecretMappingResponse]





    def to_dict(self) -> dict[str, Any]:
        from ..models.secret_mapping_response import SecretMappingResponse
        mappings = []
        for mappings_item_data in self.mappings:
            mappings_item = mappings_item_data.to_dict()
            mappings.append(mappings_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "mappings": mappings,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.secret_mapping_response import SecretMappingResponse
        d = dict(src_dict)
        mappings = []
        _mappings = d.pop("mappings")
        for mappings_item_data in (_mappings):
            mappings_item = SecretMappingResponse.from_dict(mappings_item_data)



            mappings.append(mappings_item)


        secret_mapping_list_response = cls(
            mappings=mappings,
        )

        return secret_mapping_list_response

