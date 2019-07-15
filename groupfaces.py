"""
@author: Endormi

Find the location of the faces & how many people are in this image
"""

import face_recognition

# Load image
image = face_recognition.load_image_file('./img/group/team.jpeg')
loc = face_recognition.loc(image)

print(loc)
print(f'There are {len(loc)} people in this image')
