class SmartWatch:
    def walk(self, steps):
        self.steps += steps
        self.battery -= (steps/ 500)
        print(f"You walked {steps} steps.")

    def show_status(self):
        print(f"Brand: {self.brand}\nBattery Percentage: {int(self.battery)}%\nSteps: {self.steps}")


watch1 = SmartWatch()
watch1.brand = "Mi Band"
watch1.battery = 80
watch1.steps = 0

watch1.walk(1000)
watch1.show_status()