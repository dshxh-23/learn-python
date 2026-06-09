import cv2
import matplotlib.pyplot as plt
from pathlib import Path

def get_img():
    name = input("enter image file name with extension: ")
    return name


def load_img(name):
    img_path = Path(f"images/{name}")
    img = cv2.imread(img_path)
    if img is None:
        raise FileNotFoundError("could not find the image")
    return img


def convert_rgb(bgr_img):
    rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)
    return rgb_img

def convert_gray(bgr_img):
    gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
    return gray_img


def plot_imgs(*args):
    fig, axes = plt.subplots(nrows = 1, ncols=len(args))
    for img in args:
        ...


def main():
    try:
        image = load_img(get_img())
    except FileNotFoundError:
        print("Could not find image. Make sure you entered the correct file name and the file is inside images/ folder.")
    
    img_rgb = convert_rgb(image)
    img_gray = convert_gray(image)

    