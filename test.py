import litecam
import time
camera_names = litecam.getDeviceList()
print(camera_names)

camera = litecam.PyCamera()

if camera.open(0):
    print("Camera is opened")

    mediaTypes = camera.listMediaTypes()
    print(mediaTypes)

    for i in range(3):
        frame = camera.captureFrame()
        if frame is not None:
            width = frame[0]
            height = frame[1]
            size = frame[2]
            data = frame[3]
            filename = str(i) + ".jpg"
            litecam.saveJpeg(filename, width, height, data)

        time.sleep(1)

    window = litecam.PyWindow(
        camera.getWidth(), camera.getHeight(), "Camera Stream")

    while window.waitKey('q'):
        frame = camera.captureFrame()
        if frame is not None:
            width = frame[0]
            height = frame[1]
            size = frame[2]
            data = frame[3]
            window.showFrame(width, height, data)

            contour_points = [(100, 100), (200, 100), (200, 200), (100, 200)]
            window.drawContour(contour_points)

            text = "Hello, World!"
            window.drawText(text, 50, 50, 24, (255, 0, 0))

    camera.release()
