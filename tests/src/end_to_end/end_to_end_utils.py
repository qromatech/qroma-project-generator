import datetime
import random
import os
import threading
import subprocess
import time
import requests
import psutil
from sys import platform


def is_platform_windows():
    return platform == "win32"


def is_platform_mac():
    return platform == "darwin"


# Windows...

def create_project_id():
    now = datetime.datetime.now()
    today_key = f"{now.year:04d}-{now.month:02d}-{now.day:02d}"
    today_time_key = f"{now.hour:02d}{now.minute:02d}{now.second:02d}"
    test_id = random.randint(1, 999)

    project_id = f"test-project-{today_key}.{today_time_key}.{test_id:03d}"
    return project_id


def get_test_user_qroma_dir():
    from pathlib import Path
    home_dir = Path.home()
    qroma_dir = os.path.join(home_dir, "qroma-projects")
    return qroma_dir


def get_pb_build_compiled_by_qroma_receipt_location(project_id):
    user_qroma_dir = get_test_user_qroma_dir()
    location = os.path.join(user_qroma_dir, project_id, "protobufs", "protofiles-out", "compiled-by-qroma.txt")
    return location


def get_firmware_build_output_bin_file_locations(project_id):
    user_qroma_dir = get_test_user_qroma_dir()
    esp32dev_location = os.path.join(user_qroma_dir, project_id, "firmware", f"esp32-{project_id}",
                                     ".pio", "build", "esp32dev", "firmware.bin")
    qtpy_location = os.path.join(user_qroma_dir, project_id, "firmware", f"esp32-{project_id}",
                                 ".pio", "build", "adafruit_qtpy_esp32c3", "firmware.bin")
    return [esp32dev_location, qtpy_location]


def get_site_build_output_node_modules_dir_location(project_id):
    user_qroma_dir = get_test_user_qroma_dir()
    expected_site_node_modules_location = os.path.join(user_qroma_dir, project_id,
                                                       "sites", f"site-www-{project_id}", "node_modules")
    return expected_site_node_modules_location


class WebServerTestHost:
    _project_id: str
    _thread: threading.Thread
    _keep_server_running: False
    _is_server_running: False
    server_root: str
    _server_port: int

    def init(self, project_id, server_port):
        self._project_id = project_id
        self._thread = threading.Thread(target=self.run_thread)
        self._keep_server_running = False
        self._is_server_running = False
        self._server_port = server_port
        self.server_root = f"http://localhost:{server_port}"

    def run_thread(self):
        self._is_server_running = False
        self._keep_server_running = True

        user_qroma_dir = get_test_user_qroma_dir()
        site_www_dir = os.path.join(user_qroma_dir, self._project_id, "sites", f"site-www-{self._project_id}")

        # start cmd / npm run serve
        npm_server = None

        # Windows
        if is_platform_windows():
            npm_server = subprocess.Popen(f"npm start -- --port {self._server_port}",
                                          shell=True,
                                          cwd=site_www_dir)

        # Mac
        if is_platform_mac():
            # https://stackoverflow.com/a/13143013
            cmd = f"npm start -- --port {self._server_port}"
            cmd = "exec " + cmd
            npm_server = subprocess.Popen(cmd,
                                          stdout=subprocess.PIPE,
                                          shell=True,
                                          cwd=site_www_dir)

        self._is_server_running = True

        # wait until told to stop
        while self._keep_server_running:
            time.sleep(1)

        print("TERMINATING npm_server PROCESS")

        # kill on Windows
        if is_platform_windows():
            subprocess.Popen(f"TASKKILL /F /PID {npm_server.pid} /T")

        # kill on Mac
        if is_platform_mac():
            for child in psutil.Process(npm_server.pid).children(recursive=True):
                child.kill()
            npm_server.kill()

        # wait until stopped
        self._is_server_running = False

    def wait_for_responsiveness(self, max_seconds):
        # wait until serving
        start_time = datetime.datetime.now()
        responsiveness_check_end_time = start_time + datetime.timedelta(0, max_seconds)
        is_responsive = False

        while datetime.datetime.now() < responsiveness_check_end_time and not is_responsive:
            try:
                response = requests.get(self.server_root, timeout=1.0)
                if response.ok:
                    is_responsive = True
            except Exception as e:
                time.sleep(0.5)
                print(e)

        if not is_responsive:
            raise Exception(f"Unable to get server response within {max_seconds} seconds")

    def start_server(self):
        self._thread.start()
        while not self._is_server_running:
            time.sleep(1)

    def stop_server(self):
        self._keep_server_running = False
        self._thread.join()
        self._is_server_running = False
