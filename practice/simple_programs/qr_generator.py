import qrcode

def main():
    link = input("Hyperlink: ")
    qr_img =qrcode.make(link)
    print(type(qr_img))
    qr_img.save("QR Code.png")

if __name__ == "__main__":
    main()