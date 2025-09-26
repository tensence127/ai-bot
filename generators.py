from openai import AsyncOpenAI
from config import API_KEY, BASE_URL

client = AsyncOpenAI(
    api_key=API_KEY,
    base_url=BASE_URL,
    timeout=60.0
)

async def create_response(messages):
    try:
        response = await client.chat.completions.create(
            model="google/gemma-3-12b",
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI API Error: {e}")
        raise