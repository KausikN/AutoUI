���      �PythonCodeTokenizer��Code���)��}�(�	code_path��TestCodes/ImageOps.py��
code_lines�]�(�'''
��Function Chooser Program
��'''
��
��
# Imports
��
import os
��import cv2
��import numpy as np
�� import matplotlib.pyplot as plt
�hhh�# Main Functions
��class Image:
��)    def __init__(self, path, data=None):
��        self.path = path
��        self.data = data
��#CEND
�h�def ImageAdd(a, b):
��    if a is None or b is None:
��        return None
��    return a + b
��#FEND
�h�def ImageAvg(a, b):
��    if a is None or b is None:
��        return None
��    return (a + b) / 2
��#FEND
�h�;def ImageThreshold(a, threshold, replacementVal=[0, 255]):
��'    if a is None or threshold is None:
��        return None
��    A = np.copy(a)
��8    A[np.nonzero(a < threshold[0])] = replacementVal[0]
��8    A[np.nonzero(a > threshold[1])] = replacementVal[1]
��    return A
��#FEND
�h�# Driver Code
��	# Params
��$Image_1_Path = '' #TYPE: FILE Image
��$Image_2_Path = '' #TYPE: FILE Image
��savePath = '' #TYPE: DIR
�h�Threshold_LowEnd = 0
��Replacement_LowEnd = 0
��Threshold_HighEnd = 255
��Replacement_HighEnd = 255
�h�JOperation = None #TYPE: SELECTVAL NOTYPE ImageAdd,ImageAvg,ImageThreshold
��	# Params
��imgSize = (100, 100, 3)
�h�print("Started Image Ops")
�h�2Threshold = (Threshold_LowEnd, Threshold_HighEnd)
��=Replacement_Vals = (Replacement_LowEnd, Replacement_HighEnd)
�h�# Read Images and Resize
��aaa = np.array([])
��	A = None
��	B = None
��if Image_1_Path is not None:
��!    A = cv2.imread(Image_1_Path)
��Q    A = cv2.resize(cv2.cvtColor(A, cv2.COLOR_BGR2RGB), (imgSize[0], imgSize[1]))
��else:
��B    A = cv2.resize(np.zeros((1, 1, 3)), (imgSize[0], imgSize[1]))
��if Image_2_Path is not None:
��!    B = cv2.imread(Image_2_Path)
��Q    B = cv2.resize(cv2.cvtColor(B, cv2.COLOR_BGR2RGB), (imgSize[0], imgSize[1]))
��else:
��B    B = cv2.resize(np.zeros((1, 1, 3)), (imgSize[0], imgSize[1]))
�h�# Perform Chosen Operation
��Output = None
�� if Operation == ImageThreshold:
��7    Output = Operation(A, Threshold, Replacement_Vals)
��else:
��    Output = Operation(A, B)
��*Output = np.array(Output, dtype=np.uint8)
�h�# Save Output
��if savePath is not None:
��>    cv2.imwrite(os.path.join(savePath, "Output.png"), Output)
�h�# Display Outputs
��print("Plotting Results")
��plt.subplot(1, 3, 1)
��plt.imshow(A)
��plt.subplot(1, 3, 2)
��plt.imshow(B)
��plt.subplot(1, 3, 3)
��plt.imshow(Output)
��plt.show()
�h�print("Ended Image Ops")�e�script_desc��Function Chooser Program��imports�]�(�	import os��
import cv2��import numpy as np��import matplotlib.pyplot as plt�e�classes�]�h �Class���)��}�(�name�� Image��code�]�(�(    def __init__(self, path, data=None):��        self.path = path��        self.data = data�euba�	functions�]�(h �Function���)��}�(hi�	 ImageAdd��desc�� ��
parameters�]�(�a��b�ehk]�(�    if a is None or b is None:��        return None��    return a + b�eubhs)��}�(hi�	 ImageAvg�hwhxhy]�(h{h|ehk]�(�    if a is None or b is None:��        return None��    return (a + b) / 2�eubhs)��}�(hi� ImageThreshold�hwhxhy]�(h{�	threshold��replacementVal=[0��255]�ehk]�(�&    if a is None or threshold is None:��        return None��    A = np.copy(a)��7    A[np.nonzero(a < threshold[0])] = replacementVal[0]��7    A[np.nonzero(a > threshold[1])] = replacementVal[1]��    return A�eube�script_parameters�]�(h �ScriptParameter���)��}�(hi�Image_1_Path��value�hx�value_prefix��'��value_suffix�h��type��builtins��str����ui_mode��FILE��	otherData�}��ext�]�(�.png��.jpg��.jpeg��.bmp��.JPG��.PNG�esubh�)��}�(hi�Image_2_Path�h�hxh�h�h�h�h�h�h�h�h�}�h�h�subh�)��}�(hi�savePath�h�hxh�h�h�h�h�h�h��DIR�h�}�ubh�)��}�(hi�Threshold_LowEnd�h�K h�hxh�hxh�h��int���h�Nh�}�ubh�)��}�(hi�Replacement_LowEnd�h�K h�hxh�hxh�h�h�Nh�}�ubh�)��}�(hi�Threshold_HighEnd�h�K�h�hxh�hxh�h�h�Nh�}�ubh�)��}�(hi�Replacement_HighEnd�h�K�h�hxh�hxh�h�h�Nh�}�ubh�)��}�(hi�	Operation�h�]�(�ImageAdd��ImageAvg��ImageThreshold�eh�hxh�hxh�h�h��	SELECTVAL�h�}�ube�driver_code�]�(�# Driver Code��imgSize = (100, 100, 3)��print("Started Image Ops")��1Threshold = (Threshold_LowEnd, Threshold_HighEnd)��<Replacement_Vals = (Replacement_LowEnd, Replacement_HighEnd)��# Read Images and Resize��aaa = np.array([])��A = None��B = None��if Image_1_Path is not None:��     A = cv2.imread(Image_1_Path)��P    A = cv2.resize(cv2.cvtColor(A, cv2.COLOR_BGR2RGB), (imgSize[0], imgSize[1]))��else:��A    A = cv2.resize(np.zeros((1, 1, 3)), (imgSize[0], imgSize[1]))��if Image_2_Path is not None:��     B = cv2.imread(Image_2_Path)��P    B = cv2.resize(cv2.cvtColor(B, cv2.COLOR_BGR2RGB), (imgSize[0], imgSize[1]))��else:��A    B = cv2.resize(np.zeros((1, 1, 3)), (imgSize[0], imgSize[1]))��# Perform Chosen Operation��Output = None��if Operation == ImageThreshold:��6    Output = Operation(A, Threshold, Replacement_Vals)��else:��    Output = Operation(A, B)��)Output = np.array(Output, dtype=np.uint8)��# Save Output��if savePath is not None:��=    cv2.imwrite(os.path.join(savePath, "Output.png"), Output)��# Display Outputs��print("Plotting Results")��plt.subplot(1, 3, 1)��plt.imshow(A)��plt.subplot(1, 3, 2)��plt.imshow(B)��plt.subplot(1, 3, 3)��plt.imshow(Output)��
plt.show()�hZeub.