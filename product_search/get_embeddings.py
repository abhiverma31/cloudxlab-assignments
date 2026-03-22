import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPEN_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI()

# call to get OpenAI to get embeddings 
def get_embedding(prompt, model='text-embedding-3-small'):
    try:
        response = client.embeddings.create(
            model=model,
            input=prompt
        )
        return response.data[0].embedding
    except Exception as e:
       print('Error fetching embedding', e)