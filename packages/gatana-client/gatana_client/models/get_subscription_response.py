from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_subscription_response_subscription_type_0 import GetSubscriptionResponseSubscriptionType0





T = TypeVar("T", bound="GetSubscriptionResponse")



@_attrs_define
class GetSubscriptionResponse:
    """ 
        Attributes:
            subscription_plan (str):
            subscription_seats (float):
            subscription (GetSubscriptionResponseSubscriptionType0 | None):
     """

    subscription_plan: str
    subscription_seats: float
    subscription: GetSubscriptionResponseSubscriptionType0 | None





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_subscription_response_subscription_type_0 import GetSubscriptionResponseSubscriptionType0
        subscription_plan = self.subscription_plan

        subscription_seats = self.subscription_seats

        subscription: dict[str, Any] | None
        if isinstance(self.subscription, GetSubscriptionResponseSubscriptionType0):
            subscription = self.subscription.to_dict()
        else:
            subscription = self.subscription


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "subscriptionPlan": subscription_plan,
            "subscriptionSeats": subscription_seats,
            "subscription": subscription,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_subscription_response_subscription_type_0 import GetSubscriptionResponseSubscriptionType0
        d = dict(src_dict)
        subscription_plan = d.pop("subscriptionPlan")

        subscription_seats = d.pop("subscriptionSeats")

        def _parse_subscription(data: object) -> GetSubscriptionResponseSubscriptionType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subscription_type_0 = GetSubscriptionResponseSubscriptionType0.from_dict(data)



                return subscription_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetSubscriptionResponseSubscriptionType0 | None, data)

        subscription = _parse_subscription(d.pop("subscription"))


        get_subscription_response = cls(
            subscription_plan=subscription_plan,
            subscription_seats=subscription_seats,
            subscription=subscription,
        )

        return get_subscription_response

