from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_mcp_servers_server_slug_credentials_user_response_200 import GetMcpServersServerSlugCredentialsUserResponse200
from typing import cast



def _get_kwargs(
    server_slug: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mcp-servers/{server_slug}/credentials/user".format(server_slug=quote(str(server_slug), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetMcpServersServerSlugCredentialsUserResponse200 | None:
    if response.status_code == 200:
        response_200 = GetMcpServersServerSlugCredentialsUserResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetMcpServersServerSlugCredentialsUserResponse200]:
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

) -> Response[GetMcpServersServerSlugCredentialsUserResponse200]:
    """ 
    Args:
        server_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMcpServersServerSlugCredentialsUserResponse200]
     """


    kwargs = _get_kwargs(
        server_slug=server_slug,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    server_slug: str,
    *,
    client: AuthenticatedClient | Client,

) -> GetMcpServersServerSlugCredentialsUserResponse200 | None:
    """ 
    Args:
        server_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMcpServersServerSlugCredentialsUserResponse200
     """


    return sync_detailed(
        server_slug=server_slug,
client=client,

    ).parsed

async def asyncio_detailed(
    server_slug: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetMcpServersServerSlugCredentialsUserResponse200]:
    """ 
    Args:
        server_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMcpServersServerSlugCredentialsUserResponse200]
     """


    kwargs = _get_kwargs(
        server_slug=server_slug,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    server_slug: str,
    *,
    client: AuthenticatedClient | Client,

) -> GetMcpServersServerSlugCredentialsUserResponse200 | None:
    """ 
    Args:
        server_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMcpServersServerSlugCredentialsUserResponse200
     """


    return (await asyncio_detailed(
        server_slug=server_slug,
client=client,

    )).parsed
