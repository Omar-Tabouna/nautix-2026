import socket

def is_rtsp_open(ip, port=554):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.3)

    result = sock.connect_ex((ip, port))
    sock.close()

    return result == 0


def scan_cameras(base_ip="192.168.10.", start=1, end=50):
    cameras = []

    for i in range(start, end):
        ip = f"{base_ip}{i}"

        if is_rtsp_open(ip):
            print(f"✅ Found camera at {ip}")
            cameras.append(f"rtsp://{ip}:554/stream1")

    return cameras

# cams = scan_cameras("192.168.100.", 1, 20)
# print(cams)

# self.cameras = scan_cameras("192.168.10.", 1, 20)

# self.ui.comboBox_4.clear()

# for i in range(len(self.cameras)):
#     self.ui.comboBox_4.addItem(f"Cam {i+1}")

# def choose_cam(self):
#     return self.cameras[self.ui.comboBox_4.currentIndex()]

# self.thread = VideoThread(self.choose_cam())
# self.thread.start()

# def change_camera(self):
#     self.thread.change_camera(self.choose_cam())

# cv2.VideoCapture(self.path, cv2.CAP_FFMPEG)


# from concurrent.futures import ThreadPoolExecutor
# def scan_cameras_fast(base_ip="192.168.10.", start=1, end=50):
#     cameras = []

#     def check(ip):
#         if is_rtsp_open(ip):
#             print(f"✅ {ip}")
#             return f"rtsp://{ip}:554/stream1"
#         return None

#     ips = [f"{base_ip}{i}" for i in range(start, end)]

#     with ThreadPoolExecutor(max_workers=20) as executor:
#         results = executor.map(check, ips)

#     cameras = [r for r in results if r is not None]
#     return cameras