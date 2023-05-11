import time
import concurrent.futures
from PIL import Image, ImageFilter  # here need NEW package "Pillow"

img_names = [
    'Image00001.jpg',
    'Image00002.jpg',
    'Image00002.jpg',
    'Image00004.jpg',
    'Image00005.jpg',
    'Image00006.jpg',
    'Image00007.jpg',
    'Image00008.jpg',
    'Image00009.jpg',
    'Image00010.jpg'
]

start = time.perf_counter()

size = (1200, 1200)


def process_image(img_name):       # this func for one image
#for img_name in img_names:        # with "FOR" it's took 7,8 sec
    img = Image.open(img_name)

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f'processed/{img_name}')
    print(f'{img_name} was processed...')


if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_image, img_names)                  # with "MP" it's took 3,3 sec

    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     executor.map(process_image, img_names)                  # with "MP" it's took 2,7 sec !!!!!!!!!

    print(f'Finished in {time.perf_counter() - start} seconds')
