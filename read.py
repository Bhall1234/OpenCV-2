import cv2 as cv

# https://www.youtube.com/watch?v=oXlwWbU8l2o

# Reading Images

# Takes a path to an image and returns image as matrix of pixels.
img = cv.imread('Photos/images.jpg') 

# Displays image as a new window
cv.imshow('Tyler', img)

cv.waitKey(0)

# Reading Videos

# Webcam is referenced as 0

# This is pre-recorded video  
# Download from https://universityoflincoln-my.sharepoint.com/personal/hcuayahuitl_lincoln_ac_uk/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fhcuayahuitl%5Flincoln%5Fac%5Fuk%2FDocuments%2FTSE2021%2FTeam8
# Put the file in Videos folder!
capture = cv.VideoCapture('Videos/test1639658932.91.avi')

# Use while loop and read video frame by frame
# Returns the frame, boolean says if it was succesful or not
while True:
    isTrue, frame = capture.read() # Grab frames
    cv.imshow('Video', frame) # Display each frame

    if cv.waitKey(20) & 0xFF==ord('d'): # Break out whileloop 
        break #if letter d is pressed break.

capture.release()
cv.destroyAllWindows
