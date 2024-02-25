"""requests-based implementation of web client class."""

from asyncio import TimeoutError
from http import HTTPStatus
from typing import Optional

import aiohttp
from fake_useragent import UserAgent

from .abstract_client import (
    RETRYABLE_HTTP_STATUS_CODES,
    AbstractWebClientResponse,
    AbstractWebClientSuccessResponse,
    AsyncAbstractWebClient,
    WebClientErrorResponse,
)


class AioHttpWebClientSuccessResponse(AbstractWebClientSuccessResponse):
    """
    requests-based successful response.
    """

    __slots__ = [
        "__response",
    ]

    def __init__(
        self,
        response: aiohttp.ClientResponse,
        max_response_data_length: Optional[int] = None,
    ):
        self.__response = response

    def status_code(self) -> int:
        return int(self.__response.status)

    def status_message(self) -> str:
        message = self.__response.reason
        if not message:
            message = HTTPStatus(self.status_code(), None).phrase
        return message

    def header(self, case_insensitive_name: str) -> Optional[str]:
        return self.__response.headers.get(case_insensitive_name.lower(), None)

    async def raw_data(self) -> bytes:
        # Slicing the response was producing invalid data, so we're reading the entire response
        return await self.__response.content.read()


class AioHttpWebClientErrorResponse(WebClientErrorResponse):
    """
    requests-based error response.
    """

    pass


class AioHttpWebClient(AsyncAbstractWebClient):
    """requests-based web client to be used by the sitemap fetcher."""

    __slots__ = [
        "__max_response_data_length",
        "_client",
        "_ua",
    ]

    def __init__(self, client: aiohttp.ClientSession):
        self.__max_response_data_length = None
        self._client = client

        self._ua = UserAgent()

    def user_agent(self) -> str:
        return self._ua.random

    def set_max_response_data_length(self, max_response_data_length: int) -> None:
        self.__max_response_data_length = max_response_data_length

    async def get(self, url: str) -> AbstractWebClientResponse:
        try:
            response = await self._client.get(
                url,
                auto_decompress=True,
                headers={"User-Agent": self.user_agent()},
            )
        except (aiohttp.ServerTimeoutError, TimeoutError) as ex:
            # Retryable timeouts
            return AioHttpWebClientErrorResponse(message=str(ex), retryable=True)

        except aiohttp.ClientError as ex:
            # Other errors, e.g. redirect loops
            return AioHttpWebClientErrorResponse(message=str(ex), retryable=False)

        else:
            if 200 <= response.status < 300:
                return AioHttpWebClientSuccessResponse(
                    response=response,
                    max_response_data_length=self.__max_response_data_length,
                )
            else:
                message = "{} {}".format(response.status, response.reason)

                if response.status in RETRYABLE_HTTP_STATUS_CODES:
                    return AioHttpWebClientErrorResponse(
                        message=message, retryable=True
                    )
                else:
                    return AioHttpWebClientErrorResponse(
                        message=message, retryable=False
                    )
