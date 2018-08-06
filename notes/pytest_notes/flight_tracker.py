import datetime
import redis


class FlightStatusTracker:
    ALLOWED_STATUSES = {'CANCELLED', 'DELAYED', 'ON TIME'}

    def __init__(self):
        self.redis = redis.StrictRedis()
    # however the need to mock a module in unit tests often is a signal to rethink the design
    # in this case instead of initiate a redis instance in FlightStatusTracker.__init__
    # is better changed to allow user to pass in a redis instance,
    # so that user can reuse redis elsewhere, or use their own customized redis API implementation

    # def __init__(self, redis_instance=None):
    #     self.redis = redis_instance if redis_instance else redis.StrictRedis()

    def change_status(self, flight, status):
        status = status.upper()
        if status not in self.ALLOWED_STATUSES:
            raise ValueError('{} is not a valid status'.format(status))
        key = 'flightno:{}'.format(flight)
        value = '{}|{}'.format(datetime.datetime.now().isoformat(), status)
        self.redis.set(key, value)
