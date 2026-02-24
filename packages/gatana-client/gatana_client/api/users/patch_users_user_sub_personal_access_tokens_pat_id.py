from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.patch_users_user_sub_personal_access_tokens_pat_id_response_200 import PatchUsersUserSubPersonalAccessTokensPatIdResponse200
from ...models.update_personal_access_token_request import UpdatePersonalAccessTokenRequest
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    user_sub: str,
    pat_id: str,
    *,
    body: UpdatePersonalAccessTokenRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/users/{user_sub}/personal-access-tokens/{pat_id}".format(user_sub=quote(str(user_sub), safe=""),pat_id=quote(str(pat_id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchUsersUserSubPersonalAccessTokensPatIdResponse200 | None:
    if response.status_code == 200:
        response_200 = PatchUsersUserSubPersonalAccessTokensPatIdResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchUsersUserSubPersonalAccessTokensPatIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_sub: str,
    pat_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePersonalAccessTokenRequest | Unset = UNSET,

) -> Response[PatchUsersUserSubPersonalAccessTokensPatIdResponse200]:
    """ 
    Args:
        user_sub (str):
        pat_id (str):
        body (UpdatePersonalAccessTokenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchUsersUserSubPersonalAccessTokensPatIdResponse200]
     """


    kwargs = _get_kwargs(
        user_sub=user_sub,
pat_id=pat_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    user_sub: str,
    pat_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePersonalAccessTokenRequest | Unset = UNSET,

) -> PatchUsersUserSubPersonalAccessTokensPatIdResponse200 | None:
    """ 
    Args:
        user_sub (str):
        pat_id (str):
        body (UpdatePersonalAccessTokenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchUsersUserSubPersonalAccessTokensPatIdResponse200
     """


    return sync_detailed(
        user_sub=user_sub,
pat_id=pat_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    user_sub: str,
    pat_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePersonalAccessTokenRequest | Unset = UNSET,

) -> Response[PatchUsersUserSubPersonalAccessTokensPatIdResponse200]:
    """ 
    Args:
        user_sub (str):
        pat_id (str):
        body (UpdatePersonalAccessTokenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchUsersUserSubPersonalAccessTokensPatIdResponse200]
     """


    kwargs = _get_kwargs(
        user_sub=user_sub,
pat_id=pat_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    user_sub: str,
    pat_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePersonalAccessTokenRequest | Unset = UNSET,

) -> PatchUsersUserSubPersonalAccessTokensPatIdResponse200 | None:
    """ 
    Args:
        user_sub (str):
        pat_id (str):
        body (UpdatePersonalAccessTokenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchUsersUserSubPersonalAccessTokensPatIdResponse200
     """


    return (await asyncio_detailed(
        user_sub=user_sub,
pat_id=pat_id,
client=client,
body=body,

    )).parsed
