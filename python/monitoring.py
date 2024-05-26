import os
import time

# 실행 중인 프로세스를 확인하는 함수
def check_process(process_name):
    cmd = "ps ax | grep " + process_name + " | grep -v grep"
    result = os.popen(cmd).read()
    return result != ""

# 실행할 스크립트 파일명 리스트
script_files = ["server.py"]

# 감시 주기 (초)
watch_interval = 60  # 예시로 1분마다 확인

while True:
    # 각 스크립트 파일에 대해 실행 여부 확인 후 실행
    for script_file in script_files:
        if not check_process(script_file):
            print(f"{script_file}가 실행 중이지 않습니다. 다시 실행합니다.")
            os.system(f"nohup python3 {script_file} &")
        else:
            print(f"{script_file}가 실행 중입니다.")
    
    # 일정 간격으로 감시
    time.sleep(watch_interval)
