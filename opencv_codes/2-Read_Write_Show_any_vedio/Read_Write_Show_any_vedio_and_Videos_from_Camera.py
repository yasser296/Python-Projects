import cv2

cap = cv2.VideoCapture("line_follower_3_sensors.mp4")

while (cap.isOpened()):
	_, frame = cap.read()
	# gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

	# cv2.imshow('frame165' , gray)
	cv2.imshow('frame165' , frame)


	if cv2.waitKey(1) & 0XFF == ord('q') :
		break

cap.release()
cv2.destroyAllWindows()



############################################################################################
################################################################################
###################################################################


# import cv2

# cap = cv2.VideoCapture(0) ;
# print(cap.isOpened())
# while (cap.isOpened()):
# 	ret , frame = cap.read()

# 	gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
# 	cv2.imshow('frame165' , gray)

# 	if cv2.waitKey(1) & 0XFF == ord('q') :
# 		break

# cap.release()
# cv2.destroyAllWindows()







####################################################################
#######################################################################
##########################################################################





# import cv2
# import time


# cap = cv2.VideoCapture(0) ;
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out_put = cv2.VideoWriter('output.avi' , fourcc , 20.0 , (640,480))
# out_put2 = cv2.VideoWriter('output2.avi' , fourcc , 20.0 , (640,480))


# print(cap.isOpened())
# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


# while (cap.isOpened()):
# 	ret , frame = cap.read()
# 	if ret == True:
# 		print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# 		print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# 		print("........")

# 		out_put.write(frame)

# 		gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
# 		cv2.imshow('frame165' , gray)
# 		out_put2.write(frame)

# 		if cv2.waitKey(1) & 0XFF == ord('q') :
# 			break
# 	else:
# 		break

# cap.release()
# out_put.release()
# out_put2.release()
# cv2.destroyAllWindows()
