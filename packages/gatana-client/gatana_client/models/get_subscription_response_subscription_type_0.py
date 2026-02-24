from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_subscription_response_subscription_type_0_card_type_0 import GetSubscriptionResponseSubscriptionType0CardType0





T = TypeVar("T", bound="GetSubscriptionResponseSubscriptionType0")



@_attrs_define
class GetSubscriptionResponseSubscriptionType0:
    """ 
        Attributes:
            has_payment_method (bool):
            trial_ends_at (None | str):
            status (str):
            current_period_end (str):
            cancels_at (None | str):
            per_seat_amount (float):
            currency (str):
            card (GetSubscriptionResponseSubscriptionType0CardType0 | None):
            payment_type (None | str | Unset):
     """

    has_payment_method: bool
    trial_ends_at: None | str
    status: str
    current_period_end: str
    cancels_at: None | str
    per_seat_amount: float
    currency: str
    card: GetSubscriptionResponseSubscriptionType0CardType0 | None
    payment_type: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_subscription_response_subscription_type_0_card_type_0 import GetSubscriptionResponseSubscriptionType0CardType0
        has_payment_method = self.has_payment_method

        trial_ends_at: None | str
        trial_ends_at = self.trial_ends_at

        status = self.status

        current_period_end = self.current_period_end

        cancels_at: None | str
        cancels_at = self.cancels_at

        per_seat_amount = self.per_seat_amount

        currency = self.currency

        card: dict[str, Any] | None
        if isinstance(self.card, GetSubscriptionResponseSubscriptionType0CardType0):
            card = self.card.to_dict()
        else:
            card = self.card

        payment_type: None | str | Unset
        if isinstance(self.payment_type, Unset):
            payment_type = UNSET
        else:
            payment_type = self.payment_type


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "hasPaymentMethod": has_payment_method,
            "trialEndsAt": trial_ends_at,
            "status": status,
            "currentPeriodEnd": current_period_end,
            "cancelsAt": cancels_at,
            "perSeatAmount": per_seat_amount,
            "currency": currency,
            "card": card,
        })
        if payment_type is not UNSET:
            field_dict["paymentType"] = payment_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_subscription_response_subscription_type_0_card_type_0 import GetSubscriptionResponseSubscriptionType0CardType0
        d = dict(src_dict)
        has_payment_method = d.pop("hasPaymentMethod")

        def _parse_trial_ends_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        trial_ends_at = _parse_trial_ends_at(d.pop("trialEndsAt"))


        status = d.pop("status")

        current_period_end = d.pop("currentPeriodEnd")

        def _parse_cancels_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cancels_at = _parse_cancels_at(d.pop("cancelsAt"))


        per_seat_amount = d.pop("perSeatAmount")

        currency = d.pop("currency")

        def _parse_card(data: object) -> GetSubscriptionResponseSubscriptionType0CardType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                card_type_0 = GetSubscriptionResponseSubscriptionType0CardType0.from_dict(data)



                return card_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetSubscriptionResponseSubscriptionType0CardType0 | None, data)

        card = _parse_card(d.pop("card"))


        def _parse_payment_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_type = _parse_payment_type(d.pop("paymentType", UNSET))


        get_subscription_response_subscription_type_0 = cls(
            has_payment_method=has_payment_method,
            trial_ends_at=trial_ends_at,
            status=status,
            current_period_end=current_period_end,
            cancels_at=cancels_at,
            per_seat_amount=per_seat_amount,
            currency=currency,
            card=card,
            payment_type=payment_type,
        )

        return get_subscription_response_subscription_type_0

