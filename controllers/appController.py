import serial
from unittest import result
from flask import request, render_template

ArduinoUnoSerial = serial.Serial('/dev/cu.usbserial-1420', 9600)

def index():
  args = request.args
  status = "0"
  if(args):
    if args["status"] == "1":
      status = "1"
      ArduinoUnoSerial.write("1".encode())
    else:
      status = "0"
      ArduinoUnoSerial.write("0".encode())

  data = {
    "status": status,
    "biodata": {
      "name": "Setiawan Restu Aji",
      "nim": "119203008",
      "title": "Midterm Exam"
    }
  }
  return render_template("app/index.html", result = data)


