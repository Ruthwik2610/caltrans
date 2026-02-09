import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def run_groq_llama31(prompt: str):
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You summarize incidents clearly and concisely.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
        max_tokens=300,
    )
    return completion.choices[0].message.content


if __name__ == "__main__":
    print(
        run_groq_llama31("Summarize: A truck overturned on NH44 causing major delays.")
    )
