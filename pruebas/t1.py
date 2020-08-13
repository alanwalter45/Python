from unittest import TestCase, main


class EnvironmentTest(TestCase):
    def setUp(self):
        print("inicio")

    def test_suma(self):
        a, b = 5, 5
        self.assertEqual(a+b, 10)
        print(self.test_suma.__name__, a, b)

    def test_resta(self):
        a, b = 20, 20
        self.assertEqual(a-b, 0)
        print(self.test_resta.__name__, a, b)

    def tearDown(self):
        print("luego")


if __name__ == '__main__':
    main()
