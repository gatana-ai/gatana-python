from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetSubscriptionResponseSubscriptionType0CardType0")



@_attrs_define
class GetSubscriptionResponseSubscriptionType0CardType0:
    """ 
        Attributes:
            valid (bool):
            brand (str):
            last4 (str):
            expires_year (float):
            expires_month (float):
     """

    valid: bool
    brand: str
    last4: str
    expires_year: float
    expires_month: float





    def to_dict(self) -> dict[str, Any]:
        valid = self.valid

        brand = self.brand

        last4 = self.last4

        expires_year = self.expires_year

        expires_month = self.expires_month


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "valid": valid,
            "brand": brand,
            "last4": last4,
            "expiresYear": expires_year,
            "expiresMonth": expires_month,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        valid = d.pop("valid")

        brand = d.pop("brand")

        last4 = d.pop("last4")

        expires_year = d.pop("expiresYear")

        expires_month = d.pop("expiresMonth")

        get_subscription_response_subscription_type_0_card_type_0 = cls(
            valid=valid,
            brand=brand,
            last4=last4,
            expires_year=expires_year,
            expires_month=expires_month,
        )

        return get_subscription_response_subscription_type_0_card_type_0

