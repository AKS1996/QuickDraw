import cv2
from keras.models import load_model
import numpy as np
import os
import sys

model = load_model('QuickDraw.h5')

def predict(cnt):
#    x, y, w, h = cv2.boundingRect(cnt)
#    cnt = cnt[y:y + h, x:x + w]
    keras_predict(model, cnt)

def keras_predict(model, image):
    processed = keras_process_image(image)
    print("processed: " + str(processed.shape))
    pred_probab = model.predict(processed)[0]
    print(pred_probab)
    pred_class = list(pred_probab).index(max(pred_probab))
    print(max(pred_probab), pred_class)


def keras_process_image(img):
    image_x = 28
    image_y = 28
    img = cv2.resize(img, (image_x, image_y))
    img = np.array(img, dtype=np.float32)
    img = np.reshape(img, (-1, image_x, image_y, 1))
    return img

if __name__ == '__main__':
    img = cv2.imread(sys.argv[1],0)
    img = cv2.bitwise_not(img)
    predict(img)
