import os
import cv2
import face_recognition
import numpy as np
from tqdm import tqdm
from collections import defaultdict
from imutils.video import VideoStream
from eye_status import * 

def init():
    face_cascPath = 'haarcascade_frontalface_alt.xml'
    # face_cascPath = 'lbpcascade_frontalface.xml'

    open_eye_cascPath = 'haarcascade_eye_tree_eyeglasses.xml'
    left_eye_cascPath = 'haarcascade_lefteye_2splits.xml'
    right_eye_cascPath ='haarcascade_righteye_2splits.xml'
    dataset = 'faces'

    face_detector = cv2.CascadeClassifier(face_cascPath)
    open_eyes_detector = cv2.CascadeClassifier(open_eye_cascPath)
    left_eye_detector = cv2.CascadeClassifier(left_eye_cascPath)
    right_eye_detector = cv2.CascadeClassifier(right_eye_cascPath)

    print("[LOG] Opening webcam ...")
    video_capture = VideoStream(src=1).start()

    model = load_model()


    print("[LOG] Collecting images ...")
    images = []
    for direc, _, files in tqdm(os.walk(dataset)):
        for file in files:
            if file.endswith("jpg"):
                images.append(os.path.join(direc,file))
    return (model,face_detector, open_eyes_detector, left_eye_detector,right_eye_detector, video_capture, images) 

def process_and_encode(images):
    # bilinen kodlamaların ve bilinen adların listesini başlat
    known_encodings = []
    known_names = []
    print("[LOG] Encoding faces ...")

    for image_path in tqdm(images):
        # Resmi yükle
        image = cv2.imread(image_path)
        # BGR'den RGB'ye dönüştürün
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
     
        # görüntüdeki yüzü algıla ve konumunu al (koordinatları kare kutular)
        boxes = face_recognition.face_locations(image, model='hog')

        # Yüzü 128 boyutlu bir katıştırma vektörüne kodlayın
        encoding = face_recognition.face_encodings(image, boxes)

        # kişinin adı, görüntünün geldiği klasörün adıdır
        name = image_path.split(os.path.sep)[-2]

        if len(encoding) > 0 : 
            known_encodings.append(encoding[0])
            known_names.append(name)

    return {"encodings": known_encodings, "names": known_names}

def isBlinking(history, maxFrames):
    """ @history: Göz durumunun geçmişini içeren bir dize
          burada '1', gözlerin kapalı ve '0' açık olduğu anlamına gelir.
         @maxFrames: Bir gözün kapalı olduğu maksimum ardışık kare sayısı """
    for i in range(maxFrames):
        pattern = '1' + '0'*(i+1) + '1'
        if pattern in history:
            return True
    return False

def detect_and_display(model, video_capture, face_detector, open_eyes_detector, left_eye_detector, right_eye_detector, data, eyes_detected):
        frame = video_capture.read()
        # çerçeveyi yeniden boyutlandır
        frame = cv2.resize(frame, (0, 0), fx=0.6, fy=0.6)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Yüzleri algıla
        faces = face_detector.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(50, 50),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # algılanan her yüz için
        for (x,y,w,h) in faces:
            # Yüzü 128 boyutlu bir katıştırma vektörüne kodlayın
            encoding = face_recognition.face_encodings(rgb, [(y, x+w, y+h, x)])[0]

            # Vektörü bilinen tüm yüz kodlamalarıyla karşılaştırın
            matches = face_recognition.compare_faces(data["encodings"], encoding)

            # Şimdilik kişinin adını bilmiyoruz
            name = "Unknown"

            # En az bir eşleşme varsa:
            if True in matches:
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}
                for i in matchedIdxs:
                    name = data["names"][i]
                    counts[name] = counts.get(name, 0) + 1

                # en çok oyu alan tanınan yüzü belirleyin
                name = max(counts, key=counts.get)

            face = frame[y:y+h,x:x+w]
            gray_face = gray[y:y+h,x:x+w]

            eyes = []
            
            # Göz algılama
            # önce gözlerin açık olup olmadığını kontrol edin (gözlük dikkate alınarak)
            open_eyes_glasses = open_eyes_detector.detectMultiScale(
                gray_face,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags = cv2.CASCADE_SCALE_IMAGE
            )
            # open_eyes_glasses gözleri algılarsa açıktırlar 
            if len(open_eyes_glasses) == 2:
                eyes_detected[name]+='1'
                for (ex,ey,ew,eh) in open_eyes_glasses:
                    cv2.rectangle(face,(ex,ey),(ex+ew,ey+eh),(255,255,255),2)
            
            # aksi takdirde, sol ve sağ_eye_detektörü kullanarak gözleri algılamayı deneyin
            # açık ve kapalı gözleri algılayabilen                
            else:
                # yüzü sol ve sağ taraflara ayırın
                left_face = frame[y:y+h, x+int(w/2):x+w]
                left_face_gray = gray[y:y+h, x+int(w/2):x+w]

                right_face = frame[y:y+h, x:x+int(w/2)]
                right_face_gray = gray[y:y+h, x:x+int(w/2)]

                # Sol gözü algıla
                left_eye = left_eye_detector.detectMultiScale(
                    left_face_gray,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30),
                    flags = cv2.CASCADE_SCALE_IMAGE
                )

                # Sağ gözü algıla
                right_eye = right_eye_detector.detectMultiScale(
                    right_face_gray,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30),
                    flags = cv2.CASCADE_SCALE_IMAGE
                )

                eye_status = '1' # gözlerin açık olduğunu varsayalım

                # Her göz için gözün kapalı olup olmadığını kontrol edin.
                # Biri kapalıysa, gözlerin kapalı olduğu sonucuna varırız
                for (ex,ey,ew,eh) in right_eye:
                    color = (0,255,0)
                    pred = predict(right_face[ey:ey+eh,ex:ex+ew],model)
                    if pred == 'closed':
                        eye_status='0'
                        color = (0,0,255)
                    cv2.rectangle(right_face,(ex,ey),(ex+ew,ey+eh),color,2)
                for (ex,ey,ew,eh) in left_eye:
                    color = (0,255,0)
                    pred = predict(left_face[ey:ey+eh,ex:ex+ew],model)
                    if pred == 'closed':
                        eye_status='0'
                        color = (0,0,255)
                    cv2.rectangle(left_face,(ex,ey),(ex+ew,ey+eh),color,2)
                eyes_detected[name] += eye_status

            # Her seferinde kişinin gözünü kırpıp kırpmadığını kontrol ederiz
            # Evet ise adını gösteririz
            if isBlinking(eyes_detected[name],3):
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
                # Ekran adı
                y = y - 15 if y - 15 > 15 else y + 15
                cv2.putText(frame, name, (x, y), cv2.FONT_HERSHEY_SIMPLEX,0.75, (0, 0, 200), 3)

        return frame


if __name__ == "__main__":
    (model, face_detector, open_eyes_detector,left_eye_detector,right_eye_detector, video_capture, images) = init()
    data = process_and_encode(images)

    eyes_detected = defaultdict(str)
    while True:
        frame = detect_and_display(model, video_capture, face_detector, open_eyes_detector,left_eye_detector,right_eye_detector, data, eyes_detected)
        cv2.imshow("Face Liveness Detector", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    video_capture.stop()