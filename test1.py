import openai

# 발급받은 API 키 설정
OPENAI_API_KEY = "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"

# openai API 키 인증
openai.api_key = OPENAI_API_KEY


# from pytube import YouTube
# DOWNLOAD_FOLDER = "./whisper"
# url = "https://www.youtube.com/watch?v="
# yt = YouTube(url)
# stream = yt.streams.get_highest_resolution()
# stream.download(DOWNLOAD_FOLDER)

audio_file = open("./audio.mp3", "rb")

transcript = openai.Audio.transcribe("whisper-1", audio_file)
text = transcript['text']
print(text)