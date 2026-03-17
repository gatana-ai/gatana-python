from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deployment_log_payload_pod_info import DeploymentLogPayloadPodInfo
from ...models.schema_343 import Schema343
from ...models.schema_356 import Schema356
from ...models.schema_357 import Schema357
from ...models.schema_358 import Schema358
from ...models.schema_359 import Schema359
from ...models.schema_360 import Schema360
from ...models.schema_361 import Schema361
from ...models.schema_362 import Schema362
from ...models.schema_363 import Schema363
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    hosted_function_id: str | Unset = UNSET,
    server_slug: str | Unset = UNSET,
    pod_name: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["hostedFunctionId"] = hosted_function_id

    params["serverSlug"] = server_slug

    params["podName"] = pod_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/deployments/deployment-logs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeploymentLogPayloadPodInfo
    | Schema343
    | Schema356
    | Schema357
    | Schema358
    | Schema359
    | Schema360
    | Schema361
    | Schema362
    | Schema363
    | None
):
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> (
            DeploymentLogPayloadPodInfo
            | Schema343
            | Schema356
            | Schema357
            | Schema358
            | Schema359
            | Schema360
            | Schema361
            | Schema362
            | Schema363
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_deployment_log_payload_type_0 = Schema343.from_dict(data)

                return componentsschemas_deployment_log_payload_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_deployment_log_payload_type_1 = DeploymentLogPayloadPodInfo.from_dict(data)

                return componentsschemas_deployment_log_payload_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_deployment_log_payload_type_2 = Schema356.from_dict(data)

                return componentsschemas_deployment_log_payload_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_deployment_log_payload_type_3 = Schema357.from_dict(data)

                return componentsschemas_deployment_log_payload_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_deployment_log_payload_type_4 = Schema358.from_dict(data)

                return componentsschemas_deployment_log_payload_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_deployment_log_payload_type_5 = Schema359.from_dict(data)

                return componentsschemas_deployment_log_payload_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_deployment_log_payload_type_6 = Schema360.from_dict(data)

                return componentsschemas_deployment_log_payload_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_deployment_log_payload_type_7 = Schema361.from_dict(data)

                return componentsschemas_deployment_log_payload_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_deployment_log_payload_type_8 = Schema362.from_dict(data)

                return componentsschemas_deployment_log_payload_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_deployment_log_payload_type_9 = Schema363.from_dict(data)

            return componentsschemas_deployment_log_payload_type_9

        response_200 = _parse_response_200(response.text)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeploymentLogPayloadPodInfo
    | Schema343
    | Schema356
    | Schema357
    | Schema358
    | Schema359
    | Schema360
    | Schema361
    | Schema362
    | Schema363
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    hosted_function_id: str | Unset = UNSET,
    server_slug: str | Unset = UNSET,
    pod_name: str | Unset = UNSET,
) -> Response[
    DeploymentLogPayloadPodInfo
    | Schema343
    | Schema356
    | Schema357
    | Schema358
    | Schema359
    | Schema360
    | Schema361
    | Schema362
    | Schema363
]:
    """
    Args:
        hosted_function_id (str | Unset):
        server_slug (str | Unset):
        pod_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeploymentLogPayloadPodInfo | Schema343 | Schema356 | Schema357 | Schema358 | Schema359 | Schema360 | Schema361 | Schema362 | Schema363]
    """

    kwargs = _get_kwargs(
        hosted_function_id=hosted_function_id,
        server_slug=server_slug,
        pod_name=pod_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    hosted_function_id: str | Unset = UNSET,
    server_slug: str | Unset = UNSET,
    pod_name: str | Unset = UNSET,
) -> (
    DeploymentLogPayloadPodInfo
    | Schema343
    | Schema356
    | Schema357
    | Schema358
    | Schema359
    | Schema360
    | Schema361
    | Schema362
    | Schema363
    | None
):
    """
    Args:
        hosted_function_id (str | Unset):
        server_slug (str | Unset):
        pod_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeploymentLogPayloadPodInfo | Schema343 | Schema356 | Schema357 | Schema358 | Schema359 | Schema360 | Schema361 | Schema362 | Schema363
    """

    return sync_detailed(
        client=client,
        hosted_function_id=hosted_function_id,
        server_slug=server_slug,
        pod_name=pod_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    hosted_function_id: str | Unset = UNSET,
    server_slug: str | Unset = UNSET,
    pod_name: str | Unset = UNSET,
) -> Response[
    DeploymentLogPayloadPodInfo
    | Schema343
    | Schema356
    | Schema357
    | Schema358
    | Schema359
    | Schema360
    | Schema361
    | Schema362
    | Schema363
]:
    """
    Args:
        hosted_function_id (str | Unset):
        server_slug (str | Unset):
        pod_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeploymentLogPayloadPodInfo | Schema343 | Schema356 | Schema357 | Schema358 | Schema359 | Schema360 | Schema361 | Schema362 | Schema363]
    """

    kwargs = _get_kwargs(
        hosted_function_id=hosted_function_id,
        server_slug=server_slug,
        pod_name=pod_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    hosted_function_id: str | Unset = UNSET,
    server_slug: str | Unset = UNSET,
    pod_name: str | Unset = UNSET,
) -> (
    DeploymentLogPayloadPodInfo
    | Schema343
    | Schema356
    | Schema357
    | Schema358
    | Schema359
    | Schema360
    | Schema361
    | Schema362
    | Schema363
    | None
):
    """
    Args:
        hosted_function_id (str | Unset):
        server_slug (str | Unset):
        pod_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeploymentLogPayloadPodInfo | Schema343 | Schema356 | Schema357 | Schema358 | Schema359 | Schema360 | Schema361 | Schema362 | Schema363
    """

    return (
        await asyncio_detailed(
            client=client,
            hosted_function_id=hosted_function_id,
            server_slug=server_slug,
            pod_name=pod_name,
        )
    ).parsed
