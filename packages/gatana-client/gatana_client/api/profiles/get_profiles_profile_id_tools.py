from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_profiles_profile_id_tools_response_200 import GetProfilesProfileIdToolsResponse200
from typing import cast



def _get_kwargs(
    profile_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/profiles/{profile_id}/tools".format(profile_id=quote(str(profile_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetProfilesProfileIdToolsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetProfilesProfileIdToolsResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetProfilesProfileIdToolsResponse200]:
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

) -> Response[GetProfilesProfileIdToolsResponse200]:
    """ 
    Args:
        profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProfilesProfileIdToolsResponse200]
     """


    kwargs = _get_kwargs(
        profile_id=profile_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    profile_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> GetProfilesProfileIdToolsResponse200 | None:
    """ 
    Args:
        profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProfilesProfileIdToolsResponse200
     """


    return sync_detailed(
        profile_id=profile_id,
client=client,

    ).parsed

async def asyncio_detailed(
    profile_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetProfilesProfileIdToolsResponse200]:
    """ 
    Args:
        profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProfilesProfileIdToolsResponse200]
     """


    kwargs = _get_kwargs(
        profile_id=profile_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    profile_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> GetProfilesProfileIdToolsResponse200 | None:
    """ 
    Args:
        profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProfilesProfileIdToolsResponse200
     """


    return (await asyncio_detailed(
        profile_id=profile_id,
client=client,

    )).parsed
