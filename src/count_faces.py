# count the number of faces in an image

# yoinked from here https://cloud.google.com/vision/docs/detecting-faces#vision_face_detection-python

def count_faces(raw_str):
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()

    image = vision.Image(content=raw_str)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    if response.error.message:
        raise Exception( "{}\nFor more info on error messages, check: " "https://cloud.google.com/apis/design/errors".format(response.error.message))

    return len(faces)

def count_objects(raw_str):
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()

    image = vision.Image(content=raw_str)

    objects = client.object_localization(image=image).localized_object_annotations

    return len(objects)

