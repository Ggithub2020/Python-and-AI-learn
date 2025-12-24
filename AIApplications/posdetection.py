import cv2
import mediapipe as mp

# 1. Initialize MediaPipe Pose
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

#2. start capturing video from the webcam
cap = cv2.VideoCapture(0)

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 3. Flip the frame horizontally for a later selfie-view display
        frame = cv2.flip(frame, 1)

        # 4. Convert the BGR image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # 5. Process the image and find the pose landmarks
        results = pose.process(image)

        # 6. Draw the pose landmarks on the image
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # 7. Display the resulting frame
        cv2.imshow('Pose Detection', image)

        if cv2.waitKey(5) & 0xFF == 27:  # Press 'ESC' to exit
            break
    # 8. Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()