import pyqrcode
import cv2
import random
import png
import links


# methods

def encode(val, filename):
    """
    :param val: the value to be encoded
    :param filename: what the filename will be
    :return: saves qr code under filename.png
    """
    qr = pyqrcode.create(val)
    qr.png(filename + ".png")


def decode(filename):
    """
    :param filename: the name of the file
    :return: prints the data decoded
    """
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(cv2.imread(filename + ".png"))
    print(f"\nQRCode data: {data} from {filename}.png")


def generate_qr():
    encode(random.choice(links.links), "GW")


# driver

user_input = ""

while user_input != "exit":

    if input("\nWelcome. If you would like to generate a QR code enter c. Otherwise enter d to generate QR code with a "
             "link to a website with a green message: ") == "d":
        generate_qr()
    else:
        print("Type encode below to encode a piece of data to a QR code")
        print("Otherwise type the name of a file to decode it (the name without '.png')")
        user_input = input("What would you like to do? Type:\n")

        if user_input == "exit":
            break
        elif user_input == "encode":
            user_input = input("\nWhat would you like to encode?\n")
            user_filename = input("\nWhat would you like the name of the file to be (without '.png')\n")
            encode(user_input, user_filename)
        else:
            decode(user_input)
