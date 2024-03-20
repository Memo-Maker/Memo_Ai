import os
import openai
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

# API 키 가져오기
API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = API_KEY

try:
    print("🟢 speechToTextAPI_O 시작")
    
    audio_file_path = './assets/audio/아니_이걸_파네.mp3'
    
    # 파일이 존재하지 않는 경우 FileNotFoundError 발생
    if not os.path.exists(audio_file_path):
        raise FileNotFoundError("오디오 파일이 존재하지 않습니다.")

    with open(audio_file_path, 'rb') as audio_file:
        # 오디오 -> 텍스트 변환
        transcript = openai.Audio.transcribe('whisper-1', audio_file)
        print(transcript['text'])
    
    print("🔴 speechToTextAPI_O 종료")

except FileNotFoundError as e:
    print(f"🔴 FileNotFoundError")
    print(f"🔴 오류 발생: {e}")
except Exception as e:
    print(f"🔴 오류 발생\n🔴 {e}")
