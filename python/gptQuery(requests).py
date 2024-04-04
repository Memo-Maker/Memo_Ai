import os
import requests
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

# API 키 가져오기
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def qa_gpt(content):
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"},
        json={"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": content}]},
    )

    print(f"[ response ]\n {response.json()}\n")
    print(response.json()["choices"][0]["message"]["content"])

query = input("gpt에게 할 말: ")

qa_gpt(query)
