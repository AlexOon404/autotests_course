import pytest
from datetime import datetime

@pytest.fixture(scope='class', autouse=True)
def time_start_end():
    start = datetime.now()
    print("\n\nТестирование началось", start.time(), "\n")
    yield
    end = datetime.now()
    print("\n\nТестирование Завершилось", end.time())

@pytest.fixture()
def time_work():
    start = datetime.now()
    yield
    end = datetime.now()
    result = end - start
    print("\n\nТесту потребовалось", result)
