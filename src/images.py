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

