import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sandbox_audit_log import SandboxAuditLog
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    event_name: str | Unset = UNSET,
    start_date: datetime.datetime | Unset = UNSET,
    end_date: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    params["eventName"] = event_name

    json_start_date: str | Unset = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    json_end_date: str | Unset = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["endDate"] = json_end_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/audit-logs",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SandboxAuditLog | None:
    if response.status_code == 200:
        response_200 = SandboxAuditLog.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SandboxAuditLog]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    event_name: str | Unset = UNSET,
    start_date: datetime.datetime | Unset = UNSET,
    end_date: datetime.datetime | Unset = UNSET,
) -> Response[SandboxAuditLog]:
    """
    Args:
        page (str | Unset):
        limit (str | Unset):
        event_name (str | Unset):
        start_date (datetime.datetime | Unset):
        end_date (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SandboxAuditLog]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        event_name=event_name,
        start_date=start_date,
        end_date=end_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    event_name: str | Unset = UNSET,
    start_date: datetime.datetime | Unset = UNSET,
    end_date: datetime.datetime | Unset = UNSET,
) -> SandboxAuditLog | None:
    """
    Args:
        page (str | Unset):
        limit (str | Unset):
        event_name (str | Unset):
        start_date (datetime.datetime | Unset):
        end_date (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SandboxAuditLog
    """

    return sync_detailed(
        client=client,
        page=page,
        limit=limit,
        event_name=event_name,
        start_date=start_date,
        end_date=end_date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    event_name: str | Unset = UNSET,
    start_date: datetime.datetime | Unset = UNSET,
    end_date: datetime.datetime | Unset = UNSET,
) -> Response[SandboxAuditLog]:
    """
    Args:
        page (str | Unset):
        limit (str | Unset):
        event_name (str | Unset):
        start_date (datetime.datetime | Unset):
        end_date (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SandboxAuditLog]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        event_name=event_name,
        start_date=start_date,
        end_date=end_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    event_name: str | Unset = UNSET,
    start_date: datetime.datetime | Unset = UNSET,
    end_date: datetime.datetime | Unset = UNSET,
) -> SandboxAuditLog | None:
    """
    Args:
        page (str | Unset):
        limit (str | Unset):
        event_name (str | Unset):
        start_date (datetime.datetime | Unset):
        end_date (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SandboxAuditLog
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            limit=limit,
            event_name=event_name,
            start_date=start_date,
            end_date=end_date,
        )
    ).parsed
