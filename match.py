"""
@author: Endormi

Match the face
"""

import face_recognition

# Elon Musk image
elon = face_recognition.load_image_file('./img/known/elon_musk.jpg')
elon_encode = face_recognition.face_encodings(elon)[0]

# Unknown image
unknown = face_recognition.load_image_file(
    './img/unknown/cooper.jpg')
unknown_encode = face_recognition.face_encodings(unknown)[0]

# Comparing faces
results = face_recognition.compare_faces(
    [elon_encode], unknown_encode)

if results[0]:
    print('This is Elon Musk')
else:
    print('This is NOT Elon Musk')
    