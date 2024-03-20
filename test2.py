import os
import openai
from dotenv import load_dotenv
import json

# .env 파일에서 환경 변수 로드
load_dotenv()

# API 키 가져오기
API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = API_KEY

try:
    print("🟢 speechToTextAPI_O 시작")
    
    audio_file_path = './assets/audio/10초_짜리영상_크쿠루삥뽕.mp3'
    
    # 파일이 존재하지 않는 경우 FileNotFoundError 발생
    if not os.path.exists(audio_file_path):
        raise FileNotFoundError("오디오 파일이 존재하지 않습니다.")

    with open(audio_file_path, 'rb') as audio_file:
        # 오디오 -> 텍스트 변환
        transcript = openai.Audio.transcribe('whisper-1', audio_file)
        print(transcript['text'])
        
        # JSON 파일 열기
        json_file_path = './assets/audio_urls.json'
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 파일 경로에서 마지막 '/' 이후의 문자열을 추출하여 파일 이름만 저장
        cleaned_audio_name = audio_file_path[audio_file_path.rfind('/') + 1:]
        # 파일 이름에서 확장자 부분을 제거하여 저장
        cleaned_audio_name = cleaned_audio_name[:cleaned_audio_name.rfind('.')]

        # 오디오 파일과 같은 key를 찾아서 STT 값을 추가
        for key, value in data.items():
            if key == cleaned_audio_name:
                print("🟢 같은거 찾음")
                data[key]['stt'] = transcript['text']
                # data[key]['stt'] = "sttContent"
                print("🟢 STT 저장 완료")
                break
        
        # JSON 파일 업데이트
        with open(json_file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
    print("🔴 speechToTextAPI_O 종료")

except FileNotFoundError as e:
    print(f"🔴 FileNotFoundError")
    print(f"🔴 오류 발생: {e}")
except Exception as e:
    print(f"🔴 오류 발생\n🔴 {e}")
