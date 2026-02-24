from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_teams_team_id_invitations_body import PostTeamsTeamIdInvitationsBody
from ...models.post_teams_team_id_invitations_response_200 import PostTeamsTeamIdInvitationsResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    team_id: str,
    *,
    body: PostTeamsTeamIdInvitationsBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/teams/{team_id}/invitations".format(team_id=quote(str(team_id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostTeamsTeamIdInvitationsResponse200 | None:
    if response.status_code == 200:
        response_200 = PostTeamsTeamIdInvitationsResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostTeamsTeamIdInvitationsResponse200]:
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
    body: PostTeamsTeamIdInvitationsBody | Unset = UNSET,

) -> Response[PostTeamsTeamIdInvitationsResponse200]:
    """ 
    Args:
        team_id (str):
        body (PostTeamsTeamIdInvitationsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostTeamsTeamIdInvitationsResponse200]
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
    body: PostTeamsTeamIdInvitationsBody | Unset = UNSET,

) -> PostTeamsTeamIdInvitationsResponse200 | None:
    """ 
    Args:
        team_id (str):
        body (PostTeamsTeamIdInvitationsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostTeamsTeamIdInvitationsResponse200
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
    body: PostTeamsTeamIdInvitationsBody | Unset = UNSET,

) -> Response[PostTeamsTeamIdInvitationsResponse200]:
    """ 
    Args:
        team_id (str):
        body (PostTeamsTeamIdInvitationsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostTeamsTeamIdInvitationsResponse200]
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
    body: PostTeamsTeamIdInvitationsBody | Unset = UNSET,

) -> PostTeamsTeamIdInvitationsResponse200 | None:
    """ 
    Args:
        team_id (str):
        body (PostTeamsTeamIdInvitationsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostTeamsTeamIdInvitationsResponse200
     """


    return (await asyncio_detailed(
        team_id=team_id,
client=client,
body=body,

    )).parsed
