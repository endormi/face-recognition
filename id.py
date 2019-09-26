"""
author: @endormi

Identify images and draw a label with a name below the face
"""

import face_recognition
from PIL import Image, ImageDraw

img = face_recognition.load_image_file('./img/known/image')
img_encode = face_recognition.face_encodings(img)[0]

image = face_recognition.load_image_file('./img/known/image')
image_encode = face_recognition.face_encodings(image)[0]


known_face_encodings = [
  img_encode,
  image_encode
]


known_face_names = [
  "Person",
  "Person 2"
]

# Load image to find faces
__image__ = face_recognition.load_image_file('./img/groups/image')

# Find faces
face_loc = face_recognition.face_locations(__image__)
face_encodings = face_recognition.face_encodings(__image__, face_loc)

# Convert to PIL format
pil = Image.fromarray(__image__)

# Draw image
draw = ImageDraw.Draw(pil)


# Loop through each face found in the unknown image
for (top, bottom, right, left), face_encoding in zip(face_loc, face_encodings):
  matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

  name = "Unknown Person"

  if True in matches:
    _match_ = matches.index(True)
    name = known_face_names[_match_]
  
  draw.rectangle(((left, top), (right, bottom)), outline=(0,0,0))

  # Draw a label with a name below the face
  text_width, text_height = draw.textsize(name)
  draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
  draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))

# Remove the drawing library from memory as per the Pillow docs
del draw

# Display image
pil.show()