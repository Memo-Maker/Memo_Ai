from flask import Flask, request, jsonify
from flask_cors import CORS  # Flask-CORS import

from Audio_STT_Summary import process_youtube_url  # Audio_STT2 모듈에서 함수 import
from GptQueryOpenai_API import questionToGPT
from toSpring import send_answer_to_spring_server
from toSpring import send_summary_to_spring_server


app = Flask(__name__)

# CORS 설정
CORS(app)

@app.route('/')
def index():
    return 'Hello World!'

# 영상요약
@app.route('/summaryurl', methods=['POST'])
def summarize_url():
    try:
        print("summarize_url 함수 실행", flush=True)
        data = request.get_json()
        url = data.get('url')
        userId = data.get('userId')
        print(f"userId={userId}님이 url:{url}의 영상 요약을 요청했습니다")
        
        if not url:
            return jsonify({' 🟡 error': '유튜브 URL을 제공해주세요.'}), 400
        
        print(f"url: {url}")  # 로그 출력
        
        # Audio_STT2 모듈에서 정의된 함수 호출
        cleaned_title, url, thumbnail_url, sum_result = process_youtube_url(url)
        
        print(f" 🟡  [요약 내용]\n  {sum_result}")  # 로그 출력
        send_summary_to_spring_server(userId, url, cleaned_title, thumbnail_url, sum_result)
        
        return jsonify({'summary': sum_result}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# GPT한테 질문
@app.route('/questionurl', methods=['POST'])
def question_url():
    try:
        print("question_url 함수 실행", flush=True)
        data = request.get_json()
        question = data.get('question')
        userId = data.get('userId')
        videoUrl = data.get('videoUrl')
    
        if not question:
            return jsonify({' 🟡 error': 'question을 제공해주세요.'}), 400
        
        print(f"받은 질문 : {question}")
        
        # gptQueryOpenai_API 모듈에서 정의된 함수 호출
        qAnswer = questionToGPT(question)
        print(f" 🟡  [ 답변 ]\n  {qAnswer}")  # 로그 출력
        send_answer_to_spring_server(userId, videoUrl, question, qAnswer)
        return jsonify({'qAnswer': qAnswer}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)