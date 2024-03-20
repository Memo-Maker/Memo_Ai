# import openai
# import os

# # First, set your OpenAI API key as an environment variable
# # os.environ["OPENAI_API_KEY"] = "Enter your API key here"

# # Create the OpenAI API client
# # openai.api_key = os.environ["OPENAI_API_KEY"]
# openai.api_key = "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"

# # Set the model you want to use
# model_engine = "gpt-3.5-turbo"
# file = open("audio.mp3", "rb")

# transcription = openai.Audio.transcribe("whisper-1", file)

# print(transcription['text'])


import os
import openai

API_KEY = "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"
openai.api_key = API_KEY

try:
    audio_file_path = './assets/audio/축구_간다며_뒤질래.mp3'
    # 파일이 존재하지 않는 경우 FileNotFoundError 발생
    if not os.path.exists(audio_file_path):
        raise FileNotFoundError("오디오 파일이 존재하지 않습니다.")

    with open(audio_file_path, 'rb') as audio_file:
        # 오디오 변환
        transcript = openai.Audio.transcribe('whisper-1', audio_file)
        print(transcript['text'])

except FileNotFoundError as e:
    print(f"🔴 FileNotFoundError")
    print(f"🔴 오류 발생: {e}")
except Exception as e:
    print(f"🔴 오류 발생\n🔴 {e}")
