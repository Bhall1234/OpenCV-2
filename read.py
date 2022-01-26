import cv2
import sys

# https://www.youtube.com/watch?v=oXlwWbU8l2o

# Reading Images

# Takes a path to an image and returns image as matrix of pixels.
#img = cv.imread('Photos/board.png') 

# Converting to grayscale
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

# Blur
#blur = cv.GaussianBlur(img,(3,3), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

# Edge Cascade
#canny = cv.Canny(img, 125, 175)
#cv.imshow('Canny Edges', canny)

# Dilating the image
#dilated = cv.dilate(canny, (7,7), iterations=3)
#cv.imshow('Dilated', dilated)

# Eroding
#eroded = cv.erode(dilated, (7,7), iterations=3)
#cv.imshow('Eroded', eroded)

# Resize
#resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
#cv.imshow('Resized', resized)

# Cropping
#cropped = img[50:200, 200:400]
#cv.imshow('Cropped', cropped)

#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

#canny = cv.Canny(img, 125, 175)
#cv.imshow('Canny Edges', canny)

# Displays image as a new window
#cv.imshow('Board', img)

#cv.waitKey(0)

# Reading Videos

# Webcam is referenced as 0

# This is pre-recorded video  
# Download from https://universityoflincoln-my.sharepoint.com/personal/hcuayahuitl_lincoln_ac_uk/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fhcuayahuitl%5Flincoln%5Fac%5Fuk%2FDocuments%2FTSE2021%2FTeam8
# Put the file in Videos folder!


cascPath = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)
capture = cv2.VideoCapture(0)
# Use while loop and read video frame by frame
# Returns the frame, boolean says if it was succesful or not
while True:
    isTrue, frame = capture.read() # Grab frames
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv.imshow('Video', frame) # Display each frame

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
        #flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(20) & 0xFF == ord('d'): # Break out whileloop 
        break #if letter d is pressed break.

capture.release()
cv2.destroyAllWindows
