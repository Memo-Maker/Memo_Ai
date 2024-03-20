from pytube import YouTube
from google.cloud import speech_v1
# from langchain import Translator
import openai

# Pytube를 사용하여 유튜브 영상에서 오디오를 추출하는 함수
def extract_audio(youtube_url):
    yt = YouTube(youtube_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(filename="audio")
    return "audio.mp4"

# Whisper를 사용하여 오디오를 텍스트로 변환하는 함수
def audio_to_text(audio_file):
    client = speech_v1.SpeechClient()
    with open(audio_file, "rb") as audio_file:
        content = audio_file.read()

    audio = {"content": content}
    config = {
        "language_code": "ko-KR",  # 유튜브 영상의 언어 코드 입력
        "audio_channel_count": 2,   # 오디오 채널 개수 입력
    }
    response = client.recognize(config=config, audio=audio)

    text = ""
    for result in response.results:
        text += result.alternatives[0].transcript
    return text



# ChatGPT를 사용하여 요약하는 함수
def summarize_text(text):
    openai.api_key = "YOUR_OPENAI_API_KEY"
    response = openai.Completion.create(
        engine="davinci",
        prompt=text,
        temperature=0.5,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"],
    )
    summary = response.choices[0].text.strip()
    return summary

# 메인 함수
def main(youtube_url):
    # Step 1: 오디오 추출
    audio_file = extract_audio(youtube_url)

    # Step 2: 오디오를 텍스트로 변환
    text = audio_to_text(audio_file)

    # # Step 3: Langchain 적용해서 내용 나누기
    # translated_text = translate_text(text)

    # # Step 4: ChatGPT에 요약 요청
    # summary = summarize_text(translated_text)
    # return summary
    return text

# 유튜브 영상 주소 입력
youtube_url = input("유튜브 영상 주소를 입력하세요: ")
result = main(youtube_url)
print("ChatGPT에 의한 요약:")
print(result)
