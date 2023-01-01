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

from __future__ import annotations  # for compatibility with PYTHON < 3.11
import io
import os
import pathlib
import sys
import colorama
import cv2  # type: ignore
import pyzbar.pyzbar as zbar  # type: ignore

import pytest
from pytest_mock import MockerFixture

import extract_otp_secrets
from utils import (file_exits, quick_and_dirty_workaround_encoding_problem,
                   read_binary_file_as_stream, read_csv, read_csv_str,
                   read_file_to_str, read_json, read_json_str,
                   replace_escaped_octal_utf8_bytes_with_str, count_files_in_dir)

qreader_available: bool = extract_otp_secrets.qreader_available


# Quickfix comment
# @pytest.mark.skipif(sys.platform.startswith("win") or not qreader_available or sys.implementation.name == 'pypy' or sys.version_info >= (3, 10), reason="Quickfix")


def test_cv2_segfault_1(qr_mode: str) -> None:
    print(f'QRmode: {qr_mode}')

    print('cv2.imread')
    img = cv2.imread('tests/data/test_googleauth_export.png')

    qr_mode_2 = extract_otp_secrets.QRMode[qr_mode]

    print(f'detect and decode for qr_mode {qr_mode_2}')

    print('Done')


def test_cv2_segfault_2(qr_mode: str) -> None:
    print(f'QRmode: {qr_mode}')

    print('cv2.imread')
    img = cv2.imread('tests/data/test_googleauth_export.png')

    qr_mode_2 = extract_otp_secrets.QRMode[qr_mode]

    print(f'detect and decode for qr_mode {qr_mode_2}')
    if qr_mode_2 in [extract_otp_secrets.QRMode.QREADER, extract_otp_secrets.QRMode.DEEP_QREADER]:

        print('cv.QRCodeDetector()')
        cv2.QRCodeDetector()

    elif qr_mode_2 == extract_otp_secrets.QRMode.CV2:
        cv2.QRCodeDetector().detectAndDecode(img)
    elif qr_mode_2 == extract_otp_secrets.QRMode.WECHAT:
        cv2.wechat_qrcode.WeChatQRCode().detectAndDecode(img)
    elif qr_mode_2 == extract_otp_secrets.QRMode.ZBAR:
        zbar.decode(img)

    print('Done')


def test_cv2_segfault_3(qr_mode: str) -> None:
    print(f'QRmode: {qr_mode}')

    print('cv2.imread')
    img = cv2.imread('tests/data/test_googleauth_export.png')

    qr_mode_2 = extract_otp_secrets.QRMode[qr_mode]

    print(f'detect and decode for qr_mode {qr_mode_2}')
    if qr_mode_2 in [extract_otp_secrets.QRMode.QREADER, extract_otp_secrets.QRMode.DEEP_QREADER]:

        print('cv.QRCodeDetector()')
        cv2.QRCodeDetector()

        print('from __yolo_v3_qr_detector.yolov3_qr_detector import _YoloV3QRDetector')
        from __yolo_v3_qr_detector.yolov3_qr_detector import _YoloV3QRDetector

    elif qr_mode_2 == extract_otp_secrets.QRMode.CV2:
        cv2.QRCodeDetector().detectAndDecode(img)
    elif qr_mode_2 == extract_otp_secrets.QRMode.WECHAT:
        cv2.wechat_qrcode.WeChatQRCode().detectAndDecode(img)
    elif qr_mode_2 == extract_otp_secrets.QRMode.ZBAR:
        zbar.decode(img)

    print('Done')


