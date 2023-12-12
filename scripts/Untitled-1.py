# %%
import asyncio

import nest_asyncio

nest_asyncio.apply()

from util.gpt import call_gpt

# %%
MODEL_BOT = "gpt4-1106"  # "gpt-3.5-turbo-1106"  # "gpt-4-1106-preview"

# %%
_, result = asyncio.run(
    call_gpt(
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": "Tell me something funny about is Lean 4 and mathlib.",
            },
        ],
        model=MODEL_BOT,
    )
)
result
# %%
type(result)
# %%
