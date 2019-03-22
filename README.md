# Face Recognition 

[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.1-brightgreen.svg)](https://djangoproject.com)

Face Recognition is website build in django python framework which provides services like face detect, face features and comparing faces online.

![Face Recognition Home Page](/screenshots/home.png)


## Features

* Detect human faces from picture if present
![Face Recognition Home Page](/screenshots/detect.png)


* Detect faces features from picture if human face is present
![Face Recognition Home Page](/screenshots/features.png)

* Compare any faces pictures to check whether they belong to same person or not
![Face Recognition Home Page](/screenshots/compare.png)


## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone git@github.com:umaimagit/FaceRecognition.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Install dlib library:

Copy dlib wheel file from "whl_file/dlib-19.8.1-cp36-cp36m-win_amd64.whl" and run below command

```bash
pip install dlib-19.8.1-cp36-cp36m-win_amd64.whl
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.


## License

The source code is released under the MIT License.
