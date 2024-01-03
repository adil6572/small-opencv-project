import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode


def scan_barcode(image_path):
    try:
        img = cv.imread(image_path)
        barcodes = decode(img)

        decode_list = []

        if barcodes:
            print(f"Number of QRCode in {image_path}: {len(barcodes)}")

            for barcode in barcodes:
                data = barcode.data.decode('utf-8')
                points = np.array(barcode.polygon, np.int32)
                points = points.reshape((-1, 1, 2))

                cv.polylines(img, [points], True, (0, 255, 0), 4)
                point2 = barcode.rect
                cv.putText(img, data, (point2[0], point2[1] - 10),
                           cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

                decode_list.append((img.copy(), data, point2))
        else:
            return None

    except Exception as e:
        print(f"Exception: {e}")
        return None

    return decode_list


if __name__ == "__main__":
    image_list = ["./image1.jpg", "./image2.png", "./image3.png",
                  "./image4.jpg", "./image5.jpg", "./image6.jpeg"]

    for image in image_list:
        results = scan_barcode(image)
        if results:
            for result in results:
                img = result[0]
                data = result[1]

                cv.imshow("Image", img)
                print(f" QR Code data: {data}")

            cv.waitKey(0)
        else:
            print(f"No barcodes found in {image}")
