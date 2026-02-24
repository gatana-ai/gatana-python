from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_mcp_servers_server_slug_credentials_authorize_url_redirect import GetMcpServersServerSlugCredentialsAuthorizeUrlRedirect
from ...models.get_mcp_servers_server_slug_credentials_authorize_url_response_200 import GetMcpServersServerSlugCredentialsAuthorizeUrlResponse200
from ...models.get_mcp_servers_server_slug_credentials_authorize_url_return_to import GetMcpServersServerSlugCredentialsAuthorizeUrlReturnTo
from ...models.schema_32 import Schema32
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    server_slug: str,
    *,
    scope: Schema32 | Unset = UNSET,
    redirect: GetMcpServersServerSlugCredentialsAuthorizeUrlRedirect | Unset = UNSET,
    return_to: GetMcpServersServerSlugCredentialsAuthorizeUrlReturnTo | Unset = UNSET,
    profile_id: str | Unset = UNSET,
    user_sub: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_scope: str | Unset = UNSET
    if not isinstance(scope, Unset):
        json_scope = scope.value

    params["scope"] = json_scope

    json_redirect: str | Unset = UNSET
    if not isinstance(redirect, Unset):
        json_redirect = redirect.value

    params["redirect"] = json_redirect

    json_return_to: str | Unset = UNSET
    if not isinstance(return_to, Unset):
        json_return_to = return_to.value

    params["returnTo"] = json_return_to

    params["profileId"] = profile_id

    params["userSub"] = user_sub


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mcp-servers/{server_slug}/credentials/authorize-url".format(server_slug=quote(str(server_slug), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetMcpServersServerSlugCredentialsAuthorizeUrlResponse200 | None:
    if response.status_code == 200:
        response_200 = GetMcpServersServerSlugCredentialsAuthorizeUrlResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetMcpServersServerSlugCredentialsAuthorizeUrlResponse200]:
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
    scope: Schema32 | Unset = UNSET,
    redirect: GetMcpServersServerSlugCredentialsAuthorizeUrlRedirect | Unset = UNSET,
    return_to: GetMcpServersServerSlugCredentialsAuthorizeUrlReturnTo | Unset = UNSET,
    profile_id: str | Unset = UNSET,
    user_sub: str | Unset = UNSET,

) -> Response[GetMcpServersServerSlugCredentialsAuthorizeUrlResponse200]:
    """  Get an out-of-band OAuth URL which can be opened in any browser on any device to provide
    authorization credentials for this request's authenticated user. The generated URL will not require
    user to sign-in to Gatana; instead it will directly start the OAuth authorization flow with the
    remote MCP server.

    Args:
        server_slug (str):
        scope (Schema32 | Unset):
        redirect (GetMcpServersServerSlugCredentialsAuthorizeUrlRedirect | Unset):
        return_to (GetMcpServersServerSlugCredentialsAuthorizeUrlReturnTo | Unset):
        profile_id (str | Unset):
        user_sub (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMcpServersServerSlugCredentialsAuthorizeUrlResponse200]
     """


    kwargs = _get_kwargs(
        server_slug=server_slug,
scope=scope,
redirect=redirect,
return_to=return_to,
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
    scope: Schema32 | Unset = UNSET,
    redirect: GetMcpServersServerSlugCredentialsAuthorizeUrlRedirect | Unset = UNSET,
    return_to: GetMcpServersServerSlugCredentialsAuthorizeUrlReturnTo | Unset = UNSET,
    profile_id: str | Unset = UNSET,
    user_sub: str | Unset = UNSET,

) -> GetMcpServersServerSlugCredentialsAuthorizeUrlResponse200 | None:
    """  Get an out-of-band OAuth URL which can be opened in any browser on any device to provide
    authorization credentials for this request's authenticated user. The generated URL will not require
    user to sign-in to Gatana; instead it will directly start the OAuth authorization flow with the
    remote MCP server.

    Args:
        server_slug (str):
        scope (Schema32 | Unset):
        redirect (GetMcpServersServerSlugCredentialsAuthorizeUrlRedirect | Unset):
        return_to (GetMcpServersServerSlugCredentialsAuthorizeUrlReturnTo | Unset):
        profile_id (str | Unset):
        user_sub (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMcpServersServerSlugCredentialsAuthorizeUrlResponse200
     """


    return sync_detailed(
        server_slug=server_slug,
client=client,
scope=scope,
redirect=redirect,
return_to=return_to,
profile_id=profile_id,
user_sub=user_sub,

    ).parsed

async def asyncio_detailed(
    server_slug: str,
    *,
    client: AuthenticatedClient | Client,
    scope: Schema32 | Unset = UNSET,
    redirect: GetMcpServersServerSlugCredentialsAuthorizeUrlRedirect | Unset = UNSET,
    return_to: GetMcpServersServerSlugCredentialsAuthorizeUrlReturnTo | Unset = UNSET,
    profile_id: str | Unset = UNSET,
    user_sub: str | Unset = UNSET,

) -> Response[GetMcpServersServerSlugCredentialsAuthorizeUrlResponse200]:
    """  Get an out-of-band OAuth URL which can be opened in any browser on any device to provide
    authorization credentials for this request's authenticated user. The generated URL will not require
    user to sign-in to Gatana; instead it will directly start the OAuth authorization flow with the
    remote MCP server.

    Args:
        server_slug (str):
        scope (Schema32 | Unset):
        redirect (GetMcpServersServerSlugCredentialsAuthorizeUrlRedirect | Unset):
        return_to (GetMcpServersServerSlugCredentialsAuthorizeUrlReturnTo | Unset):
        profile_id (str | Unset):
        user_sub (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMcpServersServerSlugCredentialsAuthorizeUrlResponse200]
     """


    kwargs = _get_kwargs(
        server_slug=server_slug,
scope=scope,
redirect=redirect,
return_to=return_to,
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
    scope: Schema32 | Unset = UNSET,
    redirect: GetMcpServersServerSlugCredentialsAuthorizeUrlRedirect | Unset = UNSET,
    return_to: GetMcpServersServerSlugCredentialsAuthorizeUrlReturnTo | Unset = UNSET,
    profile_id: str | Unset = UNSET,
    user_sub: str | Unset = UNSET,

) -> GetMcpServersServerSlugCredentialsAuthorizeUrlResponse200 | None:
    """  Get an out-of-band OAuth URL which can be opened in any browser on any device to provide
    authorization credentials for this request's authenticated user. The generated URL will not require
    user to sign-in to Gatana; instead it will directly start the OAuth authorization flow with the
    remote MCP server.

    Args:
        server_slug (str):
        scope (Schema32 | Unset):
        redirect (GetMcpServersServerSlugCredentialsAuthorizeUrlRedirect | Unset):
        return_to (GetMcpServersServerSlugCredentialsAuthorizeUrlReturnTo | Unset):
        profile_id (str | Unset):
        user_sub (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMcpServersServerSlugCredentialsAuthorizeUrlResponse200
     """


    return (await asyncio_detailed(
        server_slug=server_slug,
client=client,
scope=scope,
redirect=redirect,
return_to=return_to,
profile_id=profile_id,
user_sub=user_sub,

    )).parsed
