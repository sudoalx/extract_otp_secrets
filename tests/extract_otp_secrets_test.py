# pytest for extract_otp_secrets.py

# Run tests:
# pytest

# Author: Scito (https://scito.ch)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
