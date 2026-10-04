from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-5.6-luna",
    input="Say hello in Thai in one short sentence."
)

print(response.output_text)