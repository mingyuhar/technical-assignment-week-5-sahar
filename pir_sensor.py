from gpiozero import MotionSensor

pir = MotionSensor(4)

pir.wait_for_motion()
print("Motion Detected!")

while True:
    print("ada maling")
