# from PIL import Image, ImageFont
import argparse
import cv2

ASCII_ORDERS = {
    "basic": (
        " ",
        ".",
        "'",
        ",",
        ":",
        ";",
        "c",
        "l",
        "x",
        "o",
        "k",
        "X",
        "d",
        "O",
        "0",
        "K",
        "N",
    ),
    "better": ("@", "#", "8", "&", "o", ":", "*", ".", " "),
}


def convert_row_to_ascii(row):
    order = ASCII_ORDERS["basic"]
    return tuple(order[int(x / (255 / 16))] for x in row)[::-1]


def convert_to_ascii(input_grays):
    return tuple(convert_row_to_ascii(row) for row in input_grays)


def convert_image_to_ascii(input, resolution: int):
    img = cv2.imread(input)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (resolution, resolution))
    # cv2.imshow("Image", img)

    converted = convert_to_ascii(img)
    for row in converted:
        print(" ".join(row))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    parser = argparse.ArgumentParser(description="Set resolution for the script.")
    parser.add_argument(
        "--resolution", type=int, default=128, help="Resolution (default is 128)"
    )
    parser.add_argument("--input", type=str, help="Filepath for input image")

    args = parser.parse_args()
    resolution = args.resolution
    input = args.input

    convert_image_to_ascii(input, resolution)


if __name__ == "__main__":
    main()
