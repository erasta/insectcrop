import numpy as np
import urllib.request
import cv2
import os

try:
    os.mkdir( "out" )
except:
    pass

# def url_to_image(url):
# 	resp = urllib.request.urlopen(url)
# 	image = np.asarray(bytearray(resp.read()), dtype="uint8")
# 	image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
# 	return image
# img = url_to_image("https://uc5204b69423c30e717ff6a61658.previews.dropboxusercontent.com/p/thumb/AAsy9MYUdbGP5iAo0-Mb-8TaZKpoyZMeGu6ctYkHRH9VG8P6rbVeADFOtqLDiuvWmd_kuBMTTCqAMCTDfJn_sIHZj2nHyiyO234exDVUpyGbTNpqtkGZigbNSNbfodaX8qn4kOdGPurkNl84ybtLloaM_VTmncfs0kVK7NUyfdJ88m-u7Vz133zP4X3BOOeBB_WGkJrCxoTVzpQIcmYr6mhothTvSTpL89eVCOotU_eVfSy5eJ7v9UF0ULgHYFhbqmxLNvUKhlP259_q8RKTmx5nzwEcgidguO80hycVN1Nl_U7aVjt5zeWj0rZzvxq3Qy55LTvClSWU4cvDy_bnbWKOE3XpA1TTyVWw9ZpHnzLHPSmlmNvAYh7bOS5lLuP95vGuH46TizZHL_CQ80lEFUx1tkPbd1ifRG-y7cPZwQAAtebkCn66BS9GbgzUvS7C_zN5kZJyalHCpG86w6jCzxYd/p.jpeg?fv_content=true&size_mode=5")
files = os.listdir("input")
index = 0
compIndex = 0
for f in files:
    index = index + 1
    if f.endswith(".jpg") or f.endswith(".jpeg"):
        print ("working on " + str(index) + "/" + str(len(files)) + ": " + f)
        img = cv2.imread('input/' + f, cv2.IMREAD_COLOR)
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        bw_img = cv2.bitwise_not(bw_img[:, :, 1])

        [num_labels, labels, stats, centroids] = cv2.connectedComponentsWithStats(bw_img, 4, cv2.CV_32S)

        for stat in stats:
            [x, y, w, h, area] = stat
            if w > 200 and h > 200 and w < 1000 and h < 1000:
                compIndex = compIndex + 1
                cv2.imwrite("out/" + str(compIndex) + ".jpg", img[y:y+h, x:x+w])