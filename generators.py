from openai import AsyncOpenAI
from config import API_KEY, BASE_URL

client = AsyncOpenAI(
    api_key=API_KEY,
    base_url=BASE_URL,
    timeout=60.0
)

async def create_response(text: str): 
    response = await client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content