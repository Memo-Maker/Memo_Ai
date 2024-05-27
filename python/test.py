import requests
from datetime import datetime

SPRING_BASE_URL = "http://52.78.68.15:8080"

def send_summary_to_spring_server(userId, url, cleaned_title, thumbnail_url, sum_result):
    try:
        spring_server_url = f"{SPRING_BASE_URL}/api/v1/video/save"
        document_date = datetime.now().strftime("%Y-%m-%d")
        cleaned_title = cleaned_title.replace("_", " ")
        
        if cleaned_title.startswith('"') and cleaned_title.endswith('"'):
            cleaned_title = cleaned_title[1:-1]
        
        if sum_result.startswith('"') and sum_result.endswith('"'):
            sum_result = sum_result[1:-1]
            
        data = {
            'memberEmail': userId,
            "categoryName": "최근에 본 영상",
            'videoUrl': url,
            'videoTitle': cleaned_title,
            'thumbnailUrl': thumbnail_url,
            'summary': sum_result,
            'documentDate': document_date
        }

        response = requests.post(spring_server_url, json=data)

        if response.status_code == 200:
            print("답변을 스프링 서버에 성공적으로 전송했습니다.")
        else:
            print(f"스프링 서버에 답변을 전송하는 중 오류가 발생했습니다. 응답 상태코드: {response.status_code}")
            print(f"응답 내용: {response.text}")

    except Exception as e:
        print(f"스프링 서버에 답변을 전송하는 중 오류가 발생했습니다: {str(e)}")

if __name__ == "__main__":
    userId = "1"
    url = "https://example.com/video"
    cleaned_title = "Example Video Title"
    thumbnail_url = "https://example.com/thumbnail.jpg"
    sum_result = "This is a summary of the video."

    send_summary_to_spring_server(userId, url, cleaned_title, thumbnail_url, sum_result)
