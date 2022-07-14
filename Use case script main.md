Sebuah script utama main.py yang terdiri dari sebuah logic sederhana yang menjawab sebuah use case sederhana ( jelaskan use case tersebut dalam MD files! )

#Script main.py dan sebuah fungsi untuk mengambil data dari sensor tersebut

from gpiozero import MotionSensor   # mengambil package import Motion Sensor

pir = MotionSensor(4)   # PIR Sensor yang terhubung dengan GPIO 4

pir.wait_for_motion()     # Sistem akan menunggu gerakan yang datang
print("Motion Detected!")   #Apabila ada gerakan output Motion Detected

while True:
    print("ada maling")     #Apabila hasil True, keluaran menghasilkan ada Maling
    
![pir](https://user-images.githubusercontent.com/105527013/178905847-19a5dc88-501d-4d21-80b4-790149ef2806.jpg)

Penjelasan sistem User dideteksi sistem PIR SENSOR
1. Ada User yang melewati PIR SENSOR
2. Kemudian Pir Sensor Bekerja dengan sistem yang telah dijalankan
3. Sistem dari PIR Sensor Mengeluarkan Output ("Motion Detected!")
4. Gerakan terdeteksi berupa gerakan yang lewat
5. Mengeluarkan pesan tergantung script yang dibuat (Pada script yang dibuat apabila True akan mengeluarkan pesan "Ada Maling")
