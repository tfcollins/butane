from clock import clock


class _prop:
    def __init__(self, name, default, min, max, step):
        self._min = min
        self._max = max
        self._step = step
        self._val = default
        self._name = name

    def __get__(self, instance, owner):
        return self._val

    def __set__(self, instance, value):
        if self._min > value or self._max < value:
            raise Exception(
                "{} must be {}<={}<={}".format(
                    self._name, self._min, self._name, self._max
                )
            )
        self._value = value


class hmc7044(clock):

    pre_scaler_min = 1
    pre_scaler_max = 255

    vcxo_scaler_min = 1
    vcxo_scaler_max = 255
    
    r1_divider_min = 1
    r1_divider_max = 65535

    n1_divider_min = 1
    n1_divider_max = 65535

    r2_divider_min = 1
    r2_divider_max = 4095

    n2_divider_min = 1
    n2_divider_max = 4095

    osc_divider_options = [1,2,4,8]

    def __init__(self):

        name = "in0_prescaler"
        setattr(
            type(self),
            name,
            _prop(name, 1, self.pre_scaler_min, self.pre_scaler_max, 1),
        )

c = hmc7044()