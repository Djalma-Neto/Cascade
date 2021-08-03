import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0) # cria uma conexão com a web cam, o número 0 significa que estou usando a camera zero (câmera nativa do notebook)

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

reconhecimento_maos = mp.solutions.hands #inicializando mediapipe - solution hands: Reconhecimento de mãos
desenho_mp = mp.solutions.drawing_utils
maos = reconhecimento_maos.Hands()

IMAGE_FILES = []

with mp_face_detection.FaceDetection(
    model_selection=1, min_detection_confidence=0.5) as face_detection:
  for idx, file in enumerate(IMAGE_FILES):
    image = cv2.imread(file)
    # Convert the BGR image to RGB and process it with MediaPipe Face Detection.
    results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Draw face detections of each face.
    if not results.detections:
        continue
    annotated_image = image.copy()
    for detection in results.detections:
        print('Nose tip:')
        print(mp_face_detection.get_key_point(
            detection, mp_face_detection.FaceKeyPoint.NOSE_TIP))
        mp_drawing.draw_detection(annotated_image, detection)
    cv2.imwrite('/tmp/annotated_image' + str(idx) + '.png', annotated_image)

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
  while webcam.isOpened():
    success, image = webcam.read()
    image = cv2.flip(image, 180)
    frameRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image.flags.writeable = False
    results = face_detection.process(frameRGB)
    lista_maos = maos.process(frameRGB)

    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue
    
    if lista_maos.multi_hand_landmarks:
        for mao in lista_maos.multi_hand_landmarks:
            print(mao.landmark)
            desenho_mp.draw_landmarks(image, mao, reconhecimento_maos.HAND_CONNECTIONS)
    if results.detections:
      for detection in results.detections:
        mp_drawing.draw_detection(image, detection)
    cv2.imshow('MediaPipe Face Detection', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break         
        
webcam.release() # Fecha a webcam