import psutil

#  Captura o sensor da bateria
battery = psutil.sensors_battery()

#  Captura o percentual da bateria
percent = str(battery.percent)

#  Mostra resultado
print('###--------------------RESULTADO--------------------###')
print(f'No momento voce tem {percent:.2s}% de bateria!')
