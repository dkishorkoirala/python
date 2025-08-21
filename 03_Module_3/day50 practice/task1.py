class Camera:
    def click(self):
        print("Taking a photo...")


class SmartCamera(Camera):
    def click(self):
        super().click()
        print("Applying AI filters...")


camera = SmartCamera()
camera.click()