def test_cv2_segfault_4(qr_mode: str) -> None:
    print(f'QRmode: {qr_mode}')

    print('cv2.imread')
    img = cv2.imread('tests/data/test_googleauth_export.png')

    qr_mode_2 = extract_otp_secrets.QRMode[qr_mode]

    print(f'detect and decode for qr_mode {qr_mode_2}')
    if qr_mode_2 in [extract_otp_secrets.QRMode.QREADER, extract_otp_secrets.QRMode.DEEP_QREADER]:

        print('cv.QRCodeDetector()')
        cv2.QRCodeDetector()

        print('from __yolo_v3_qr_detector.yolov3_qr_detector import _YoloV3QRDetector')
        from __yolo_v3_qr_detector.yolov3_qr_detector import _YoloV3QRDetector

        print('_YoloV3QRDetector()')
        _YoloV3QRDetector()

    elif qr_mode_2 == extract_otp_secrets.QRMode.CV2:
        cv2.QRCodeDetector().detectAndDecode(img)
    elif qr_mode_2 == extract_otp_secrets.QRMode.WECHAT:
        cv2.wechat_qrcode.WeChatQRCode().detectAndDecode(img)
    elif qr_mode_2 == extract_otp_secrets.QRMode.ZBAR:
        zbar.decode(img)

    print('Done')


def test_cv2_segfault_5(qr_mode: str) -> None:
    print(f'QRmode: {qr_mode}')

    print('cv2.imread')
    img = cv2.imread('tests/data/test_googleauth_export.png')

    qr_mode_2 = extract_otp_secrets.QRMode[qr_mode]

    print(f'detect and decode for qr_mode {qr_mode_2}')
    if qr_mode_2 in [extract_otp_secrets.QRMode.QREADER, extract_otp_secrets.QRMode.DEEP_QREADER]:

        print('cv.QRCodeDetector()')
        cv2.QRCodeDetector()

        print('from __yolo_v3_qr_detector.yolov3_qr_detector import _YoloV3QRDetector')
        from __yolo_v3_qr_detector.yolov3_qr_detector import _YoloV3QRDetector

        print('_YoloV3QRDetector()')
        _YoloV3QRDetector()

        print('from qreader import QReader')
        from qreader import QReader

    elif qr_mode_2 == extract_otp_secrets.QRMode.CV2:
        cv2.QRCodeDetector().detectAndDecode(img)
    elif qr_mode_2 == extract_otp_secrets.QRMode.WECHAT:
        cv2.wechat_qrcode.WeChatQRCode().detectAndDecode(img)
    elif qr_mode_2 == extract_otp_secrets.QRMode.ZBAR:
        zbar.decode(img)

    print('Done')


def test_cv2_segfault_6(qr_mode: str) -> None:
    print(f'QRmode: {qr_mode}')

    print('cv2.imread')
    img = cv2.imread('tests/data/test_googleauth_export.png')

    qr_mode_2 = extract_otp_secrets.QRMode[qr_mode]

    print(f'detect and decode for qr_mode {qr_mode_2}')
    if qr_mode_2 in [extract_otp_secrets.QRMode.QREADER, extract_otp_secrets.QRMode.DEEP_QREADER]:

        print('cv.QRCodeDetector()')
        cv2.QRCodeDetector()

        print('from __yolo_v3_qr_detector.yolov3_qr_detector import _YoloV3QRDetector')
        from __yolo_v3_qr_detector.yolov3_qr_detector import _YoloV3QRDetector

        print('_YoloV3QRDetector()')
        _YoloV3QRDetector()

        print('from qreader import QReader')
        from qreader import QReader

        print('QReader()')
        qreader = QReader()

    elif qr_mode_2 == extract_otp_secrets.QRMode.CV2:
        cv2.QRCodeDetector().detectAndDecode(img)
    elif qr_mode_2 == extract_otp_secrets.QRMode.WECHAT:
        cv2.wechat_qrcode.WeChatQRCode().detectAndDecode(img)
    elif qr_mode_2 == extract_otp_secrets.QRMode.ZBAR:
        zbar.decode(img)

    print('Done')


