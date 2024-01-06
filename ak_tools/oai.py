# -*- coding: utf-8 -*-


#
# IMPORTS
#


from openai import AsyncOpenAI
from pydantic import SecretStr

from .config import MyBaseSecrets

#
#
# CONFIGURATION
#


class OpenAISecrets(MyBaseSecrets):
    openai_api_key: SecretStr
    openai_org: SecretStr


#
# INITIALIZATION
#


_secrets = OpenAISecrets()

client = AsyncOpenAI(
    organization=_secrets.openai_org.get_secret_value(),
    api_key=_secrets.openai_api_key.get_secret_value(),
)

del _secrets
