# scrape and store images in the images dir
import requests
import time

class Images:
    GENERIC_CAM_URL = f"https://recsports.ufl.edu/cam/camXXXFILLERXXX.jpg?t={int(time.time())}"
    NUMBER_OF_CAMS = 8

    @staticmethod
    def get_images():
        raw_images = []
        for cam_num in range(1, 9): # 1, 2, 3, 4, ..., 8
            cam_url = Images.GENERIC_CAM_URL.replace("XXXFILLERXXX", str(cam_num))
            raw = requests.get(cam_url)
            raw_images.append(raw.content)

        return raw_images

def test():
    frames =[]
    while len(frames) < 20:
        url = f"https://recsports.ufl.edu/cam/cam1.jpg?t={int(time.time())}"
        raw = requests.get(url)

        if raw.content in frames:
            continue
            

        frames.append(raw.content)
        print("added one")
    for i, frame in enumerate(frames):
        with open(f"images/frame_{i+1}.jpg", 'wb') as fo:
            fo.write(frame)

