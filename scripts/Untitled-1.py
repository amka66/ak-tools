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

# %%
import ak_tools
from ak_tools.read import read_jsonlines_to_dataframe
from ak_tools.write import write_dataframe_to_jsonlines

read_jsonlines_to_dataframe
write_dataframe_to_jsonlines

print(ak_tools.__version__)
# %%
