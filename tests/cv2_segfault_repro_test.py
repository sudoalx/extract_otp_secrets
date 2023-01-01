# pytest for extract_otp_secrets.py

# Run tests:
# pytest

import cv2  # type: ignore

def test_cv2_segfault_6_f0() -> None:
    print('cv2.imread')
    img = cv2.imread('tests/data/test_googleauth_export.png')

    yolo_v3_QR_detector = cv2.dnn.readNetFromDarknet(cfgFile='tests/data/qrcode-yolov3-tiny.cfg', darknetModel='tests/data/qrcode-yolov3-tiny_last.weights')
    yolo_v3_QR_detector.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)

    output_layer_names = yolo_v3_QR_detector.getLayerNames()
    output_layer_name = output_layer_names[yolo_v3_QR_detector.getUnconnectedOutLayers()[0] - 1]

    print('cv2.dnn.blobFromImage')
    _INPUT_SIZE = (416, 416)
    _CONF_THRESHOLD = 0.5

    blob = cv2.dnn.blobFromImage(img, 1 / 255, _INPUT_SIZE, swapRB=False, crop=False)

    print('yolo.yolo_v3_QR_detector.setInput')
    yolo_v3_QR_detector.setInput(blob=blob)

    # Transform the image to blob and predict
    # print('yolo_v3_QR_detector.forward')
    # output = yolo_v3_QR_detector.forward(output_layer_name)

    print('Done')


def test_cv2_segfault_6_f1() -> None:
    print('cv2.imread')
    img = cv2.imread('tests/data/test_googleauth_export.png')

    yolo_v3_QR_detector = cv2.dnn.readNetFromDarknet(cfgFile='tests/data/qrcode-yolov3-tiny.cfg', darknetModel='tests/data/qrcode-yolov3-tiny_last.weights')
    yolo_v3_QR_detector.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)

    output_layer_names = yolo_v3_QR_detector.getLayerNames()
    output_layer_name = output_layer_names[yolo_v3_QR_detector.getUnconnectedOutLayers()[0] - 1]

    print('cv2.dnn.blobFromImage')
    _INPUT_SIZE = (416, 416)
    _CONF_THRESHOLD = 0.5

    blob = cv2.dnn.blobFromImage(img, 1 / 255, _INPUT_SIZE, swapRB=False, crop=False)

    print('yolo.yolo_v3_QR_detector.setInput')
    yolo_v3_QR_detector.setInput(blob=blob)

    # Transform the image to blob and predict
    print('yolo_v3_QR_detector.forward')
    output = yolo_v3_QR_detector.forward(output_layer_name)

    print('Done')
