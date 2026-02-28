from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.schema_51 import Schema51
from ...types import Response


def _get_kwargs(
    user_sub: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/{user_sub}".format(
            user_sub=quote(str(user_sub), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Schema51 | None:
    if response.status_code == 200:
        response_200 = Schema51.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Schema51]:
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
) -> Response[Schema51]:
    """
    Args:
        user_sub (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Schema51]
    """

    kwargs = _get_kwargs(
        user_sub=user_sub,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_sub: str,
    *,
    client: AuthenticatedClient | Client,
) -> Schema51 | None:
    """
    Args:
        user_sub (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Schema51
    """

    return sync_detailed(
        user_sub=user_sub,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_sub: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Schema51]:
    """
    Args:
        user_sub (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Schema51]
    """

    kwargs = _get_kwargs(
        user_sub=user_sub,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_sub: str,
    *,
    client: AuthenticatedClient | Client,
) -> Schema51 | None:
    """
    Args:
        user_sub (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Schema51
    """

    return (
        await asyncio_detailed(
            user_sub=user_sub,
            client=client,
        )
    ).parsed
