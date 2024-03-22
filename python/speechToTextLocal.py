import whisper
import os
import time

audio_file_name = "이게_불법이_아니었다고.mp3"
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
