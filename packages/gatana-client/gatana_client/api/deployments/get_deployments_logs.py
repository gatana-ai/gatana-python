from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_deployments_logs_previous import GetDeploymentsLogsPrevious
from ...models.get_deployments_logs_response_200 import GetDeploymentsLogsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    pod_name: str,
    previous: GetDeploymentsLogsPrevious | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["podName"] = pod_name

    json_previous: str | Unset = UNSET
    if not isinstance(previous, Unset):
        json_previous = previous.value

    params["previous"] = json_previous

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/deployments/logs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetDeploymentsLogsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetDeploymentsLogsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetDeploymentsLogsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    pod_name: str,
    previous: GetDeploymentsLogsPrevious | Unset = UNSET,
) -> Response[GetDeploymentsLogsResponse200]:
    """
    Args:
        pod_name (str):
        previous (GetDeploymentsLogsPrevious | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDeploymentsLogsResponse200]
    """

    kwargs = _get_kwargs(
        pod_name=pod_name,
        previous=previous,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    pod_name: str,
    previous: GetDeploymentsLogsPrevious | Unset = UNSET,
) -> GetDeploymentsLogsResponse200 | None:
    """
    Args:
        pod_name (str):
        previous (GetDeploymentsLogsPrevious | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDeploymentsLogsResponse200
    """

    return sync_detailed(
        client=client,
        pod_name=pod_name,
        previous=previous,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    pod_name: str,
    previous: GetDeploymentsLogsPrevious | Unset = UNSET,
) -> Response[GetDeploymentsLogsResponse200]:
    """
    Args:
        pod_name (str):
        previous (GetDeploymentsLogsPrevious | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDeploymentsLogsResponse200]
    """

    kwargs = _get_kwargs(
        pod_name=pod_name,
        previous=previous,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    pod_name: str,
    previous: GetDeploymentsLogsPrevious | Unset = UNSET,
) -> GetDeploymentsLogsResponse200 | None:
    """
    Args:
        pod_name (str):
        previous (GetDeploymentsLogsPrevious | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDeploymentsLogsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            pod_name=pod_name,
            previous=previous,
        )
    ).parsed
