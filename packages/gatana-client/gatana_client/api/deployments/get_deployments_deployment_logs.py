from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deployment_log_payload_type_0 import DeploymentLogPayloadType0
from ...models.deployment_log_payload_type_1 import DeploymentLogPayloadType1
from ...models.deployment_log_payload_type_2 import DeploymentLogPayloadType2
from ...models.deployment_log_payload_type_3 import DeploymentLogPayloadType3
from ...models.deployment_log_payload_type_4 import DeploymentLogPayloadType4
from ...models.deployment_log_payload_type_5 import DeploymentLogPayloadType5
from ...models.deployment_log_payload_type_6 import DeploymentLogPayloadType6
from ...models.deployment_log_payload_type_7 import DeploymentLogPayloadType7
from ...models.deployment_log_payload_type_8 import DeploymentLogPayloadType8
from ...models.deployment_log_payload_type_9 import DeploymentLogPayloadType9
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    hosted_function_id: str | Unset = UNSET,
    server_slug: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["hostedFunctionId"] = hosted_function_id

    params["serverSlug"] = server_slug

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
    DeploymentLogPayloadType0
    | DeploymentLogPayloadType1
    | DeploymentLogPayloadType2
    | DeploymentLogPayloadType3
    | DeploymentLogPayloadType4
    | DeploymentLogPayloadType5
    | DeploymentLogPayloadType6
    | DeploymentLogPayloadType7
    | DeploymentLogPayloadType8
    | DeploymentLogPayloadType9
    | None
):
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> (
            DeploymentLogPayloadType0
            | DeploymentLogPayloadType1
            | DeploymentLogPayloadType2
            | DeploymentLogPayloadType3
            | DeploymentLogPayloadType4
            | DeploymentLogPayloadType5
            | DeploymentLogPayloadType6
            | DeploymentLogPayloadType7
            | DeploymentLogPayloadType8
            | DeploymentLogPayloadType9
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_deployment_log_payload_type_0 = DeploymentLogPayloadType0.from_dict(data)

                return componentsschemas_deployment_log_payload_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_deployment_log_payload_type_1 = DeploymentLogPayloadType1.from_dict(data)

                return componentsschemas_deployment_log_payload_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_deployment_log_payload_type_2 = DeploymentLogPayloadType2.from_dict(data)

                return componentsschemas_deployment_log_payload_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_deployment_log_payload_type_3 = DeploymentLogPayloadType3.from_dict(data)

                return componentsschemas_deployment_log_payload_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_deployment_log_payload_type_4 = DeploymentLogPayloadType4.from_dict(data)

                return componentsschemas_deployment_log_payload_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_deployment_log_payload_type_5 = DeploymentLogPayloadType5.from_dict(data)

                return componentsschemas_deployment_log_payload_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_deployment_log_payload_type_6 = DeploymentLogPayloadType6.from_dict(data)

                return componentsschemas_deployment_log_payload_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_deployment_log_payload_type_7 = DeploymentLogPayloadType7.from_dict(data)

                return componentsschemas_deployment_log_payload_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_deployment_log_payload_type_8 = DeploymentLogPayloadType8.from_dict(data)

                return componentsschemas_deployment_log_payload_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_deployment_log_payload_type_9 = DeploymentLogPayloadType9.from_dict(data)

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
    DeploymentLogPayloadType0
    | DeploymentLogPayloadType1
    | DeploymentLogPayloadType2
    | DeploymentLogPayloadType3
    | DeploymentLogPayloadType4
    | DeploymentLogPayloadType5
    | DeploymentLogPayloadType6
    | DeploymentLogPayloadType7
    | DeploymentLogPayloadType8
    | DeploymentLogPayloadType9
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
) -> Response[
    DeploymentLogPayloadType0
    | DeploymentLogPayloadType1
    | DeploymentLogPayloadType2
    | DeploymentLogPayloadType3
    | DeploymentLogPayloadType4
    | DeploymentLogPayloadType5
    | DeploymentLogPayloadType6
    | DeploymentLogPayloadType7
    | DeploymentLogPayloadType8
    | DeploymentLogPayloadType9
]:
    """
    Args:
        hosted_function_id (str | Unset):
        server_slug (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeploymentLogPayloadType0 | DeploymentLogPayloadType1 | DeploymentLogPayloadType2 | DeploymentLogPayloadType3 | DeploymentLogPayloadType4 | DeploymentLogPayloadType5 | DeploymentLogPayloadType6 | DeploymentLogPayloadType7 | DeploymentLogPayloadType8 | DeploymentLogPayloadType9]
    """

    kwargs = _get_kwargs(
        hosted_function_id=hosted_function_id,
        server_slug=server_slug,
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
) -> (
    DeploymentLogPayloadType0
    | DeploymentLogPayloadType1
    | DeploymentLogPayloadType2
    | DeploymentLogPayloadType3
    | DeploymentLogPayloadType4
    | DeploymentLogPayloadType5
    | DeploymentLogPayloadType6
    | DeploymentLogPayloadType7
    | DeploymentLogPayloadType8
    | DeploymentLogPayloadType9
    | None
):
    """
    Args:
        hosted_function_id (str | Unset):
        server_slug (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeploymentLogPayloadType0 | DeploymentLogPayloadType1 | DeploymentLogPayloadType2 | DeploymentLogPayloadType3 | DeploymentLogPayloadType4 | DeploymentLogPayloadType5 | DeploymentLogPayloadType6 | DeploymentLogPayloadType7 | DeploymentLogPayloadType8 | DeploymentLogPayloadType9
    """

    return sync_detailed(
        client=client,
        hosted_function_id=hosted_function_id,
        server_slug=server_slug,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    hosted_function_id: str | Unset = UNSET,
    server_slug: str | Unset = UNSET,
) -> Response[
    DeploymentLogPayloadType0
    | DeploymentLogPayloadType1
    | DeploymentLogPayloadType2
    | DeploymentLogPayloadType3
    | DeploymentLogPayloadType4
    | DeploymentLogPayloadType5
    | DeploymentLogPayloadType6
    | DeploymentLogPayloadType7
    | DeploymentLogPayloadType8
    | DeploymentLogPayloadType9
]:
    """
    Args:
        hosted_function_id (str | Unset):
        server_slug (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeploymentLogPayloadType0 | DeploymentLogPayloadType1 | DeploymentLogPayloadType2 | DeploymentLogPayloadType3 | DeploymentLogPayloadType4 | DeploymentLogPayloadType5 | DeploymentLogPayloadType6 | DeploymentLogPayloadType7 | DeploymentLogPayloadType8 | DeploymentLogPayloadType9]
    """

    kwargs = _get_kwargs(
        hosted_function_id=hosted_function_id,
        server_slug=server_slug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    hosted_function_id: str | Unset = UNSET,
    server_slug: str | Unset = UNSET,
) -> (
    DeploymentLogPayloadType0
    | DeploymentLogPayloadType1
    | DeploymentLogPayloadType2
    | DeploymentLogPayloadType3
    | DeploymentLogPayloadType4
    | DeploymentLogPayloadType5
    | DeploymentLogPayloadType6
    | DeploymentLogPayloadType7
    | DeploymentLogPayloadType8
    | DeploymentLogPayloadType9
    | None
):
    """
    Args:
        hosted_function_id (str | Unset):
        server_slug (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeploymentLogPayloadType0 | DeploymentLogPayloadType1 | DeploymentLogPayloadType2 | DeploymentLogPayloadType3 | DeploymentLogPayloadType4 | DeploymentLogPayloadType5 | DeploymentLogPayloadType6 | DeploymentLogPayloadType7 | DeploymentLogPayloadType8 | DeploymentLogPayloadType9
    """

    return (
        await asyncio_detailed(
            client=client,
            hosted_function_id=hosted_function_id,
            server_slug=server_slug,
        )
    ).parsed
