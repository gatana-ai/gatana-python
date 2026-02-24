from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_teams_team_id_claim_mappings_mapping_id_response_200 import DeleteTeamsTeamIdClaimMappingsMappingIdResponse200
from typing import cast



def _get_kwargs(
    team_id: str,
    mapping_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/teams/{team_id}/claim-mappings/{mapping_id}".format(team_id=quote(str(team_id), safe=""),mapping_id=quote(str(mapping_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteTeamsTeamIdClaimMappingsMappingIdResponse200 | None:
    if response.status_code == 200:
        response_200 = DeleteTeamsTeamIdClaimMappingsMappingIdResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteTeamsTeamIdClaimMappingsMappingIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    team_id: str,
    mapping_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[DeleteTeamsTeamIdClaimMappingsMappingIdResponse200]:
    """ 
    Args:
        team_id (str):
        mapping_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteTeamsTeamIdClaimMappingsMappingIdResponse200]
     """


    kwargs = _get_kwargs(
        team_id=team_id,
mapping_id=mapping_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    team_id: str,
    mapping_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> DeleteTeamsTeamIdClaimMappingsMappingIdResponse200 | None:
    """ 
    Args:
        team_id (str):
        mapping_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteTeamsTeamIdClaimMappingsMappingIdResponse200
     """


    return sync_detailed(
        team_id=team_id,
mapping_id=mapping_id,
client=client,

    ).parsed

async def asyncio_detailed(
    team_id: str,
    mapping_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[DeleteTeamsTeamIdClaimMappingsMappingIdResponse200]:
    """ 
    Args:
        team_id (str):
        mapping_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteTeamsTeamIdClaimMappingsMappingIdResponse200]
     """


    kwargs = _get_kwargs(
        team_id=team_id,
mapping_id=mapping_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    team_id: str,
    mapping_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> DeleteTeamsTeamIdClaimMappingsMappingIdResponse200 | None:
    """ 
    Args:
        team_id (str):
        mapping_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteTeamsTeamIdClaimMappingsMappingIdResponse200
     """


    return (await asyncio_detailed(
        team_id=team_id,
mapping_id=mapping_id,
client=client,

    )).parsed
