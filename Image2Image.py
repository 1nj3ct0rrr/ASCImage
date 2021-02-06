import cv2
import argparse
import colorama
import numpy as np
from colorama import Fore, Back, Style
from PIL import Image, ImageFont, ImageDraw, ImageOps

colorama.init(autoreset=True)


def Banner():
    print(
        f'{Fore.YELLOW}  _______  _______  _______  ___   __   __  _______  _______  _______  {Fore.RED}       {Fore.BLUE}    ___   __   __  _______  _______  _______  _______  ___   __   __  _______  _______  _______ '
    )
    print(
        f'{Fore.YELLOW} |   _   ||       ||       ||   | |  |_|  ||   _   ||       ||       | {Fore.RED}       {Fore.BLUE}   |   | |  |_|  ||   _   ||       ||       ||       ||   | |  |_|  ||   _   ||       ||       |'
    )
    print(
        f'{Fore.YELLOW} |  |_|  ||  _____||       ||   | |       ||  |_|  ||    ___||    ___| {Fore.RED}  ____ {Fore.BLUE}   |   | |       ||  |_|  ||    ___||    ___||____   ||   | |       ||  |_|  ||    ___||    ___|'
    )
    print(
        f'{Fore.YELLOW} |       || |_____ |       ||   | |       ||       ||   | __ |   |___  {Fore.RED} |____|{Fore.BLUE}   |   | |       ||       ||   | __ |   |___  ____|  ||   | |       ||       ||   | __ |   |___ '
    )
    print(
        f'{Fore.YELLOW} |       ||_____  ||      _||   | |       ||       ||   ||  ||    ___| {Fore.RED}       {Fore.BLUE}   |   | |       ||       ||   ||  ||    ___|| ______||   | |       ||       ||   ||  ||    ___|'
    )
    print(
        f'{Fore.YELLOW} |   _   | _____| ||     |_ |   | | ||_|| ||   _   ||   |_| ||   |___  {Fore.RED}       {Fore.BLUE}   |   | | ||_|| ||   _   ||   |_| ||   |___ | |_____ |   | | ||_|| ||   _   ||   |_| ||   |___ '
    )
    print(
        f'{Fore.YELLOW} |__| |__||_______||_______||___| |_|   |_||__| |__||_______||_______| {Fore.RED}       {Fore.BLUE}   |___| |_|   |_||__| |__||_______||_______||_______||___| |_|   |_||__| |__||_______||_______|'
    )

    print('\n')
    print(f'  Writed by {Back.GREEN}{Fore.BLACK}1nj3ct0r')

    print('\n')


def GetArgs():
    Banner()

    parser = argparse.ArgumentParser('ASCImage')
    parser.add_argument('--input',
                        type=str,
                        default='Data/Input.jpg',
                        help='Path to input image')
    parser.add_argument('--output',
                        type=str,
                        default='Data/Output.jpg',
                        help='Path to output image')
    parser.add_argument('--column',
                        type=int,
                        default=200,
                        help='Number of characters for output\'s width')

    parser.add_argument('--scale', type=int, default=2, help='Upsize output')
    parser.add_argument('--background',
                        type=str,
                        default='white',
                        choices=['black', 'white'],
                        help='Background color')
    parser.add_argument('--mode',
                        type=str,
                        default='complex',
                        choices=['simple', 'complex'],
                        help='10 or 70 different characters')

    args = parser.parse_args()

    return args


def main(opt):
    if opt.mode == 'simple':
        char_list = '@%#*+=-:. '
    else:
        char_list = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`\'. '

    if opt.background == 'white':
        bg_code = 255
    else:
        bg_code = 0

    num_cols = opt.column
    num_chars = len(char_list)
    image = cv2.imread(opt.input)
    try:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except:
        print(f'{Fore.RED} Incorrect image path...')

    font = ImageFont.truetype('Fonts/DejaVuSansMonoBold.ttf')

    height, width = image.shape
    cell_width = width / opt.column

    cell_height = 2 * cell_width
    num_rows = int(height / cell_height)
    if num_cols > width or num_rows > height:
        cell_width = 6
        cell_height = 12
        num_cols = int(width / cell_width)
        num_rows = int(height / cell_height)
        print(f'{Fore.RED} Too many columns or rows! Use default setting...')

    char_width, char_height = font.getsize('A')

    out_width = char_width * num_cols
    out_height = 2 * char_height * num_rows
    out_image = Image.new('L', (out_width, out_height), bg_code)

    draw = ImageDraw.Draw(out_image)

    for i in range(num_rows):
        line = ''.join([
            char_list[min(
                int(
                    np.mean(image[
                        int(i * cell_height):min(int(
                            (i + 1) * cell_height), height),
                        int(j * cell_width):min(int(
                            (j + 1) * cell_width), width)]) * num_chars / 255),
                num_chars - 1)] for j in range(num_cols)
        ]) + '\n'

        draw.text((0, i * char_height), line, fill=255 - bg_code, font=font)

    if opt.background == 'white':
        cropped_image = ImageOps.invert(out_image).getbbox()
    else:
        cropped_image = out_image.getbbox()

    out_image = out_image.crop(cropped_image)

    out_image.save(opt.output)


if __name__ == '__main__':
    opt = GetArgs()

    main(opt)
