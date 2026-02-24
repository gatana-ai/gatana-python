from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.secret_store_response import SecretStoreResponse





T = TypeVar("T", bound="SecretStoreListResponse")



@_attrs_define
class SecretStoreListResponse:
    """ 
        Attributes:
            stores (list[SecretStoreResponse]):
     """

    stores: list[SecretStoreResponse]





    def to_dict(self) -> dict[str, Any]:
        from ..models.secret_store_response import SecretStoreResponse
        stores = []
        for stores_item_data in self.stores:
            stores_item = stores_item_data.to_dict()
            stores.append(stores_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "stores": stores,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.secret_store_response import SecretStoreResponse
        d = dict(src_dict)
        stores = []
        _stores = d.pop("stores")
        for stores_item_data in (_stores):
            stores_item = SecretStoreResponse.from_dict(stores_item_data)



            stores.append(stores_item)


        secret_store_list_response = cls(
            stores=stores,
        )

        return secret_store_list_response

