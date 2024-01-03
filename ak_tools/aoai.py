# -*- coding: utf-8 -*-


#
# IMPORTS
#


from openai import AsyncAzureOpenAI
from pydantic import HttpUrl, SecretStr

from .settings import MyBaseSecrets, MyBaseSettings

#
#
# TYPE HINTS
#


Message = dict


#
# TYPES
#


class AOAISecrets(MyBaseSecrets):
    aoai_api_key: SecretStr


class AOAISettings(MyBaseSettings):
    aoai_endpoint: HttpUrl
    aoai_api_version: str


#
# INITIALIZATION
#


settings = AOAISettings()
_secrets = AOAISecrets()

client = AsyncAzureOpenAI(
    azure_endpoint=str(settings.aoai_endpoint),
    api_key=_secrets.aoai_api_key.get_secret_value(),
    api_version=settings.aoai_api_version,
)

del _secrets
