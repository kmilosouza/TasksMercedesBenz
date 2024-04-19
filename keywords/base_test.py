import pytest

@pytest.mark.usefixtures("setup_teardown")
class BaseTest:

    def some_method():
        pass