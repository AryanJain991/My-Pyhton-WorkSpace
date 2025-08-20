import cv2
import mediapipe as mp

# Initialize Mediapipe Holistic model and drawing utilities
mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh  # For face landmarks

# Open webcam
cap = cv2.VideoCapture(0)

# Set up the Holistic model
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        # Read frames from the webcam
        ret, frame = cap.read()
        if not ret:
            print("Frames not found")
            break

        # Convert BGR image to RGB for Mediapipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame using the Holistic model
        results = holistic.process(rgb_frame)

        # Draw landmarks for pose, face, and hands
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
        if results.face_landmarks:
            mp_drawing.draw_landmarks(frame, results.face_landmarks, mp_face_mesh.FACEMESH_TESSELATION)  # Fixed face drawing
        if results.left_hand_landmarks:
            mp_drawing.draw_landmarks(frame, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        if results.right_hand_landmarks:
            mp_drawing.draw_landmarks(frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

        # Display the annotated frame
        cv2.imshow("MediaPipe Holistic Output", frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
