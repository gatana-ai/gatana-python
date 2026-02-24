from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_personal_access_token_request import CreatePersonalAccessTokenRequest
from ...models.post_users_user_sub_personal_access_tokens_response_200 import PostUsersUserSubPersonalAccessTokensResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    user_sub: str,
    *,
    body: CreatePersonalAccessTokenRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/users/{user_sub}/personal-access-tokens".format(user_sub=quote(str(user_sub), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostUsersUserSubPersonalAccessTokensResponse200 | None:
    if response.status_code == 200:
        response_200 = PostUsersUserSubPersonalAccessTokensResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostUsersUserSubPersonalAccessTokensResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_sub: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreatePersonalAccessTokenRequest | Unset = UNSET,

) -> Response[PostUsersUserSubPersonalAccessTokensResponse200]:
    """ 
    Args:
        user_sub (str):
        body (CreatePersonalAccessTokenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostUsersUserSubPersonalAccessTokensResponse200]
     """


    kwargs = _get_kwargs(
        user_sub=user_sub,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    user_sub: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreatePersonalAccessTokenRequest | Unset = UNSET,

) -> PostUsersUserSubPersonalAccessTokensResponse200 | None:
    """ 
    Args:
        user_sub (str):
        body (CreatePersonalAccessTokenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostUsersUserSubPersonalAccessTokensResponse200
     """


    return sync_detailed(
        user_sub=user_sub,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    user_sub: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreatePersonalAccessTokenRequest | Unset = UNSET,

) -> Response[PostUsersUserSubPersonalAccessTokensResponse200]:
    """ 
    Args:
        user_sub (str):
        body (CreatePersonalAccessTokenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostUsersUserSubPersonalAccessTokensResponse200]
     """


    kwargs = _get_kwargs(
        user_sub=user_sub,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    user_sub: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreatePersonalAccessTokenRequest | Unset = UNSET,

) -> PostUsersUserSubPersonalAccessTokensResponse200 | None:
    """ 
    Args:
        user_sub (str):
        body (CreatePersonalAccessTokenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostUsersUserSubPersonalAccessTokensResponse200
     """


    return (await asyncio_detailed(
        user_sub=user_sub,
client=client,
body=body,

    )).parsed
