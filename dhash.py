import cv2
import sys
Size_width = 9
Size_height = 8


def calculate_dhash(img):
    """Calculates dhash of image object 
        :input :param: an image object
        :return dhash value
        """
    try:
        dhash = ''
        # check if an valid image in case of invalid image none is returned
        if img is not None:
            height, width = img.shape[:2]
            # check if the size of the image is larger than 9*8
            if width > Size_width and height > Size_height:
                # resizing the image
                img = cv2.resize(img, (Size_width, Size_height))
                # COnverting to grayscale
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                bits = []
                # xrange is similar to range,only difference is that range returns list while xrange returns an object of xrange which consumes less memory
                # img.shape[0]=width
                # img.shape[1]=height
                for row in range(img.shape[0]):
                    for col in range(img.shape[1]-1):
                        l = img[row][col]
                        r = img[row][col+1]
                        bits.append('1') if l > r else bits.append('0')

                for i in range(0, len(bits), 4):
                    dhash += hex(int(''.join(bits[i:i+4]), 2))
                dhash = dhash.replace('0x', '')
                return dhash
            else:
                return dhash
        else:
            return dhash
    except Exception as e:
        return False
