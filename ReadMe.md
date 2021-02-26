# ASCImage

Hello! With this Python project, you can see the images and photos you have in ASCII-Art ✏️🤩

## WTF is ASCII-Art

ASCII-Art can be a photo or text (Or even a work of art) created by using different characters on computer or laptop keyboard or any other characters 🤔🔠🔡🔢🔣

## Scripts

In this repository you can see **2 scripts**, which I will now explain the use of each separately:

- **Image to Text (Image2Text.py)**:
  By using this script, you can give your photo as input and receive a **text file (.txt)** as output file in which your photo is in the form of ASCII-Art ✏️😉
- **Image to Image (Image2Image.py)**:
By using this script, you can give your photo as input and receiev a file as an **image (.png, .jpg, ...)** as an output file in which your photo is a ASCII-Art, but you can not change it because the output file is a file in the form of an image 😉✏️

## Example

- Input Image ➡️
  ![Input](https://uupload.ir/files/6zbj_test.png)

- Output Image ⬅️
  ![Output](https://uupload.ir/files/lkdp_result.png)

## WTF Should I Do

- **How to run 🤷🤷‍♂️**

  You can use the `python3 {NAME OF SCRIPT}.py --help` command to find out what the scripts need and how they run 😁

- **Python Packages**
  - CV2
  - Numpy
  - Argparse
  - Colorama
  - PIL (Image, ImageFont, ImageDraw, ImageOps)

- **Example for run**
  - Image2Text:
    ```python
    python3 Image2Text.py --input input.jpg --output output.txt --column 200 --mode simple
    ```
  - Image2Image:
    ```python
    python3 Image2Image.py --input input.jpg --output output.jpg --column 200 --scale 2 --background white --mode simple
    ```
