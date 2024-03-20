import openai

# OpenAI Key 설정 및 인증
OPENAI_API_KEY = "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"
#"오픈AI에서 발급받은 API 키"

openai.api_key = OPENAI_API_KEY

# 유튜브 영상 다운로드
from pytube import YouTube
DOWNLOAD_FOLDER = "C:/Users/코딩하는 금융인/Desktop/whisper" # 경로 설정
url = "https://www.youtube.com/watch?v=" # 유튜브 영상 url
yout = YouTube(url)
stream = yout.streams.get_highest_resolution() # 유튜브 파일 다운로드
stream.download(DOWNLOAD_FOLDER)

# 유튜브 영상 mp3 파일 전환
from moviepy.editor import VideoFileClip
video_file_path = "C:/Users/코딩하는 금융인/Desktop/whisper/video.mp4"
video = VideoFileClip(video_file_path)
audio_file_path = "C:/Users/코딩하는 금융인/Desktop/whisper/audio.mp3"
video.audio.write_audiofile(audio_file_path)

# whisper 모델 사용하기
audio_file = open("C:/Users/코딩하는 금융인/Desktop/whisper/audio.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
text = transcript['text']
print(text) # whisper text 추출