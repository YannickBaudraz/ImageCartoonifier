import mimetypes
from tkinter import filedialog

import cv2


def upload_image():
    extensions = [k for k, v in mimetypes.types_map.items() if 'image' in v]
    accepted_types = [("Image Files", extensions)]
    path = filedialog.askopenfilename(title="Select Image", filetypes=accepted_types)

    return path


def read_image(path):
    return cv2.imread(path)


def cartoonify(img):
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    filtered = cv2.bilateralFilter(rgb, 9, 250, 250)
    denoised = cv2.fastNlMeansDenoising(filtered, None, 10, 7, 21)
    cartoonified = cv2.cvtColor(denoised, cv2.COLOR_RGB2BGR)

    return cartoonified


def show(img):
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def save(cartoon_image):
    cv2.imwrite("cartoon.png", cartoon_image)


image_path = upload_image()

if image_path:
    image = read_image(image_path)
    cartoon = cartoonify(image)
    show(cartoon)
    save(cartoon)
