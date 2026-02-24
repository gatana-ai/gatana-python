from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_profiles_profile_id_claim_mappings_body import PostProfilesProfileIdClaimMappingsBody
from ...models.post_profiles_profile_id_claim_mappings_response_200 import PostProfilesProfileIdClaimMappingsResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    profile_id: str,
    *,
    body: PostProfilesProfileIdClaimMappingsBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/profiles/{profile_id}/claim-mappings".format(profile_id=quote(str(profile_id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostProfilesProfileIdClaimMappingsResponse200 | None:
    if response.status_code == 200:
        response_200 = PostProfilesProfileIdClaimMappingsResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostProfilesProfileIdClaimMappingsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    profile_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostProfilesProfileIdClaimMappingsBody | Unset = UNSET,

) -> Response[PostProfilesProfileIdClaimMappingsResponse200]:
    """ 
    Args:
        profile_id (str):
        body (PostProfilesProfileIdClaimMappingsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostProfilesProfileIdClaimMappingsResponse200]
     """


    kwargs = _get_kwargs(
        profile_id=profile_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    profile_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostProfilesProfileIdClaimMappingsBody | Unset = UNSET,

) -> PostProfilesProfileIdClaimMappingsResponse200 | None:
    """ 
    Args:
        profile_id (str):
        body (PostProfilesProfileIdClaimMappingsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostProfilesProfileIdClaimMappingsResponse200
     """


    return sync_detailed(
        profile_id=profile_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    profile_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostProfilesProfileIdClaimMappingsBody | Unset = UNSET,

) -> Response[PostProfilesProfileIdClaimMappingsResponse200]:
    """ 
    Args:
        profile_id (str):
        body (PostProfilesProfileIdClaimMappingsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostProfilesProfileIdClaimMappingsResponse200]
     """


    kwargs = _get_kwargs(
        profile_id=profile_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    profile_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostProfilesProfileIdClaimMappingsBody | Unset = UNSET,

) -> PostProfilesProfileIdClaimMappingsResponse200 | None:
    """ 
    Args:
        profile_id (str):
        body (PostProfilesProfileIdClaimMappingsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostProfilesProfileIdClaimMappingsResponse200
     """


    return (await asyncio_detailed(
        profile_id=profile_id,
client=client,
body=body,

    )).parsed
