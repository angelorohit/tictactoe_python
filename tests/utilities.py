from functools import wraps
from unittest.mock import patch


def input_cases(cases: dict = None):
    def _decorate(test_func):
        @wraps(test_func)
        @patch('builtins.input', side_effect=cases.keys())
        def wrapper(self, magic_mock, *args, **kwargs):
            for expected_output in cases.values():
                test_func(self, expected_output, *args, **kwargs)
        return wrapper
    return _decorate
