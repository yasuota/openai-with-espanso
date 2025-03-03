import sys
from openai import OpenAI
import os

client = OpenAI(default_headers={
    "api_Key": os.getenv("OPENAI_API_KEY")}
)


def run(var):
    response = client.chat.completions.create(
        messages=[
            {"role": "system",
                "content": "You are a teacher who translates English into Spanish."},
            {"role": "user", "content": var},
        ],
        model="gpt-4o-mini",
    )
    print(response.choices[0].message.content)
    return


if __name__ == "__main__":
    run(str(sys.argv[1:]))
