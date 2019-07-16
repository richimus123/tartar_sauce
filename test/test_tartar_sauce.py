"""Unit tests for tartar_sauce."""

from typing import Callable

import os

import pytest
import ujson

import tartar_sauce

BASE_DIR = os.path.dirname(__file__)
ARCHIVE_FILE = os.path.join(BASE_DIR, 'test_archive.tar.gz')
with open(os.path.join(BASE_DIR, 'test_cases.json'), 'rb') as handle:
    TEST_CASES = ujson.load(handle)


def _run_test_case(test_case: dict, function: Callable) -> None:
    """Helper to run a test case."""
    args = test_case.get('args', [])
    kwargs = test_case.get('kwargs', {})
    raises = test_case.get('raises')
    if raises:
        with pytest.raises(raises):
            function(*args, **kwargs)
    else:
        result = list(function(*args, **kwargs))
        expected = test_case.get('expected_result')
        assert result == expected


@pytest.mark.parametrize('test_case', TEST_CASES)
def test_read_archive(test_case):
    """Test tartar_sauce.read_archive."""
    test_case['kwargs']['filename'] = ARCHIVE_FILE
    _run_test_case(test_case, tartar_sauce.read_archive)
