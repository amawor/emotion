import cv2
from deepface import DeepFace
import numpy as np
import json


imglist = [
    "test.jpg",
    "namiyo0303_1.jpg",
    "cover-1-1332-750x422.jpg",
    "523.jpg",
    "362137929_1098259657816241_9041815736222973208_n.jpg",
]
for number in range(1, 56):
    img = str(number) + ".jpg"
    loaded = cv2.imread(img)
    print(img)
    try:
        obj = json.dumps(DeepFace.analyze(img, actions=["emotion"]))
        """
        emotion = DeepFace.analyze(img, actions=["emotion"])
        age = DeepFace.analyze(img, actions=["age"])
        race = DeepFace.analyze(img, actions=["race"])
        """
        obj = json.loads(obj)
        print(obj["dominant_emotion"])
        # print(age)
        # print(race)
    except:
        # print("face not found")
        pass
