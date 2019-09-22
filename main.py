import dt
import os

import hamingdistance as hp
import cv2
import dhash
import numpy as np


# works till images are 50%resized and are exact duplicates and are rotated by an integral multiple of 90


ls = ['.jpeg', '.png', '.jpg']
list1 = {}
image_count = 0


def find_dhash_at_all_right_angles(img_path):
    """
        Returns a 64 bit string containing dhash value at all 90 angles.
        :input:param: image path
        :return:64 bit string containing dhash value at all 90 angles.
        """
    img = cv2.imread(img_path)
    img1 = cv2.medianBlur(img, 3)
    cv2.imshow("image", img1)
    cv2.waitKey(8000)
    dhash = ''
    # check if an valid image in case of invalid image none is returned
    if img1 is not None:
        for a in range(0, 4):
            rotated = np.rot90(img1, a)
            dhash += dhash.calculate_dhash(rotated)
        return dhash
    else:
        return False


try:
    # path contains the path where the scanning is to be started.
    path = ""
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            ext = os.path.splitext(name)[1]
            if ext in ls:
                image_count += 1
                path_of_file = os.path.join(root, name)
                val = find_dhash_at_all_right_angles(path_of_file)
                # incase of unsuccessful obtaining of dhash value of val would be ''
                if val:
                    available_hashes = list1.keys()
                    # if found=1 that means similar cropped image exists
                    found = 0
                    for val1 in available_hashes:
                        hd = hp.haming_distance(val, val1)
                        # None can be returned from
                        if not hd:
                            if hd < 6:
                                list1.setdefault(val1, []).append(path_of_file)
                                found = 1
                        #image = cv2.imread(path_of_file)
                        # cv2.imshow("Duplicate",image)
                            break
                        # we set hd=1 because we do not want to add it to the list
                        if not hd:
                            found = 1
                    if found == 0:
                        # no existing image is found so we would have to append first 16 bits of it
                        list1.setdefault(val[0:16], []).append(path_of_file)
except Exception as e:
    print("Error Occured:{0}".format(e))
list2 = list1.keys()
nonduplicates = len(list2)
# stop=timeit.default_timer()
print ("Total images ", image_count)
print ("\n")
print ("Total non duplicates %s", nonduplicates)
for c in list1:
    print (c)
    print (list1.get(c))
