import whisper
import os
import time
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.document import Document


# text_splitter 설정
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=50,
    length_function=len,
)

try:
    print("🟢 test 시작")
    start_time = time.time()  # 시작 시간 기록
    
    result = "model.transcribe(audio_file_path)"
    print(result['text'])
    print(str(len(result['text'])) + "자")


    docs = [Document(page_content=x) for x in text_splitter.split_text(result["text"])]

    split_docs = text_splitter.split_documents(docs)

    print(f"split_docs : {len(split_docs)} 개")
    
    end_time = time.time()  # 종료 시간 기록
    elapsed_time = end_time - start_time  # 전체 실행 시간 계산
    print(f"🔵 프로그램 소요 시간: {elapsed_time:.2f} 초")  # 실행 시간 출력

except FileNotFoundError as e:
    print(f"오디오 파일을 찾을 수 없습니다.")
    print(f"오류 발생: {e}")

except Exception as e:
    print(f"오류 발생: {e}")
