'''
Создать класс TrafficLight (светофор)
 и определить у него один атрибут color (цвет) и метод running (запуск).
  Атрибут реализовать как приватный.
   В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
    Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
    третьего (зеленый) — на ваше усмотрение.
    Переключение между режимами должно осуществляться только в указанном порядке
    (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
выводить соответствующее сообщение и завершать скрипт.
'''
import time


class TrafficLight:
    __color = 'red'
    __start_time = int(time.time())

    def running(self):
        delta = int(time.time()) - self.__start_time
        mod = delta % 19
        if 0 <= mod <= 6:
            self.__color = 'red'
        elif 7 <= mod <= 8:
            self.__color = 'yellow'
        else:
            self.__color = 'green'


    def get_color(self):
        self.running()
        print(self.__color)


traffic_light = TrafficLight()
traffic_light.get_color()

time.sleep(7)
traffic_light.get_color()

time.sleep(2)
traffic_light.get_color()

time.sleep(10)
traffic_light.get_color()

for i in range(100):
    traffic_light.get_color()
    time.sleep(1)


