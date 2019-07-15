# face-recognition

Using [Python Face Recognition](https://pypi.org/project/face_recognition/) library. It was built using dlib's **state-of-the-art face** recognition built with deep learning.

Install dlib: 

```sh
pip install dlib
```

Install face recognition:

```sh
pip install face_recognition
```

Clone this repository:

```sh
git clone https://github.com/endormi/face-recognition.git
```

Test to see if it's installed correctly:

```sh
face_recognition ./img/known ./img/unknown
```

### Quick examples:

If you want to see the face distance calculated for each match in order to adjust the tolerance setting, you can use `--show-distance true`

```sh
face_recognition --show-distance true ./img/known ./img/unknown
```

If you simply want to know the names of the people in each photograph but don't care about file names

```sh
face_recognition ./img/known ./img/unknown | cut -d ',' -f2
```

- groupfaces - Find the locations of the faces & how many people are in this image. 

- match - Match the face.

To try other stuff, check the [documentation](https://github.com/ageitgey/face_recognition)
