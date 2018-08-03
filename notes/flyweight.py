import weakref


class CarModel:
    _models = weakref.WeakValueDictionary()

    def __new__(cls, model_name, *args, **kwargs):
        model = cls._models.get(model_name)
        if not model:
            model = super().__new__(cls)  # 初始化是 type.__call__()执行，不是__new__，所以这里不需要传入其他的参数
            cls._models[model_name] = model
        return model

    def __init__(self, model_name, air=False, tilt=False, cruise_control=False, power_locks=False, alloy_wheels=False, usb_charger=False):
        if not hasattr(self, "initted"):
            self.model_name = model_name
            self.air = air
            self.tilt = tilt
            self.cruise_control = cruise_control
            self.power_locks = power_locks
            self.alloy_wheels = alloy_wheels
            self.usb_charger = usb_charger
            self.initted = True

    def check_serial(self, serial_number):
        print('Sorry, we are unable to check the serial number {} on the {} at this time'.format(serial_number, self.model_name))


class Car:

    def __init__(self, model, color, serial):
        self.model = model
        self.color = color
        self.serial = serial

    def check_serial(self):
        return self.model.check_serial(self.serial)
