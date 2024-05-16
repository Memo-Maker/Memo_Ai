import requests
from datetime import datetime  # datetime 모듈을 import 합니다.

SPRING_BASE_URL = "http://localhost:8080";

# 질문
def send_answer_to_spring_server(userId, videoUrl, question, qAnswer):
    try:
        # 스프링 서버의 URL 설정
        spring_server_url = f"{SPRING_BASE_URL}/api/v1/questions/fetch-from-flask"

        # POST 요청에 보낼 데이터 설정
        data = {
            'memberEmail': userId,
            'videoUrl': videoUrl,
            'question': question,
            'answer': qAnswer
        }

        # POST 요청 보내기
        response = requests.post(spring_server_url, json=data)

        # 응답 상태코드 확인
        if response.status_code == 200:
            print("답변을 스프링 서버에 성공적으로 전송했습니다.")
        else:
            print(
                f"스프링 서버에 답변을 전송하는 중 오류가 발생했습니다. 응답 상태코드: {response.status_code}")

    except Exception as e:
        print(f"스프링 서버에 답변을 전송하는 중 오류가 발생했습니다: {str(e)}")

# 요약
def send_summary_to_spring_server(userId, url, cleaned_title, thumbnail_url, sum_result):
    try:
        # 스프링 서버의 URL 설정
        spring_server_url = f"{SPRING_BASE_URL}/api/v1/video/save"
        
        # 현재 날짜를 "YYYY-MM-DD" 형식으로 설정
        document_date = datetime.now().strftime("%Y-%m-%d")

        # POST 요청에 보낼 데이터 설정
        data = {
            'memberEmail': userId,
            "categoryName": "최근에 본 영상",
            'videoUrl': url,
            'videoTitle': cleaned_title,
            'thumbnailUrl': thumbnail_url,
            'summary': sum_result,
            'documentDate': document_date  # documentDate 추가
        }

        # POST 요청 보내기
        response = requests.post(spring_server_url, json=data)

        # 응답 상태코드 확인
        if response.status_code == 200:
            print("답변을 스프링 서버에 성공적으로 전송했습니다.")
        else:
            print(
                f"스프링 서버에 답변을 전송하는 중 오류가 발생했습니다. 응답 상태코드: {response.status_code}")

    except Exception as e:
        print(f"스프링 서버에 답변을 전송하는 중 오류가 발생했습니다: {str(e)}")
