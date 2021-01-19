import cv2
import argparse
import colorama
import numpy as np
from colorama import Fore, Back, Style

colorama.init(autoreset = True)

def Banner():
    print(f"{Fore.YELLOW}  _______  _______  _______  ___   __   __  _______  _______  _______  {Fore.RED}       {Fore.BLUE}    ___   __   __  _______  _______  _______  _______  _______  _______  __   __  _______ ")
    print(f"{Fore.YELLOW} |   _   ||       ||       ||   | |  |_|  ||   _   ||       ||       | {Fore.RED}       {Fore.BLUE}   |   | |  |_|  ||   _   ||       ||       ||       ||       ||       ||  |_|  ||       |")
    print(f"{Fore.YELLOW} |  |_|  ||  _____||       ||   | |       ||  |_|  ||    ___||    ___| {Fore.RED}  ____ {Fore.BLUE}   |   | |       ||  |_|  ||    ___||    ___||____   ||_     _||    ___||       ||_     _|")
    print(f"{Fore.YELLOW} |       || |_____ |       ||   | |       ||       ||   | __ |   |___  {Fore.RED} |____|{Fore.BLUE}   |   | |       ||       ||   | __ |   |___  ____|  |  |   |  |   |___ |       |  |   |  ")
    print(f"{Fore.YELLOW} |       ||_____  ||      _||   | |       ||       ||   ||  ||    ___| {Fore.RED}       {Fore.BLUE}   |   | |       ||       ||   ||  ||    ___|| ______|  |   |  |    ___| |     |   |   |  ")
    print(f"{Fore.YELLOW} |   _   | _____| ||     |_ |   | | ||_|| ||   _   ||   |_| ||   |___  {Fore.RED}       {Fore.BLUE}   |   | | ||_|| ||   _   ||   |_| ||   |___ | |_____   |   |  |   |___ |   _   |  |   |  ")
    print(f"{Fore.YELLOW} |__| |__||_______||_______||___| |_|   |_||__| |__||_______||_______| {Fore.RED}       {Fore.BLUE}   |___| |_|   |_||__| |__||_______||_______||_______|  |___|  |_______||__| |__|  |___|  ")

    print('\n')
    print(f"  Writed by {Back.GREEN}{Fore.BLACK}1nj3ct0r")

    print('\n')

def GetArgs():
    Banner()

    parser = argparse.ArgumentParser("ASCImage")
    parser.add_argument("--input", type = str, default = "Data/Input.jpg", help = "Path to input image")
    parser.add_argument("--output", type = str, default = "Data/Output.txt", help = "Path to output text file")
    parser.add_argument("--column", type = int, default = 150, help = "Number of characters for output's width")
    parser.add_argument("--mode", type = str, default = "complex", choices = ["simple", "complex"],
        help = "10 or 70 different characters")

    args = parser.parse_args()
    return args

def main(opt):
    if opt.mode == "simple":
        char_list = "@%#*+=-:. "
    else:
        char_list = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

    num_cols = opt.column
    num_chars = len(char_list)
    image = cv2.imread(opt.input)
    try:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except:
        print(f"{Fore.RED} Incorrect image path...")

    height, width = image.shape
    cell_width = width / opt.column
    
    cell_height = 2 * cell_width
    num_rows = int(height / cell_height)
    if (num_cols > width or num_rows > height):
        cell_width = 6
        cell_height = 12
        num_cols = int(width / cell_width)
        num_rows = int(height / cell_height)
        print(f"{Fore.RED} Too many columns or rows! Use default setting...")

    output_file = open(opt.output, 'w')

    for i in range(num_rows):
        for j in range(num_cols):
            output_file.write(
                    char_list[min(int(np.mean(image[int(i * cell_height): min(int((i + 1) * cell_height), height),
                        int(j * cell_width): min(int((j + 1) * cell_width),
                            width)]) * num_chars / 255), num_chars - 1)])

        output_file.write('\n')

    output_file.close()

if __name__ == "__main__":
    opt = GetArgs()

    main(opt)
