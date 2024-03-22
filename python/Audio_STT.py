from pytube import YouTube
import re
import os
import json
import whisper
import time

print("🟢 extractAudio.py 시작")

# URL 입력
# url = 'https://youtu.be/nspco5QyZwo?si=yPG2ZxNat-ypSQgi'
url = input("URL 입력 : ")

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
    cleaned_title :{
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



audio_file_name = f"{cleaned_title}.mp3"
additional_path = r"assets\audio"  # 추가적인 경로

# 스크립트 파일이 있는 디렉토리의 절대 경로를 기반으로 오디오 파일의 경로를 설정합니다.
# script_directory는 현재 파이썬 프로젝트가 있는 위치를 말함
script_directory = os.path.dirname(os.path.abspath(__file__))
MEMO_AI_directory = os.path.dirname(script_directory)

# 경로를 조립해서 오디오파일 경로로 만듦
audio_file_path = os.path.join(MEMO_AI_directory, additional_path, audio_file_name)

print(f" -->> audio_file_path = {audio_file_path}")

try:
    print("🟢 speechToTextAPI_X 시작")
    start_time = time.time()  # 시작 시간 기록
    
    if not os.path.exists(audio_file_path):
        raise FileNotFoundError("오디오 파일을 찾을 수 없습니다.")

    # tiny, base, small, medium, large
    model = whisper.load_model('medium')
    result = model.transcribe(audio_file_path)
    print(result['text'])
    
    end_time = time.time()  # 종료 시간 기록
    elapsed_time = end_time - start_time  # 전체 실행 시간 계산
    print(f"🔵 프로그램 소요 시간: {elapsed_time:.2f} 초")  # 실행 시간 출력

except FileNotFoundError as e:
    print(f"오디오 파일을 찾을 수 없습니다.")
    print(f"오류 발생: {e}")

except Exception as e:
    print(f"오류 발생: {e}")
