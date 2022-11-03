import apriltag
import cv2


def readCamera():
    detector = apriltag.Detector()
    vc = cv2.VideoCapture(0)
    while vc.isOpened():
        ret, frame = vc.read()
        frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # print(frame.shape)
        result = detector.detect(frame2)
        if len(result) != 0:
            corners = result[0].corners
            print(int(corners[0][0]), int(corners[0][1]))
            cv2.rectangle(frame, (int(corners[0][0]), int(corners[0][1])), (int(corners[2][0]), int(corners[2][1])), (0, 255, 0), 3)
            cv2.imwrite("apriltag2.jpg", frame)
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



if __name__ == "__main__":
    readCamera()