# scrape and store images in the images dir
import requests
import base64

class Images:
    GENERIC_CAM_URL = "https://recsports.ufl.edu/cam/camXXXFILLERXXX.jpg"
    NUMBER_OF_CAMS = 8

    @staticmethod
    def get_images():
        b64_images = []
        for cam_num in range(1, 9): # 1, 2, 3, 4, ..., 8
            cam_url = Images.GENERIC_CAM_URL.replace("XXXFILLERXXX", str(cam_num))
            raw = requests.get(cam_url)
            b64_images.append(Images._b64_enc_img(raw.content))

        return b64_images

    @staticmethod
    def _b64_enc_img(raw_str):
        return base64.b64encode(raw_str)

