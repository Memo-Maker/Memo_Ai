import whisper
import os
import time
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from langchain.chains.mapreduce import MapReduceChain
from langchain.chains import ReduceDocumentsChain, MapReduceDocumentsChain
from langchain.chat_models import ChatOpenAI
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

# API 키 가져오기
API_KEY = os.getenv("OPENAI_API_KEY")

# #### Audio
# 오디오파일 이름
audio_file_name = "전세사기_피해자가_대응_플랫폼_만들었다_전세위키_등장_전세사기대책위원회와_함께_만들었습니다.mp3"

#   경로
# 스크립트 파일이 있는 디렉토리의 절대 경로를 기반으로 오디오 파일의 경로를 설정합니다.
# script_directory는 현재 파이썬 프로젝트가 있는 위치를 말함
additional_path = r"assets\audio"  # 추가적인 경로
script_directory = os.path.dirname(os.path.abspath(__file__))
MEMO_AI_directory = os.path.dirname(script_directory)

# 경로를 조립해서 오디오파일 경로로 만듦
audio_file_path = os.path.join(MEMO_AI_directory, additional_path, audio_file_name)
print(f" -->> audio_file_path = {audio_file_path}")



# #### Langchain 모델 및 map-reduce 체인 설정
llm = ChatOpenAI(temperature=0, openai_api_key=API_KEY)

# text_splitter 설정
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=50,
    length_function=len,
)

# Map prompt
map_template = """The following is a set of documents
{docs}
Based on this list of docs, please identify the main themes
Helpful Answer:"""

map_prompt = PromptTemplate.from_template(map_template)

# Reduce prompt
reduce_template = """The following is set of summaries:
{doc_summaries}
Take these and distill it into a final, consolidated summary of the main themes.
The final answer is a single paragraph of about 100 words and must be in Korean.
Helpful Answer:"""

reduce_prompt = PromptTemplate.from_template(reduce_template)

# 1. Reduce chain
# 조각을 합쳐서 요약
reduce_chain = LLMChain(llm=llm, prompt=reduce_prompt)

# Takes a list of documents, combines them into a single string, and passes this to an LLMChain
# 내용의 리스트(조각)를 가져와 하나의 문자열로 결합하고 이를 LLMChain으로 전달합니다.
combine_documents_chain = StuffDocumentsChain(
    llm_chain=reduce_chain, document_variable_name="doc_summaries"
)

# Combines and iteravely reduces the mapped documents
# 매핑된 문서를 결합하고 반복적으로 축소합니다.
reduce_documents_chain = ReduceDocumentsChain(
    # This is final chain that is called.
    # 호출되는 최종 체인입니다.
    combine_documents_chain=combine_documents_chain,
    # If documents exceed context for `StuffDocumentsChain`
    # `StuffDocumentsChain`의 컨텍스트를 초과할 경우
    collapse_documents_chain=combine_documents_chain,
    # The maximum number of tokens to group documents into.
    # 문서를 그룹화하는 데 사용되는 최대 토큰 수입니다.
    token_max=4000,
)

# 2. Map chain
map_chain = LLMChain(llm=llm, prompt=map_prompt)

# Combining documents by mapping a chain over them, then combining results
# 문서에 체인을 매핑하고 결과를 결합하여 문서를 만듭니다.
map_reduce_chain = MapReduceDocumentsChain(
    # Map chain
    llm_chain=map_chain,
    # Reduce chain
    reduce_documents_chain=reduce_documents_chain,
    # The variable name in the llm_chain to put the documents in
    # llm 체인 내의 문서를 넣을 변수 이름
    document_variable_name="docs",
    # Return the results of the map steps in the output
    # 중간 단계의 결과를 출력으로 반환할지 여부
    return_intermediate_steps=False,
)

try:
    print("🟢 speechToTextAPI_X 시작")
    start_time = time.time()  # 시작 시간 기록
    
    if not os.path.exists(audio_file_path):
        raise FileNotFoundError("오디오 파일을 찾을 수 없습니다.")
    
    # tiny, base, small, medium, large
    model = whisper.load_model('base')
    result = model.transcribe(audio_file_path)
    print(result['text'])
    print(str(len(result['text'])) + "자")

    # text_split
    docs = [Document(page_content=x) for x in text_splitter.split_text(result["text"])]
    split_docs = text_splitter.split_documents(docs)
    print(f"split_docs : {len(split_docs)} 개")

    # 내용 요약 시작
    sum_result = map_reduce_chain.run(split_docs)

    print(sum_result)
    
    end_time = time.time()  # 종료 시간 기록
    elapsed_time = end_time - start_time  # 전체 실행 시간 계산
    print(f"🔵 프로그램 소요 시간: {elapsed_time:.2f} 초")  # 실행 시간 출력
    

except FileNotFoundError as e:
    print(f"오디오 파일을 찾을 수 없습니다.")
    print(f"오류 발생: {e}")

except Exception as e:
    print(f"오류 발생: {e}")
