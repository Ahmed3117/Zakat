def getCannyFrame( frame):
    gray = cv2.cvtColor(frame, cv2.IMREAD_GRAYSCALE)
    gray = cv2.GaussianBlur(gray, (3, 3), 0) # change 3,3 to 5,5
    frame = cv2.Canny(gray, 100, 200) # change 100, 200 to 75, 200
    return frame

''' 
The cv2.Canny function takes several arguments, including the input image and two threshold values.
 The threshold values control the sensitivity of the edge detection and can be adjusted
to achieve the desired result.

A common approach to choosing the threshold values is to use a ratio of 2:1 or 3:1 between the
 upper and lower thresholds. For example,
 if you set the upper threshold to 150, you could set the lower threshold to 75 or 50
 '''

also try this :
 
 def getCannyFrame( frame):
    gray = cv2.cvtColor(frame, cv2.IMREAD_GRAYSCALE)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)  # change 3,3 to 5,5
    v = np.median(np.abs(np.gradient(gray)))

    # Determine the lower and upper thresholds based on the median
    lower = int(max(0, (1.0 - 0.33) * v))
    upper = int(min(255, (1.0 + 0.33) * v))
    frame = cv2.Canny(gray, lower, upper)
    return frame
 -------------------------------------------------------------------------------------
try to comment this line :

input_image.resize((794, 1123), resample=Image.BICUBIC)

-----------------------------------------------------------------------------------
try to change values ( 51, 1) in this line : 
adaptiveFrame = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 51, 1)

---------------------------------------------------------------------------------
try this function :
also try ADAPTIVE_THRESH_MEAN_C , also try changing values( 51, 1)
def getAdaptiveThresh( frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    _, adaptiveFrame = cv2.threshold(frame, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # adaptiveFrame = cv2.threshold(frame, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    # adaptiveFrame = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 51, 0)
    # adaptiveFrame = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 51, 1)
    return adaptiveFrame

------------------------------------------

العب فى قيم السطر ده : 

 if len(approx) == 4 and aspect_ratio >= 0.7 and aspect_ratio <= 1.2:

والسطر ده

if (len(approx) > 10 and w / h <= 1.2 and w / h >= 0.7):
---------------------------------------------------