# The class for performing semantic segmentation is imported from pixelLib and we created an instance of the class.
import pixellib
from pixellib.semantic import semantic_segmentation
segment_image = semantic_segmentation()

# In the code below we loaded the xception model trained on pascal voc for segmenting objects. 
# The model can be downloaded from Github link mentioned below this comment line
# https://github.com/ayoolaolafenwa/PixelLib/releases/download/1.1/deeplabv3_xception_tf_dim_ordering_tf_kernels.h5
segment_image.load_pascalvoc_model("deeplabv3_xception_tf_dim_ordering_tf_kernels.h5") 

# Next we load the function to perform segmentation on an image. The function takes two parameters :
# path_to_image:- this is the path to the image to be segmented.
# output_image_name:- this is the path to save the segmented image. It will be saved in your current working directory.
# segment_image.segmentAsPascalvoc("path_to_image", output_image_name = "path_to_output_image")
segment_image.segmentAsPascalvoc("sample.jpg", output_image_name = "output.jpg")
