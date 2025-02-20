import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

while True:
    # Set up the model and prompt
    model_engine = "gpt-4o"
    prompt = input("Enter new prompt: ")
    if prompt.lower() in ["exit", "quit"]:
        break

    try:
        completion = openai.chat.completions.create(
            model=model_engine,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1024,
            temperature=0.9,
            n=1,
        )

        response = completion.choices[0].message.content
        print(response)

    except Exception as e:
        print(f"Error: {e}")
