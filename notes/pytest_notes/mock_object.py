from unittest.mock import Mock, patch
import datetime
import pytest

from flight_tracker import FlightStatusTracker


@pytest.fixture
def tracker():
    return FlightStatusTracker()


def test_mock_method(tracker):
    tracker.redis.set = Mock()
    with pytest.raises(ValueError) as ex:
        tracker.change_status('AC101', 'lost')
    assert ex.value.args[0] == 'LOST is not a valid status'
    assert tracker.redis.set.call_count == 0


def test_patch(tracker):
    tracker.redis.set = Mock()
    fake_now = datetime.datetime(2018, 8, 5)
    with patch('datetime.datetime') as dt:
        dt.now.return_value = fake_now
        tracker.change_status('AC102', 'on time')
    dt.now.assert_called_once_with()
    tracker.redis.set.assert_called_once_with(
        'flightno:AC102',
        '2018-08-05T00:00:00|ON TIME'
    )

# however the need to mock a module in unit tests often is a signal to rethink the design
# in this case instead of initiate a redis instance in FlightStatusTracker.__init__
# is better changed to allow user to pass in a redis instance,
# so that user can reuse redis elsewhere, or use their own customized redis API implementation

# def __init__(self, redis_instance=None):
#     self.redis = redis_instance if redis_instance else redis.StrictRedis()
