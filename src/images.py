# scrape and store images in the images dir
import requests

class Images:
    GENERIC_CAM_URL = "https://recsports.ufl.edu/cam/camXXXFILLERXXX.jpg"
    NUMBER_OF_CAMS = 8

    @staticmethod
    # returns nothing but will save the images to folder for later
    def get_images():
        raw_strs = []
        for cam_num in range(1, 9): # 1, 2, 3, 4, ..., 8
            cam_url = Images.GENERIC_CAM_URL.replace("XXXFILLERXXX", str(cam_num))
            raw = requests.get(cam_url)
            raw_strs.append(raw.content)

        Images._write_images(raw_strs)

    @staticmethod
    def _write_images(raw_strs):
        for i, raw_str in enumerate(raw_strs):
            file_name = f"images/cam_{str(i+1)}.jpg"
            with open(file_name, 'wb') as fo:
                fo.write(raw_str)
