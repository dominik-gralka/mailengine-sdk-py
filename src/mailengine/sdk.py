"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .pet import Pet
from .sdkconfiguration import SDKConfiguration, ServerEnvironment
from .store import Store
from .user import User
from .utils.retries import RetryConfig
from mailengine import utils
from mailengine._hooks import SDKHooks
from mailengine.models import components
from typing import Callable, Dict, Optional, Union

class MailEngine:
    r"""Petstore - OpenAPI 3.1: This is a sample Pet Store Server based on the OpenAPI 3.1 specification.

    Some useful links:
    - [OpenAPI Reference](https://www.speakeasyapi.dev/openapi)
    - [The Pet Store repository](https://github.com/swagger-api/swagger-petstore)
    - [The source API definition for the Pet Store](https://github.com/swagger-api/swagger-petstore/blob/master/src/main/resources/openapi.yaml)
    http://swagger.io - Find out more about Swagger
    """
    pet: Pet
    r"""Everything about your Pets
    http://swagger.io - Find out more
    """
    store: Store
    r"""Access to Petstore orders
    http://swagger.io - Find out more about our store
    """
    user: User
    r"""Operations about user"""

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 api_key: Union[str, Callable[[], str]],
                 environment: ServerEnvironment = None,
                 server_idx: Optional[int] = None,
                 server_url: Optional[str] = None,
                 url_params: Optional[Dict[str, str]] = None,
                 client: Optional[requests_http.Session] = None,
                 retry_config: Optional[RetryConfig] = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.

        :param api_key: The api_key required for authentication
        :type api_key: Union[str, Callable[[], str]]
        :param environment: Allows setting the environment variable for url substitution
        :type environment: ServerEnvironment
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: RetryConfig
        """
        if client is None:
            client = requests_http.Session()

        if callable(api_key):
            def security():
                return components.Security(api_key = api_key())
        else:
            security = components.Security(api_key = api_key)

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)
        server_defaults = [
            {
                'environment': environment or 'prod',
            },
        ]
    

        self.sdk_configuration = SDKConfiguration(
            client,
            security,
            server_url,
            server_idx,
            server_defaults,
            retry_config=retry_config
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(current_server_url, self.sdk_configuration.client)
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__['_hooks'] = hooks

        self._init_sdks()


    def _init_sdks(self):
        self.pet = Pet(self.sdk_configuration)
        self.store = Store(self.sdk_configuration)
        self.user = User(self.sdk_configuration)
