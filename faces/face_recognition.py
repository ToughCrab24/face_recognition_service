import face_recognition

from config.settings.base import BASE_DIR
from faces.exceptions import NoFaceFoundException
from faces.serializers import FaceSerializer


def find_face(unknown_face_path, known_faces):
    unknown_image = face_recognition.load_image_file(BASE_DIR + unknown_face_path)
    unknown_face_encodings = face_recognition.face_encodings(unknown_image)

    if len(unknown_face_encodings) < 1:
        raise NoFaceFoundException('No Face Found.')

    unknown_face_encoding = unknown_face_encodings[0]
    known_faces_encodings = []

    for known_face in known_faces:
        image = face_recognition.load_image_file(BASE_DIR + known_face.face_image.url)
        image_encoding = face_recognition.face_encodings(image)[0]
        known_faces_encodings.append(image_encoding)

    # use the database to search of the face
    results = face_recognition.compare_faces(known_faces_encodings, unknown_face_encoding)

    face_results = []
    for index, face_matches in enumerate(results):
        if face_matches:
            serializer = FaceSerializer(known_faces[index])
            face_results.append(serializer.data)

    return face_results
