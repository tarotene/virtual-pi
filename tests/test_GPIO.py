import unittest

try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    import VPi.GPIO as GPIO


class TestGPIO(unittest.TestCase):
    def test_setmode_BCM(self):
        GPIO.setmode(GPIO.BCM)
        self.assertEqual(GPIO.getmode(), GPIO.BCM)

    def test_setmode_BOARD(self):
        GPIO.setmode(GPIO.BOARD)
        self.assertEqual(GPIO.getmode(), GPIO.BOARD)

    def test_setup_IN(self):
        GPIO.setup(15, GPIO.IN)
        self.assertEqual(GPIO.gpio_function(15), GPIO.IN)

    def test_setup_OUT(self):
        GPIO.setup(15, GPIO.OUT)
        self.assertEqual(GPIO.gpio_function(15), GPIO.OUT)

    def test_output_HIGH(self):
        GPIO.setup(15, GPIO.OUT)
        GPIO.output(15, GPIO.HIGH)
        self.assertEqual(GPIO.input(15), GPIO.HIGH)

    def test_output_LOW(self):
        GPIO.setup(15, GPIO.OUT)
        GPIO.output(15, GPIO.LOW)
        self.assertEqual(GPIO.input(15), GPIO.LOW)


if __name__ == '__main__':
    unittest.main()
