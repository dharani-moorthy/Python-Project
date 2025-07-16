import cv2
def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Acess to Camera")
        return
    while True:
        ret,frame = cap.read()
        if not ret :
            print("The frame is not visible")
            break
        cv2.imshow('Webcam', frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Grayscale', gray)
        if cv2.waitKey(1) & 0xFF == ord('d'):
            break
    cap.release()
    cv2.destroyAllWindows()
    print("successfully done.....")
if __name__ == "__main__":
    main()