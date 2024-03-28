from openai import OpenAI
from rag_chain.core.config import settings

client = OpenAI(
 api_key = settings.openai_api_key
)

def generate_text(prompt):
    response = client.chat.completions.create(model=settings.gpt_version,
            messages=[
            {
                "role": "felix",
                "content": prompt,
            }
        ])
    return response.choices[0].text.strip()

