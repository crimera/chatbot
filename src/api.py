import openai
from models import Prompt
from config import OPENAI_KEY

async def generate_response(prompt: Prompt) -> str:
    try:
        openai.api_key = OPENAI_KEY
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt.render().strip(),
            temperature=1.0,
            top_p=0.9,
            max_tokens=512,
        )

        return response.choices[0].text
    except Exception as e:
        return e