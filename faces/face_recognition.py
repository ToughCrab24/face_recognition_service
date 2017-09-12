class FaceRecognition(object):
    def find_face(self, face):
        import face_recognition
        image = face_recognition.load_image_file("your_file.jpg")
        face_locations = face_recognition.face_locations(image)
        # use the database to search of the face

        # if there is a match then return something

        pass
