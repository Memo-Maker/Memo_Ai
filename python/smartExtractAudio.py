# 자막이 있다면 자막으로 stt과정 대체


# from pytube import YouTube
# # 라이브러리 가져오기

# yt = YouTube('https://www.youtube.com/watch?v=CAhU7a-ll_s')
# # 동영상 링크를 이용해 YouTube 객체 생성

# # yt_captions = yt.captions
# # print(f"yt_captions = {yt_captions}")
# # # YouTube 객체에서 caption 객체를 가져옴

# # print("다운가능한 영상 자막 정보 :")
# # for i, cap in enumerate(yt.captions.all()):
# #     print(i, " : ", cap)

# # print("언어를 선택하세요 (code 입력): ")
# # code = input()
# # my_caption = yt_captions.get_by_language_code(code)
# # print("선택된 caption : ", my_caption)
# # print("선택된 자막 보여주기 :")
# # print(my_caption.generate_srt_captions())

# # print("end")
# if yt.captions:
#     print("다운가능한 영상 자막 정보 :")
#     for i, cap in enumerate(yt.captions.all()):
#         print(i, " : ", cap)
# else:
#     print("이 동영상에는 자막이 없습니다.")

# # print(f"yt.captions.all() = {yt.captions.all()}")

# # # 언어로 자막 선택하기
# # ## 한글 자막 1순위로 선택하기. 만약 한글 자막이 없다면 자막 리스트 중 첫 번째 자막 선택하기
# # caption = yt.captions.get_by_language_code('ko')
# # if caption == None:
# #     caption = yt.captions.all()[0]