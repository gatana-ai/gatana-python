from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_mcp_servers_server_slug_credentials_copy_response_200 import PostMcpServersServerSlugCredentialsCopyResponse200
from ...models.schema_32 import Schema32
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    server_slug: str,
    *,
    id: str,
    to: Schema32,
    profile_id: str | Unset = UNSET,
    user_sub: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["id"] = id

    json_to = to.value
    params["to"] = json_to

    params["profileId"] = profile_id

    params["userSub"] = user_sub


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/mcp-servers/{server_slug}/credentials/copy".format(server_slug=quote(str(server_slug), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostMcpServersServerSlugCredentialsCopyResponse200 | None:
    if response.status_code == 200:
        response_200 = PostMcpServersServerSlugCredentialsCopyResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostMcpServersServerSlugCredentialsCopyResponse200]:
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
    id: str,
    to: Schema32,
    profile_id: str | Unset = UNSET,
    user_sub: str | Unset = UNSET,

) -> Response[PostMcpServersServerSlugCredentialsCopyResponse200]:
    """  Copy credentials to the another scope

    Args:
        server_slug (str):
        id (str): ID of the credentials to copy
        to (Schema32):
        profile_id (str | Unset): Target profile ID when copying to profile scope
        user_sub (str | Unset): Target user sub when copying to user scope which is not the
            currently authenticated user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostMcpServersServerSlugCredentialsCopyResponse200]
     """


    kwargs = _get_kwargs(
        server_slug=server_slug,
id=id,
to=to,
profile_id=profile_id,
user_sub=user_sub,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    server_slug: str,
    *,
    client: AuthenticatedClient | Client,
    id: str,
    to: Schema32,
    profile_id: str | Unset = UNSET,
    user_sub: str | Unset = UNSET,

) -> PostMcpServersServerSlugCredentialsCopyResponse200 | None:
    """  Copy credentials to the another scope

    Args:
        server_slug (str):
        id (str): ID of the credentials to copy
        to (Schema32):
        profile_id (str | Unset): Target profile ID when copying to profile scope
        user_sub (str | Unset): Target user sub when copying to user scope which is not the
            currently authenticated user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostMcpServersServerSlugCredentialsCopyResponse200
     """


    return sync_detailed(
        server_slug=server_slug,
client=client,
id=id,
to=to,
profile_id=profile_id,
user_sub=user_sub,

    ).parsed

async def asyncio_detailed(
    server_slug: str,
    *,
    client: AuthenticatedClient | Client,
    id: str,
    to: Schema32,
    profile_id: str | Unset = UNSET,
    user_sub: str | Unset = UNSET,

) -> Response[PostMcpServersServerSlugCredentialsCopyResponse200]:
    """  Copy credentials to the another scope

    Args:
        server_slug (str):
        id (str): ID of the credentials to copy
        to (Schema32):
        profile_id (str | Unset): Target profile ID when copying to profile scope
        user_sub (str | Unset): Target user sub when copying to user scope which is not the
            currently authenticated user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostMcpServersServerSlugCredentialsCopyResponse200]
     """


    kwargs = _get_kwargs(
        server_slug=server_slug,
id=id,
to=to,
profile_id=profile_id,
user_sub=user_sub,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    server_slug: str,
    *,
    client: AuthenticatedClient | Client,
    id: str,
    to: Schema32,
    profile_id: str | Unset = UNSET,
    user_sub: str | Unset = UNSET,

) -> PostMcpServersServerSlugCredentialsCopyResponse200 | None:
    """  Copy credentials to the another scope

    Args:
        server_slug (str):
        id (str): ID of the credentials to copy
        to (Schema32):
        profile_id (str | Unset): Target profile ID when copying to profile scope
        user_sub (str | Unset): Target user sub when copying to user scope which is not the
            currently authenticated user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostMcpServersServerSlugCredentialsCopyResponse200
     """


    return (await asyncio_detailed(
        server_slug=server_slug,
client=client,
id=id,
to=to,
profile_id=profile_id,
user_sub=user_sub,

    )).parsed
