from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.server_file import ServerFile





T = TypeVar("T", bound="GetMcpServersServerSlugFilesResponse200")



@_attrs_define
class GetMcpServersServerSlugFilesResponse200:
    """ 
        Attributes:
            files (list[ServerFile]):
     """

    files: list[ServerFile]





    def to_dict(self) -> dict[str, Any]:
        from ..models.server_file import ServerFile
        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "files": files,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_file import ServerFile
        d = dict(src_dict)
        files = []
        _files = d.pop("files")
        for files_item_data in (_files):
            files_item = ServerFile.from_dict(files_item_data)



            files.append(files_item)


        get_mcp_servers_server_slug_files_response_200 = cls(
            files=files,
        )

        return get_mcp_servers_server_slug_files_response_200

