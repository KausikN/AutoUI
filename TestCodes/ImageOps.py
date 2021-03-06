'''
Function Chooser Program
'''

# Imports
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt



# Main Functions
class Image:
    def __init__(self, path, data=None):
        self.path = path
        self.data = data
#CEND

def ImageAdd(a, b):
    if a is None or b is None:
        return None
    return a + b
#FEND

def ImageAvg(a, b):
    if a is None or b is None:
        return None
    return (a + b) / 2
#FEND

def ImageThreshold(a, threshold, replacementVal=[0, 255]):
    if a is None or threshold is None:
        return None
    A = np.copy(a)
    A[np.nonzero(a < threshold[0])] = replacementVal[0]
    A[np.nonzero(a > threshold[1])] = replacementVal[1]
    return A
#FEND

# Driver Code
# Params
Image_1_Path = '' #TYPE: FILE Image
Image_2_Path = '' #TYPE: FILE Image
savePath = '' #TYPE: DIR

Threshold_LowEnd = 0
Replacement_LowEnd = 0
Threshold_HighEnd = 255
Replacement_HighEnd = 255

Operation = None #TYPE: SELECTVAL NOTYPE ImageAdd,ImageAvg,ImageThreshold
# Params
imgSize = (100, 100, 3)

print("Started Image Ops")

Threshold = (Threshold_LowEnd, Threshold_HighEnd)
Replacement_Vals = (Replacement_LowEnd, Replacement_HighEnd)

# Read Images and Resize
aaa = np.array([])
A = None
B = None
if Image_1_Path is not None:
    A = cv2.imread(Image_1_Path)
    A = cv2.resize(cv2.cvtColor(A, cv2.COLOR_BGR2RGB), (imgSize[0], imgSize[1]))
else:
    A = cv2.resize(np.zeros((1, 1, 3)), (imgSize[0], imgSize[1]))
if Image_2_Path is not None:
    B = cv2.imread(Image_2_Path)
    B = cv2.resize(cv2.cvtColor(B, cv2.COLOR_BGR2RGB), (imgSize[0], imgSize[1]))
else:
    B = cv2.resize(np.zeros((1, 1, 3)), (imgSize[0], imgSize[1]))

# Perform Chosen Operation
Output = None
if Operation == ImageThreshold:
    Output = Operation(A, Threshold, Replacement_Vals)
else:
    Output = Operation(A, B)
Output = np.array(Output, dtype=np.uint8)

# Save Output
if savePath is not None:
    cv2.imwrite(os.path.join(savePath, "Output.png"), Output)

# Display Outputs
print("Plotting Results")
plt.subplot(1, 3, 1)
plt.imshow(A)
plt.subplot(1, 3, 2)
plt.imshow(B)
plt.subplot(1, 3, 3)
plt.imshow(Output)
plt.show()

print("Ended Image Ops")