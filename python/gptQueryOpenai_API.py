import os
import openai
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

# API 키 가져오기
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def questionToGPT(content):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": content}]
    )

    # print(f"response :\n {response}")
    print(f" 🟡 답변 :\n {response.choices[0].message.content}")
    return response.choices[0].message.content

if __name__ == "__main__":
    url = input("질문 입력 : ")
    questionToGPT(url)
