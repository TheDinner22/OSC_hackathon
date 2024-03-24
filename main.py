from src.images import Images, test
from src.count_faces import count_faces, count_objects


def main():
    raw_images = Images.get_images()
    for raw_image in raw_images:
        print(count_objects(raw_image))

if __name__ == "__main__":
    main()
