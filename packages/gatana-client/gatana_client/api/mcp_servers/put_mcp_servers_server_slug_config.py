from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.put_mcp_servers_server_slug_config_body_type_0 import PutMcpServersServerSlugConfigBodyType0
from ...models.put_mcp_servers_server_slug_config_body_type_1 import PutMcpServersServerSlugConfigBodyType1
from ...models.put_mcp_servers_server_slug_config_body_type_2 import PutMcpServersServerSlugConfigBodyType2
from ...models.put_mcp_servers_server_slug_config_body_type_3 import PutMcpServersServerSlugConfigBodyType3
from ...models.put_mcp_servers_server_slug_config_body_type_4 import PutMcpServersServerSlugConfigBodyType4
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    server_slug: str,
    *,
    body: PutMcpServersServerSlugConfigBodyType0 | PutMcpServersServerSlugConfigBodyType1 | PutMcpServersServerSlugConfigBodyType2 | PutMcpServersServerSlugConfigBodyType3 | PutMcpServersServerSlugConfigBodyType4 | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/mcp-servers/{server_slug}/config".format(server_slug=quote(str(server_slug), safe=""),),
    }

    
    if isinstance(body, PutMcpServersServerSlugConfigBodyType0):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, PutMcpServersServerSlugConfigBodyType1):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, PutMcpServersServerSlugConfigBodyType2):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, PutMcpServersServerSlugConfigBodyType3):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()



    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    server_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutMcpServersServerSlugConfigBodyType0 | PutMcpServersServerSlugConfigBodyType1 | PutMcpServersServerSlugConfigBodyType2 | PutMcpServersServerSlugConfigBodyType3 | PutMcpServersServerSlugConfigBodyType4 | Unset = UNSET,

) -> Response[Any]:
    """ 
    Args:
        server_slug (str):
        body (PutMcpServersServerSlugConfigBodyType0 | PutMcpServersServerSlugConfigBodyType1 |
            PutMcpServersServerSlugConfigBodyType2 | PutMcpServersServerSlugConfigBodyType3 |
            PutMcpServersServerSlugConfigBodyType4 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        server_slug=server_slug,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    server_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutMcpServersServerSlugConfigBodyType0 | PutMcpServersServerSlugConfigBodyType1 | PutMcpServersServerSlugConfigBodyType2 | PutMcpServersServerSlugConfigBodyType3 | PutMcpServersServerSlugConfigBodyType4 | Unset = UNSET,

) -> Response[Any]:
    """ 
    Args:
        server_slug (str):
        body (PutMcpServersServerSlugConfigBodyType0 | PutMcpServersServerSlugConfigBodyType1 |
            PutMcpServersServerSlugConfigBodyType2 | PutMcpServersServerSlugConfigBodyType3 |
            PutMcpServersServerSlugConfigBodyType4 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        server_slug=server_slug,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

