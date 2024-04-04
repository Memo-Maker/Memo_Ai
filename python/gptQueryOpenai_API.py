import os
import openai
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

# API 키 가져오기
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def qa_gpt(content):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": content}]
    )

    # print(f"response :\n {response}")
    # print(f"답변 :\n {response.choices[0].message.content}")
    return response.choices[0].message.content


# query = input("gpt에게 할 말: ")

# qa_gpt(query)
