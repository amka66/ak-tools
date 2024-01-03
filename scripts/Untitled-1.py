# %%
import asyncio

import nest_asyncio

nest_asyncio.apply()
from ak_tools.gpt import call_gpt
from ak_tools.main import MainSettings

# %%
settings = MainSettings()

# %%
_, message, response = asyncio.run(
    call_gpt(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": settings.main_content,
            },
        ],
        model=settings.main_model,
    )
)
print(message.content)
print(response.model)

# %%
