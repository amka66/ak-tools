# -*- coding: utf-8 -*-


#
# IMPORTS
#


import json
from typing import Literal

from openai.types.chat import ChatCompletion, ChatCompletionMessage

from .config import MyBaseSettings

#
#
# TYPE HINTS
#


Message = dict


#
# CONFIGURATION
#


class GPTSettings(MyBaseSettings):
    gpt_client: Literal["openai", "aoai"]


settings = GPTSettings()


#
# INITIALIZATION
#


if settings.gpt_client == "openai":
    from .oai import client
elif settings.gpt_client == "aoai":
    from .aoai import client


#
# CHAT COMPLETION CALL
#


async def call_gpt(
    messages, *, model: str, tools: list[dict] = [], **kwargs
) -> tuple[Message, ChatCompletionMessage, ChatCompletion]:
    """Utility function for calling GPT"""
    assert model is not None

    if len(tools) > 0:
        response = await client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools,
            **kwargs,
        )
    else:
        response = await client.chat.completions.create(
            model=model,
            messages=messages,
            **kwargs,
        )
    message = response.choices[0].message
    assert message.role == "assistant"
    # assert message.name is None
    if len(tools) == 0:
        assert message.tool_calls is None
    return message.model_dump(), message, response


#
# HANDLING OF CHAT HISTORY
#


def add_to_history(history: list[Message], message: Message) -> None:
    """Utility function for adding a message to history in-place"""
    message = {**message}
    for field in ["function_call", "tool_calls"]:
        if field in message and message[field] is None:
            del message[field]
    history += [message]


def get_str_message(message: Message) -> str:
    """Get pretty string of message"""
    role = message["role"]
    content = message["content"] or ""
    tool_calls: list[dict] = []
    if "tool_calls" in message:
        for call in message["tool_calls"]:
            assert call["type"] == "function"
            tool_calls += [
                {
                    "id": call["id"],
                    "function_name": call["function"]["name"],
                    "arguments": json.loads(call["function"]["arguments"]),
                }
            ]
    tool_call_id = ""
    if "tool_call_id" in message:
        tool_call_id = message["tool_call_id"]
    if tool_call_id:
        content = json.loads(content)
    new_message = {
        "tool_call_id": tool_call_id,
        "content": content,
        "tool_calls": tool_calls,
    }
    if not content:
        del new_message["content"]
    if not tool_calls:
        del new_message["tool_calls"]
    if not tool_call_id:
        del new_message["tool_call_id"]
    str_new_message = f"{role.upper()} " + json.dumps(new_message, indent=4)
    return str_new_message
