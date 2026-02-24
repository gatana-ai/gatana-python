from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_sandbox_id_audit_logs_id_response_200 import GetSandboxIdAuditLogsIdResponse200
from ...types import Response


def _get_kwargs(
    sandbox_id: str,
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/{sandbox_id}/audit-logs/{id}".format(
            sandbox_id=quote(str(sandbox_id), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetSandboxIdAuditLogsIdResponse200 | None:
    if response.status_code == 200:
        response_200 = GetSandboxIdAuditLogsIdResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetSandboxIdAuditLogsIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sandbox_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetSandboxIdAuditLogsIdResponse200]:
    """
    Args:
        sandbox_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSandboxIdAuditLogsIdResponse200]
    """

    kwargs = _get_kwargs(
        sandbox_id=sandbox_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sandbox_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetSandboxIdAuditLogsIdResponse200 | None:
    """
    Args:
        sandbox_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSandboxIdAuditLogsIdResponse200
    """

    return sync_detailed(
        sandbox_id=sandbox_id,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    sandbox_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetSandboxIdAuditLogsIdResponse200]:
    """
    Args:
        sandbox_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSandboxIdAuditLogsIdResponse200]
    """

    kwargs = _get_kwargs(
        sandbox_id=sandbox_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sandbox_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetSandboxIdAuditLogsIdResponse200 | None:
    """
    Args:
        sandbox_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSandboxIdAuditLogsIdResponse200
    """

    return (
        await asyncio_detailed(
            sandbox_id=sandbox_id,
            id=id,
            client=client,
        )
    ).parsed