def test_cv2_segfault_6_d1(qr_mode: str) -> None:
    print(f'QRmode: {qr_mode}')

    print('cv2.imread')
    img = cv2.imread('tests/data/test_googleauth_export.png')

    qr_mode_2 = extract_otp_secrets.QRMode[qr_mode]

    print(f'detect and decode for qr_mode {qr_mode_2}')
    if qr_mode_2 in [extract_otp_secrets.QRMode.QREADER, extract_otp_secrets.QRMode.DEEP_QREADER]:

        print('cv.QRCodeDetector()')
        cv2_qr =cv2.QRCodeDetector()

        print('from __yolo_v3_qr_detector.yolov3_qr_detector import _YoloV3QRDetector')
        from __yolo_v3_qr_detector.yolov3_qr_detector import _YoloV3QRDetector

        print('_YoloV3QRDetector()')
        yolo = _YoloV3QRDetector()

        print('from qreader import QReader')
        from qreader import QReader

        print('QReader()')
        qreader = QReader()

        print('yolo.detect')
        yolo.detect(img)

    elif qr_mode_2 == extract_otp_secrets.QRMode.CV2:
        cv2.QRCodeDetector().detectAndDecode(img)
    elif qr_mode_2 == extract_otp_secrets.QRMode.WECHAT:
        cv2.wechat_qrcode.WeChatQRCode().detectAndDecode(img)
    elif qr_mode_2 == extract_otp_secrets.QRMode.ZBAR:
        zbar.decode(img)

    print('Done')


def test_cv2_segfault_6_d2(qr_mode: str) -> None:
    print(f'QRmode: {qr_mode}')

    print('cv2.imread')
    img = cv2.imread('tests/data/test_googleauth_export.png')

    qr_mode_2 = extract_otp_secrets.QRMode[qr_mode]

    print(f'detect and decode for qr_mode {qr_mode_2}')
    if qr_mode_2 in [extract_otp_secrets.QRMode.QREADER, extract_otp_secrets.QRMode.DEEP_QREADER]:

        print('cv.QRCodeDetector()')
        cv2_qr =cv2.QRCodeDetector()

        print('from __yolo_v3_qr_detector.yolov3_qr_detector import _YoloV3QRDetector')
        from __yolo_v3_qr_detector.yolov3_qr_detector import _YoloV3QRDetector

        print('_YoloV3QRDetector()')
        yolo = _YoloV3QRDetector()

        print('from qreader import QReader')
        from qreader import QReader

        print('QReader()')
        qreader = QReader()

        print('yolo.detect')
        yolo.detect(img)

        print('yolo.detect')
        cv2_qr.detect(img)

    elif qr_mode_2 == extract_otp_secrets.QRMode.CV2:
        cv2.QRCodeDetector().detectAndDecode(img)
    elif qr_mode_2 == extract_otp_secrets.QRMode.WECHAT:
        cv2.wechat_qrcode.WeChatQRCode().detectAndDecode(img)
    elif qr_mode_2 == extract_otp_secrets.QRMode.ZBAR:
        zbar.decode(img)

    print('Done')


def test_cv2_segfault_6_a(qr_mode: str) -> None:
    print(f'QRmode: {qr_mode}')

    print('cv2.imread')
    img = cv2.imread('tests/data/test_googleauth_export.png')

    qr_mode_2 = extract_otp_secrets.QRMode[qr_mode]

    print(f'detect and decode for qr_mode {qr_mode_2}')
    if qr_mode_2 in [extract_otp_secrets.QRMode.QREADER, extract_otp_secrets.QRMode.DEEP_QREADER]:

        print('cv.QRCodeDetector()')
        cv2.QRCodeDetector()

        print('from __yolo_v3_qr_detector.yolov3_qr_detector import _YoloV3QRDetector')
        from __yolo_v3_qr_detector.yolov3_qr_detector import _YoloV3QRDetector

        print('_YoloV3QRDetector()')
        _YoloV3QRDetector()

        print('from qreader import QReader')
        from qreader import QReader

        print('QReader()')
        qreader = QReader()

        print('qreader.detect(img)')
        found, bbox = qreader.detect(img)

    elif qr_mode_2 == extract_otp_secrets.QRMode.CV2:
        cv2.QRCodeDetector().detectAndDecode(img)
    elif qr_mode_2 == extract_otp_secrets.QRMode.WECHAT:
        cv2.wechat_qrcode.WeChatQRCode().detectAndDecode(img)
    elif qr_mode_2 == extract_otp_secrets.QRMode.ZBAR:
        zbar.decode(img)

    print('Done')


