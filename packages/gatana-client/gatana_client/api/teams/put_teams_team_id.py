from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.put_teams_team_id_body import PutTeamsTeamIdBody
from ...models.schema_67 import Schema67
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    team_id: str,
    *,
    body: PutTeamsTeamIdBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/teams/{team_id}".format(team_id=quote(str(team_id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Schema67 | None:
    if response.status_code == 200:
        response_200 = Schema67.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Schema67]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    team_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutTeamsTeamIdBody | Unset = UNSET,

) -> Response[Schema67]:
    """ 
    Args:
        team_id (str):
        body (PutTeamsTeamIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Schema67]
     """


    kwargs = _get_kwargs(
        team_id=team_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    team_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutTeamsTeamIdBody | Unset = UNSET,

) -> Schema67 | None:
    """ 
    Args:
        team_id (str):
        body (PutTeamsTeamIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Schema67
     """


    return sync_detailed(
        team_id=team_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    team_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutTeamsTeamIdBody | Unset = UNSET,

) -> Response[Schema67]:
    """ 
    Args:
        team_id (str):
        body (PutTeamsTeamIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Schema67]
     """


    kwargs = _get_kwargs(
        team_id=team_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    team_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutTeamsTeamIdBody | Unset = UNSET,

) -> Schema67 | None:
    """ 
    Args:
        team_id (str):
        body (PutTeamsTeamIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Schema67
     """


    return (await asyncio_detailed(
        team_id=team_id,
client=client,
body=body,

    )).parsed
