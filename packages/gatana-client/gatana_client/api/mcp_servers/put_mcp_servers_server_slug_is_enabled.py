from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.put_mcp_servers_server_slug_is_enabled_body import PutMcpServersServerSlugIsEnabledBody
from ...models.put_mcp_servers_server_slug_is_enabled_response_200 import PutMcpServersServerSlugIsEnabledResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    server_slug: str,
    *,
    body: PutMcpServersServerSlugIsEnabledBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/mcp-servers/{server_slug}/isEnabled".format(server_slug=quote(str(server_slug), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PutMcpServersServerSlugIsEnabledResponse200 | None:
    if response.status_code == 200:
        response_200 = PutMcpServersServerSlugIsEnabledResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PutMcpServersServerSlugIsEnabledResponse200]:
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
    body: PutMcpServersServerSlugIsEnabledBody | Unset = UNSET,

) -> Response[PutMcpServersServerSlugIsEnabledResponse200]:
    """ 
    Args:
        server_slug (str):
        body (PutMcpServersServerSlugIsEnabledBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutMcpServersServerSlugIsEnabledResponse200]
     """


    kwargs = _get_kwargs(
        server_slug=server_slug,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    server_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutMcpServersServerSlugIsEnabledBody | Unset = UNSET,

) -> PutMcpServersServerSlugIsEnabledResponse200 | None:
    """ 
    Args:
        server_slug (str):
        body (PutMcpServersServerSlugIsEnabledBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutMcpServersServerSlugIsEnabledResponse200
     """


    return sync_detailed(
        server_slug=server_slug,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    server_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutMcpServersServerSlugIsEnabledBody | Unset = UNSET,

) -> Response[PutMcpServersServerSlugIsEnabledResponse200]:
    """ 
    Args:
        server_slug (str):
        body (PutMcpServersServerSlugIsEnabledBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutMcpServersServerSlugIsEnabledResponse200]
     """


    kwargs = _get_kwargs(
        server_slug=server_slug,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    server_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutMcpServersServerSlugIsEnabledBody | Unset = UNSET,

) -> PutMcpServersServerSlugIsEnabledResponse200 | None:
    """ 
    Args:
        server_slug (str):
        body (PutMcpServersServerSlugIsEnabledBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutMcpServersServerSlugIsEnabledResponse200
     """


    return (await asyncio_detailed(
        server_slug=server_slug,
client=client,
body=body,

    )).parsed
