# -*- coding: utf-8 -*-


#
# IMPORTS
#


from openai import AsyncAzureOpenAI
from pydantic import HttpUrl, SecretStr

from .config import MyBaseSecrets, MyBaseSettings

#
#
# CONFIGURATION
#


class AOAISecrets(MyBaseSecrets):
    aoai_api_key: SecretStr
    aoai_endpoint: HttpUrl


class AOAISettings(MyBaseSettings):
    aoai_api_version: str


#
# INITIALIZATION
#


settings = AOAISettings()

_secrets = AOAISecrets()

client = AsyncAzureOpenAI(
    azure_endpoint=str(_secrets.aoai_endpoint),
    api_key=_secrets.aoai_api_key.get_secret_value(),
    api_version=settings.aoai_api_version,
)

del _secrets
