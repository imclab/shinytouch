class Graphics:
    def draw_mode(self, image, mode):
        """ Draws the mode Text """
        font = cvInitFont(CV_FONT_HERSHEY_SIMPLEX,0.75,0.75,0,2,CV_AA)
        cvPutText(image, mode, cvPoint(5,25), font, cvScalar(255, 0, 0))
        return image

    def drawquad(self, frame):
        """ Draws the quad around the screen """
        global warp_points

        tl=cvPoint(warp_points[0][0], warp_points[0][1])
        tr=cvPoint(warp_points[1][0], warp_points[1][1])
        br=cvPoint(warp_points[2][0], warp_points[2][1])
        bl=cvPoint(warp_points[3][0], warp_points[3][1])

        red=CV_RGB(250,0,0)

        cvLine(frame,tl,tr,red,1,CV_AA)
        cvLine(frame,tr,br,red,1,CV_AA)
        cvLine(frame,br,bl,red,1,CV_AA)
        cvLine(frame,bl,tl,red,1,CV_AA)

        return frame

    def fps(self, frame, fps):
        """ Draws the FPS Meter """
        global height
        font = cvInitFont(CV_FONT_HERSHEY_SIMPLEX,0.4,0.4,0,1,CV_AA)
        cvPutText(frame, "FPS: "+str(fps), cvPoint(5,height-10), font, cvScalar(255,255,255))

        return frame
    
    def callibration(self, frame, clicks):
        global width, height
        if clicks == 0:
          point1 = cvPoint(0,0)
          point2 = cvPoint(20,20)
        elif clicks == 1:
          point1 = cvPoint(width - 20, 0)
          point2 = cvPoint(width, 20)
        elif clicks == 2:
          point1 = cvPoint(width - 20, height - 20)
          point2 = cvPoint(width, height)
        elif clicks == 3:
          point1 = cvPoint(0, height-20)
          point2 = cvPoint(20, height)
        cvRectangle(frame, point1, point2, cvScalar(0,255,255), 20)
        return frame
