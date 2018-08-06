import sys
import pytest
# pytest.mark.xfail equivalent to unittest.expectedFailure(), with optional conditional argument


def test_simple_skip():
    if sys.platform != 'fakeos':
        pytest.skip('Test works only on fakeOS')

    fakeos.fake_action()
    assert fakeos.did_not_happen


@pytest.mark.skipif('sys.version_info <= (3, 0)')
def test_python3():
    assert b'hello'.decode() == 'hello'
