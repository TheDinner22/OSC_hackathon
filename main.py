import requests

def get_images():
    raw = requests.get("https://recsports.ufl.edu/cam/cam4.jpg")
    return raw.content

def str_to_img(raw_str, new_file_name):
    with open(new_file_name, 'wb') as fo:
        fo.write(raw_str)

def main():
    raw_str = get_images()
    str_to_img(raw_str, "new_file.jpg")

if __name__ == "__main__":
    main()
