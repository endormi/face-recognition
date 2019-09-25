"""
author: @endormi

Match the face
"""

import face_recognition

# Known image
img = face_recognition.load_image_file('./img/known/image')
img_encode = face_recognition.face_encodings(img)[0]

# Unknown image
unknown = face_recognition.load_image_file(
    './img/unknown/image')
unknown_encode = face_recognition.face_encodings(unknown)[0]

# Comparing faces
res = face_recognition.compare_faces(
    [img_encode], unknown_encode)

if res[0]:
    print('This is known image')
else:
    print('This is an unknown image')
    