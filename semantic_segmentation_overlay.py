# we added the extra parameter overlay and set it to true and we obtained an image with a segmentation overlay on the objects.
import pixellib
from pixellib.semantic import semantic_segmentation
import cv2

segment_image = semantic_segmentation()
segment_image.load_pascalvoc_model("pascal.h5")
segmap, segoverlay = segment_image.segmentAsPascalvoc("sample.jpg", overlay= True)
cv2.imwrite("img.jpg", segoverlay)
print(segoverlay.shape)
