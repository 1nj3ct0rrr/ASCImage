# ASCImage

Hi, My name is Hesam and I come back with another interesting project!
In this project I write a python script to convert images to ASCII text art

We have 2 python scrip: **Image2Text.py** and **Image2Image.py**

- **Image to Text**:
  with this python script, you can make a text file (.txt) that when you open this file, you
  see your text art of input image -> Image file (.png, .jpg and ...) to text file (.txt)
- **Image to Image**:
  with this python script, you can make an image file (.png or ...) that when you open this file,
  you see your text art of your input image as a picture -> Image file (.png, .jpg and ...) to image file

### Example

- Input Image
  ![Input](https://uupload.ir/files/6zbj_test.png)

- Output Image
  ![Output](https://uupload.ir/files/lkdp_result.png)

### Installation

- **How to run**

  You can run `python3 {NAME OF SCRIPT}.py --help` to see how to run this scripts with command

- **Python Packages**
  - CV2
  - Argparse
  - Colorama
  - Numpy
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
