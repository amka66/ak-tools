# -*- coding: utf-8 -*-


#
# IMPORTS
#


import os

from dotenv import load_dotenv
from openai import AsyncAzureOpenAI

#
#
# TYPE HINTS
#


Message = dict


#
# INITIALIZATION
#


load_dotenv()

AOAI_API_KEY = os.getenv("AOAI_API_KEY")
AOAI_ENDPOINT = os.getenv("AOAI_ENDPOINT")
AOAI_API_VERSION = os.getenv("AOAI_API_VERSION")

client = AsyncAzureOpenAI(
    azure_endpoint=AOAI_ENDPOINT,
    api_key=AOAI_API_KEY,
    api_version=AOAI_API_VERSION,
)
