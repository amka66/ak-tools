# -*- coding: utf-8 -*-


#
# IMPORTS
#


import os

from dotenv import load_dotenv
from openai import AsyncOpenAI

#
#
# INITIALIZATION
#


load_dotenv()

_OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
_OPENAI_ORGANIZATION = os.getenv("OPENAI_ORGANIZATION")

client = AsyncOpenAI(
    organization=_OPENAI_ORGANIZATION,
    api_key=_OPENAI_API_KEY,
)
