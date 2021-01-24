import PIL.Image

print('''
github.com/RodricBr\n
\t<-#============================#->
\t  | Image to ASCII Generator   |
\t  | Not my idea not my script. |
\t  |       Youtube: Kite        |
\t<-#============================#->
''')

#ASCII Characters to output text
ascii_char = [' ', ' ', '.', '-', 'n', 'O', 'o', 's', 'S', 'v', 'V']
#Default '@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.'

#Resize image to new width
def resize_img(image, new_width=100): #Default 100
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_img = image.resize((new_width, new_height))
    return(resized_img)

#Convert each pixel to grayscale
def grayfy(image):
    grayscale_image = image.convert('L')
    return(grayscale_image)

def pixel_to_ascii(image):
    pixels = image.getdata()
    characters = ''.join((ascii_char[pixel//25] for pixel in pixels)) #Default 25
    return(characters)

def main(new_width=100): #Default 100
    path = input('[+] Enter a valid path to an imagen:\n>>> ')
    try:
        image = PIL.Image.open(path)
    except:
        print(f'{path} is not a valid pathname to an image!')
    new_image_data = pixel_to_ascii(grayfy(resize_img(image)))

    pixel_count = len(new_image_data)
    ascii_image = '\n'.join(new_image_data[i:(i + new_width)] for i in range(0, pixel_count, new_width))

    print(ascii_image)

    with open('imagem_ascii.txt', 'w') as f:
        f.write(ascii_image)
main()
