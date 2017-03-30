import os
import time

OUTPUT = 'out'
INPUT = 'in'
HIGH = 1
LOW = 0

class BBB_GPIO:
    def __init__(self, pin):
        """ rajouter conversion de nom de pin en numero"""
        self.pin = pin
        self.create = self.__create()
        self.path_gpio = '/sys/class/gpio/'


    def __open(self, files):
        try:
            with open('{0}/gpio{1}/{2}'.format(self.path_gpio, self.pin, files), 'wr') as f:
                return f
        except OSError as exception:
            print(exception)

    def __create(self):
        os.chdir(self.path_gpio)
        return os.system('echo {0} > export'.format(self.pin))

    def remove(self):
        os.chdir(self.path_gpio)
        return os.system('echo {0} > unexport'.format(self.pin))

    def direction(self, direction):
        f = self.__open('direction')
        f.write(direction)
        return f.close()

    def value(self, value):
        f = self.__open('value')
        f.write(value)
        return f.close()

if __name__ == '__main__':
    BBB_GPIO44 = BBB_GPIO(44)
    BBB_GPIO44.direction(OUTPUT).value(HIGH)
    time.sleep(5)
    BBB_GPIO44.remove()
