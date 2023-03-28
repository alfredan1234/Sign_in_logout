import pytest


class TestDemo:
    def test_a(self):
        print("a")

    def test_b(self):
        print("b")

    def test_c(self):
        print("c")


if __name__ == "__main__":
    pytest.main(['pytest_1.py'])
