import face_recognition
import cv2

# Load known image (face to be recognized)
known_image = face_recognition.load_image_file("1.jpg")
known_face_encoding = face_recognition.face_encodings(known_image)[0]

# Test image with potential face for recognition
test_image = face_recognition.load_image_file("2.jpg")

# Find faces in the test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Compare known face encoding with each detected face in the test image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
  # Compare encodings with a tolerance of 0.4 (higher is less strict)
  matches = face_recognition.compare_faces([known_face_encoding], face_encoding, tolerance=0.4)

  if matches[0]:
    name = "Known Face"  # replace with actual name if known
    # Draw a box around the face
    cv2.rectangle(test_image, (left, top), (right, bottom), (0, 0, 255), 2)
    # Add a label
    cv2.rectangle(test_image, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(test_image, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

# Display the results
cv2.imshow('Image', test_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
