import math
from pathlib import Path
import matplotlib.pyplot as plt
import cv2

# ==== ==== ==== ====

def get_img():
    name = input("enter image file name with extension: ")
    return name

# -- -- -- --

def load_img(name):
    
    proj_dir = Path(__file__).resolve().parent
    img_path = proj_dir / "images" / name

    img = cv2.imread(str(img_path))
    if img is None:
        raise FileNotFoundError("could not find the image")
    return img

# -- -- -- --

def convert_rgb(bgr_img):
    rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)
    return rgb_img

# -- -- -- --

def convert_gray(bgr_img):
    gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
    return gray_img

# -- -- -- --

def plot_imgs(*imgs, titles=None):

    num_imgs = len(imgs)

    if num_imgs == 0:
        print("No images provided to plot")
        return
    
    fig, axes = plt.subplots(math.ceil(num_imgs / 3), min(3, num_imgs), figsize=(2 * min(num_imgs, 3), 2 * math.ceil(num_imgs / 3)))

    # convert axes to list if it's not already
    if num_imgs == 1:
        axes = [axes]
    else:       # for more than 3 images
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


def save_img(img, name, ext):
    """saves img as name.ext in outputs/. the image must be in BGR format"""

    proj_dir = Path(__file__).resolve().parent
    op_dir = proj_dir / 'outputs'
    op_dir.mkdir(parents=True, exist_ok=True)
    file_path = op_dir / f"{name}.{ext}"

    success = cv2.imwrite(f"{str(file_path)}", img)

    if success:
        print(f"{name}.{ext} saved successfully at {str(op_dir)}")
    else:
        print("failed to save file")


def main():
    try:
        name = get_img()
        image = load_img(name)
    except FileNotFoundError:
        print("could not find image")
        return
    
    save_img(image, "orig_img", "png")

    img_gray = convert_gray(image)
    save_img(img_gray, "gray_img", "png")


    plot_imgs(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), img_gray, image, titles = ['Original', 'Grayscale', 'BR inverted'])


if __name__ == "__main__":
    main()