# -*- coding: utf-8 -*-


#
# IMPORTS
#


from openai import AsyncOpenAI
from pydantic import SecretStr

from .config import MyBaseSecrets, MyBaseSettings

#
#
# CONFIGURATION
#


class OpenAISecrets(MyBaseSecrets):
    openai_api_key: SecretStr


class OpenAISettings(MyBaseSettings):
    openai_org: str


settings = OpenAISettings()

_secrets = OpenAISecrets()


#
# INITIALIZATION
#


client = AsyncOpenAI(
    organization=settings.openai_org,
    api_key=_secrets.openai_api_key.get_secret_value(),
)

del _secrets
