import whisper
import os

print("🟢 speechToTextAPI_X 시작")

audio_file_path = './assets/audio/이게_불법이_아니었다고.mp3'

try:
    # 파일이 존재하지 않는 경우 FileNotFoundError 발생
    if not os.path.exists(audio_file_path):
        raise FileNotFoundError("오디오 파일이 존재하지 않습니다.")

    # "audio.mp3" 오디오 파일을 로드합니다.
    audio_data, _ = whisper.load_audio(audio_file_path)

    # "base" 크기의 Whisper 모델을 메모리에 로드합니다.
    model = whisper.load_model("base")

    # 오디오 -> 텍스트 변환
    transcript = model.transcribe(audio_data)
    print(transcript['text'])

    print("🔴 speechToTextAPI_X 종료")

except FileNotFoundError as e:
    print(f"🔴 FileNotFoundError")
    print(f"🔴 오류 발생: {e}")
except Exception as e:
    print(f"🔴 오류 발생\n🔴 {e}")
