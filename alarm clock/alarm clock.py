from datetime import datetime
from playsound import playsound



def validate_time(alarm_time):
  if len(alarm_time) != 11:
    return "Invalid time format! Please try again..."
  else:
    if int(alarm_time[0:2]) > 12:
      return "Invalid Hour format. please try again..."
    elif int(alarm_time[3:5]) > 59:
      return "invalid menuite format. please try again..."
    elif int(alarm_time[6:8]) > 59:
      return "invalid secend format. please try again..."

    else:
      return "ok"
    



while True:
  alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")
  validate = validate_time(alarm_time.lower())
  if validate == "ok":
    print(f"valid this time : {alarm_time}")
    break
  else:
    print("try again")

h_alert = alarm_time[0:2]
m_alert = alarm_time[3:5]
s_alert = alarm_time[6:8]
alarm_period  = alarm_time[9:].upper()




while True:
  now = datetime.now()
  current_hour = now.strftime("%I")
  current_min = now.strftime("%M")
  current_sec = now.strftime("%S")
  current_period = now.strftime("%p")
  


  if h_alert == current_hour:
    if m_alert == current_min:
      if current_sec == s_alert:
        if alarm_period == current_period:
          print("wake up!")
          playsound('/content/pelican-sound1.mp3')