def test_cv2_segfault_6_b(qr_mode: str) -> None:
    print(f'QRmode: {qr_mode}')

    print('cv2.imread')
    img = cv2.imread('tests/data/test_googleauth_export.png')

    qr_mode_2 = extract_otp_secrets.QRMode[qr_mode]

    print(f'detect and decode for qr_mode {qr_mode_2}')
    if qr_mode_2 in [extract_otp_secrets.QRMode.QREADER, extract_otp_secrets.QRMode.DEEP_QREADER]:

        print('cv.QRCodeDetector()')
        cv2.QRCodeDetector()

        print('from __yolo_v3_qr_detector.yolov3_qr_detector import _YoloV3QRDetector')
        from __yolo_v3_qr_detector.yolov3_qr_detector import _YoloV3QRDetector

        print('_YoloV3QRDetector()')
        _YoloV3QRDetector()

        print('from qreader import QReader')
        from qreader import QReader

        print('QReader()')
        qreader = QReader()

        print('qreader.detect(img)')
        found, bbox = qreader.detect(img)

        print('qreader.decode(img, bbox)')
        qreader.decode(img, bbox)

    elif qr_mode_2 == extract_otp_secrets.QRMode.CV2:
        cv2.QRCodeDetector().detectAndDecode(img)
    elif qr_mode_2 == extract_otp_secrets.QRMode.WECHAT:
        cv2.wechat_qrcode.WeChatQRCode().detectAndDecode(img)
    elif qr_mode_2 == extract_otp_secrets.QRMode.ZBAR:
        zbar.decode(img)

    print('Done')


def test_cv2_segfault_7(qr_mode: str) -> None:
    print(f'QRmode: {qr_mode}')

    print('cv2.imread')
    img = cv2.imread('tests/data/test_googleauth_export.png')

    qr_mode_2 = extract_otp_secrets.QRMode[qr_mode]

    print(f'detect and decode for qr_mode {qr_mode_2}')
    if qr_mode_2 in [extract_otp_secrets.QRMode.QREADER, extract_otp_secrets.QRMode.DEEP_QREADER]:

        print('cv.QRCodeDetector()')
        cv2.QRCodeDetector()

        print('from __yolo_v3_qr_detector.yolov3_qr_detector import _YoloV3QRDetector')
        from __yolo_v3_qr_detector.yolov3_qr_detector import _YoloV3QRDetector

        print('_YoloV3QRDetector()')
        _YoloV3QRDetector()

        print('from qreader import QReader')
        from qreader import QReader

        print('QReader()')
        qreader = QReader()

        print('QReader().detect_and_decode')
        qreader.detect_and_decode(img, qr_mode == extract_otp_secrets.QRMode.DEEP_QREADER)

    elif qr_mode_2 == extract_otp_secrets.QRMode.CV2:
        cv2.QRCodeDetector().detectAndDecode(img)
    elif qr_mode_2 == extract_otp_secrets.QRMode.WECHAT:
        cv2.wechat_qrcode.WeChatQRCode().detectAndDecode(img)
    elif qr_mode_2 == extract_otp_secrets.QRMode.ZBAR:
        zbar.decode(img)

    print('extract_otp_secrets.main')
    extract_otp_secrets.main(['--qr', qr_mode, 'tests/data/test_googleauth_export.png'])

    print('Done')


EXPECTED_STDOUT_FROM_EXAMPLE_EXPORT_PNG = '''Name:    Test1:test1@example1.com
Secret:  JBSWY3DPEHPK3PXP
Issuer:  Test1
Type:    totp

Name:    Test2:test2@example2.com
Secret:  JBSWY3DPEHPK3PXQ
Issuer:  Test2
Type:    totp

Name:    Test3:test3@example3.com
Secret:  JBSWY3DPEHPK3PXR
Issuer:  Test3
Type:    totp

'''
