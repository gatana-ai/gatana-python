from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="TenantSamlConfiguration")



@_attrs_define
class TenantSamlConfiguration:
    """ 
        Attributes:
            is_enabled (bool):
            display_name (str):
            idp_metadata_url (str):
            idp_metadata_document (str):
            entry_point (str):
            cert (str):
            identifier_format (str):
            signature_algorithm (str):
            email_claim (str):
            first_name_claim (str):
            last_name_claim (str):
     """

    is_enabled: bool
    display_name: str
    idp_metadata_url: str
    idp_metadata_document: str
    entry_point: str
    cert: str
    identifier_format: str
    signature_algorithm: str
    email_claim: str
    first_name_claim: str
    last_name_claim: str





    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        display_name = self.display_name

        idp_metadata_url = self.idp_metadata_url

        idp_metadata_document = self.idp_metadata_document

        entry_point = self.entry_point

        cert = self.cert

        identifier_format = self.identifier_format

        signature_algorithm = self.signature_algorithm

        email_claim = self.email_claim

        first_name_claim = self.first_name_claim

        last_name_claim = self.last_name_claim


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "isEnabled": is_enabled,
            "displayName": display_name,
            "idpMetadataUrl": idp_metadata_url,
            "idpMetadataDocument": idp_metadata_document,
            "entryPoint": entry_point,
            "cert": cert,
            "identifierFormat": identifier_format,
            "signatureAlgorithm": signature_algorithm,
            "emailClaim": email_claim,
            "firstNameClaim": first_name_claim,
            "lastNameClaim": last_name_claim,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_enabled = d.pop("isEnabled")

        display_name = d.pop("displayName")

        idp_metadata_url = d.pop("idpMetadataUrl")

        idp_metadata_document = d.pop("idpMetadataDocument")

        entry_point = d.pop("entryPoint")

        cert = d.pop("cert")

        identifier_format = d.pop("identifierFormat")

        signature_algorithm = d.pop("signatureAlgorithm")

        email_claim = d.pop("emailClaim")

        first_name_claim = d.pop("firstNameClaim")

        last_name_claim = d.pop("lastNameClaim")

        tenant_saml_configuration = cls(
            is_enabled=is_enabled,
            display_name=display_name,
            idp_metadata_url=idp_metadata_url,
            idp_metadata_document=idp_metadata_document,
            entry_point=entry_point,
            cert=cert,
            identifier_format=identifier_format,
            signature_algorithm=signature_algorithm,
            email_claim=email_claim,
            first_name_claim=first_name_claim,
            last_name_claim=last_name_claim,
        )

        return tenant_saml_configuration

