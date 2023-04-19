# Demo by Adrian Rosebrock on implementing multithreading in openCV taken from:
# https://pyimagesearch.com/2015/12/21/increasing-webcam-fps-with-python-and-opencv/

# import the necessary packages
from __future__ import print_function
from imutils.video import WebcamVideoStream
from imutils.video import FPS
import argparse
import imutils
import cv2

# created a *threaded* video stream, allow the camera sensor to warmup,
# and start the FPS counter
print("[INFO] sampling THREADED frames from webcam...")
vs = WebcamVideoStream(src=0).start()
fps = FPS().start()


# loop over some frames...this time using the threaded stream
while True:
    # grab the frame from the threaded video stream and resize it
    # to have a maximum width of 400 pixels
    frame = vs.read()
    frame = imutils.resize(frame, width=400)
    # check to see if the frame should be displayed to our screen
    cv2.imshow("Frame", frame)

    # update the FPS counter
    fps.update()

    if cv2.waitKey(1) & 0xff == ord('q'):
        break


# stop the timer and display FPS information
fps.stop()
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()