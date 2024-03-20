from pytube import YouTube
import re
import os
import json

# URL 입력
url = 'https://www.youtube.com/watch?v=tW4bs15UYG8'
# YouTube 객체 생성
yt = YouTube(url)

# 폴더 경로 설정
output_folder = os.path.join('./assets', 'audio')
os.makedirs(output_folder, exist_ok=True)  # 만약 폴더가 존재하지 않으면 생성

# 파일명으로 허용되지 않는 문자 제거 및 공백 대체
cleaned_title = re.sub(r'[^\w\s-]', '', yt.title).strip().replace(' ', '_')

# 썸네일 이미지 가져오기
thumbnail_url = yt.thumbnail_url

# 오디오 다운로드
audio_file_path = os.path.join(output_folder, cleaned_title + '.mp3')
yt.streams.filter(only_audio=True).first().download(
    output_path=output_folder, filename=cleaned_title + '.mp3'
)

# JSON data (video title, URL, and thumbnail URL)
data = {
  yt.title:{
    'title': yt.title,
    "url": url,
    "thumbnail_url": thumbnail_url
  }
}

json_file_path = os.path.join('assets', 'audio_urls.json')

# JSON 파일이 이미 존재하는 경우 데이터 추가
if os.path.exists(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as f:  # UTF-8 인코딩으로 파일 열기
        existing_data = json.load(f)
    existing_data.update(data)
    data = existing_data

with open(json_file_path, 'w', encoding='utf-8') as f:  # UTF-8 인코딩으로 파일 쓰기
    json.dump(data, f, indent=4, ensure_ascii=False)

print("🔴 extractAudio.py 종료")
