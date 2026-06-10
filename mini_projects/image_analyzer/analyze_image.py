import cv2
import matplotlib.pyplot as plt
from pathlib import Path
import math

def get_img():
    name = input("enter image file name with extension: ")
    return name


def load_img(name):
    
    script_dir = Path(__file__).resolve().parent
    img_path = script_dir / "images" / name

    img = cv2.imread(str(img_path))
    if img is None:
        raise FileNotFoundError("could not find the image")
    return img


def convert_rgb(bgr_img):
    rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)
    return rgb_img


def convert_gray(bgr_img):
    gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
    return gray_img


def plot_imgs(*imgs, titles=None):

    num_imgs = len(imgs)

    if num_imgs == 0:
        print("No images provided to plot")
        return
    
    fig, axes = plt.subplots(math.ceil(num_imgs / 3), min(3, num_imgs), figsize=(2 * min(num_imgs, 3), 2 * math.ceil(num_imgs / 3)))

    # if there's only 1 plot, plt.subplot returns only a single Axes object and not a list of axes of objects. Hence we convert it to list
    if num_imgs == 1:
        axes = [axes]
    else:
        axes = axes.flatten()

    for i, img in enumerate(imgs):
        if len(img.shape) == 2:
            axes[i].imshow(img, cmap='gray')
        else:
            axes[i].imshow(img)
    
        axes[i].axis('off')

        if titles and i < len(titles):
            axes[i].set_title(titles[i])

    plt.tight_layout()
    plt.show()


def main():
    try:
        name = get_img()
        image = load_img(name)
    except FileNotFoundError:
        print("Could not find image. Make sure you entered the correct file name and the file is inside images/ folder.")
        return
    
    img_rgb = convert_rgb(image)
    img_gray = convert_gray(image)

    plot_imgs(image, img_rgb, img_gray, image, image, titles = ['BGR', 'RGB', 'Grayscale'])


if __name__ == "__main__":
    main()