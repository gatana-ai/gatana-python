from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_mcp_servers_server_slug_credentials_profile_response_200 import GetMcpServersServerSlugCredentialsProfileResponse200
from typing import cast



def _get_kwargs(
    server_slug: str,
    *,
    profile_id: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["profileId"] = profile_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mcp-servers/{server_slug}/credentials/profile".format(server_slug=quote(str(server_slug), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetMcpServersServerSlugCredentialsProfileResponse200 | None:
    if response.status_code == 200:
        response_200 = GetMcpServersServerSlugCredentialsProfileResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetMcpServersServerSlugCredentialsProfileResponse200]:
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
    profile_id: str,

) -> Response[GetMcpServersServerSlugCredentialsProfileResponse200]:
    """ 
    Args:
        server_slug (str):
        profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMcpServersServerSlugCredentialsProfileResponse200]
     """


    kwargs = _get_kwargs(
        server_slug=server_slug,
profile_id=profile_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    server_slug: str,
    *,
    client: AuthenticatedClient | Client,
    profile_id: str,

) -> GetMcpServersServerSlugCredentialsProfileResponse200 | None:
    """ 
    Args:
        server_slug (str):
        profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMcpServersServerSlugCredentialsProfileResponse200
     """


    return sync_detailed(
        server_slug=server_slug,
client=client,
profile_id=profile_id,

    ).parsed

async def asyncio_detailed(
    server_slug: str,
    *,
    client: AuthenticatedClient | Client,
    profile_id: str,

) -> Response[GetMcpServersServerSlugCredentialsProfileResponse200]:
    """ 
    Args:
        server_slug (str):
        profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMcpServersServerSlugCredentialsProfileResponse200]
     """


    kwargs = _get_kwargs(
        server_slug=server_slug,
profile_id=profile_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    server_slug: str,
    *,
    client: AuthenticatedClient | Client,
    profile_id: str,

) -> GetMcpServersServerSlugCredentialsProfileResponse200 | None:
    """ 
    Args:
        server_slug (str):
        profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMcpServersServerSlugCredentialsProfileResponse200
     """


    return (await asyncio_detailed(
        server_slug=server_slug,
client=client,
profile_id=profile_id,

    )).parsed
