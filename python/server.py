from flask import Flask, request, jsonify
from flask_cors import CORS  # Flask-CORS import

from Audio_STT2 import process_youtube_url  # Audio_STT2 모듈에서 함수 import


app = Flask(__name__)

# CORS 설정
CORS(app)

@app.route('/summaryurl', methods=['POST'])
def summarize_url():
    try:
        print("summarize_url 함수 실행", flush=True)
        data = request.get_json()
        url = data.get('url')
        print(f"url: {url}")  # 로그 출력
        if not url:
            return jsonify({' 🟡 error': '유튜브 URL을 제공해주세요.'}), 400

        # Audio_STT2 모듈에서 정의된 함수 호출
        sum_result = process_youtube_url(url)
        print(f" 🟡  [요약 내용]\n  {sum_result}")  # 로그 출력

        return jsonify({'summary': sum_result}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)