from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_mcp_servers_server_slug_tools_tool_name_call_body import (
    PostMcpServersServerSlugToolsToolNameCallBody,
)
from ...models.post_mcp_servers_server_slug_tools_tool_name_call_response_200 import (
    PostMcpServersServerSlugToolsToolNameCallResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    server_slug: str,
    tool_name: str,
    *,
    body: PostMcpServersServerSlugToolsToolNameCallBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/mcp-servers/{server_slug}/tools/{tool_name}/call".format(
            server_slug=quote(str(server_slug), safe=""),
            tool_name=quote(str(tool_name), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PostMcpServersServerSlugToolsToolNameCallResponse200 | None:
    if response.status_code == 200:
        response_200 = PostMcpServersServerSlugToolsToolNameCallResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PostMcpServersServerSlugToolsToolNameCallResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    server_slug: str,
    tool_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostMcpServersServerSlugToolsToolNameCallBody | Unset = UNSET,
) -> Response[PostMcpServersServerSlugToolsToolNameCallResponse200]:
    """
    Args:
        server_slug (str):
        tool_name (str):
        body (PostMcpServersServerSlugToolsToolNameCallBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostMcpServersServerSlugToolsToolNameCallResponse200]
    """

    kwargs = _get_kwargs(
        server_slug=server_slug,
        tool_name=tool_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    server_slug: str,
    tool_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostMcpServersServerSlugToolsToolNameCallBody | Unset = UNSET,
) -> PostMcpServersServerSlugToolsToolNameCallResponse200 | None:
    """
    Args:
        server_slug (str):
        tool_name (str):
        body (PostMcpServersServerSlugToolsToolNameCallBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostMcpServersServerSlugToolsToolNameCallResponse200
    """

    return sync_detailed(
        server_slug=server_slug,
        tool_name=tool_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    server_slug: str,
    tool_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostMcpServersServerSlugToolsToolNameCallBody | Unset = UNSET,
) -> Response[PostMcpServersServerSlugToolsToolNameCallResponse200]:
    """
    Args:
        server_slug (str):
        tool_name (str):
        body (PostMcpServersServerSlugToolsToolNameCallBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostMcpServersServerSlugToolsToolNameCallResponse200]
    """

    kwargs = _get_kwargs(
        server_slug=server_slug,
        tool_name=tool_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server_slug: str,
    tool_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostMcpServersServerSlugToolsToolNameCallBody | Unset = UNSET,
) -> PostMcpServersServerSlugToolsToolNameCallResponse200 | None:
    """
    Args:
        server_slug (str):
        tool_name (str):
        body (PostMcpServersServerSlugToolsToolNameCallBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostMcpServersServerSlugToolsToolNameCallResponse200
    """

    return (
        await asyncio_detailed(
            server_slug=server_slug,
            tool_name=tool_name,
            client=client,
            body=body,
        )
    ).parsed
