import cv2 
# 1, load the cascade classifier first
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 2, start webcam
cap = cv2.VideoCapture(0)

while True:
        # 3, read the frame from webcam
        ret, frame = cap.read()
        
        if not ret:
            break
        
        # 4, convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # 5, detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        # 6, draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        # 7, display the frame with detected faces
        cv2.imshow('Face Detection', frame)
        
        # 8, break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
# 9, clean up
cap.release()   
cv2.destroyAllWindows()
