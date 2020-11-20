class jesd:
    """ JESD Rate Manager """

    """ M: Number of virtual converters """
    M_min = 1
    M_max = 8
    M_possible = [1, 2, 4, 8, 16, 32]
    _M = 1

    """ L: Lanes per link """
    L_min = 1
    L_max = 8
    L_possible = [1, 2, 4, 8]
    _L = 1

    """ F: Octets per frame per link """
    F_min = 1
    F_max = 16
    F_possible = [1, 2, 4, 8, 16]
    _F = 1

    """ N: Number of non-dummy bits per sample """
    N_min = 12
    N_max = 16
    N_possible = range(12, 16)
    _N = 12

    """ Np: Number of bits per sample """
    Np_min = 12
    Np_max = 16
    Np_possible = range(12, 16)
    _Np = 16

    """ K: Frame per multiframe """
    K_min = 4
    K_max = 32
    K_possible = [4, 8, 12, 16, 20, 24, 28, 32]
    _K = 4

    """ R: <FIXME> must be integer"""
    _R = 1

    """ D: <FIXME> must be integer"""
    _D = 1

    """ S: <FIXME> must be integer"""
    _S = 1

    """ C: Interpolator or decimation factor must be integer"""
    _C = 1

    allowed_encodings = ["8b10b", "64b66b"]
    encodings_n = {"8b10b": 8, "64b66b": 64}
    encodings_d = {"8b10b": 10, "64b66b": 66}
    _encoding = "8b10b"

    _sample_rate = 122.88e6

    _sysref_clock = 100e6

    """ bits
        Usually:
            32 for JESD204B 
            64 for JESD204C
    """
    _data_path_width = 32

    def __init__(self):
        pass

    @property
    def encoding(self):
        return self._encoding

    @encoding.setter
    def encoding(self, value):
        if value not in self.allowed_encodings:
            raise Exception("Must be {}".format(",".join(self.allowed_encodings)))
        self._encoding = value

    @property
    def encoding_d(self):
        return self.encodings_d[self._encoding]

    @property
    def encoding_n(self):
        return self.encodings_n[self._encoding]

    @property
    def lane_rate(self):
        return (
            self._sample_rate
            * self.M
            * self.Np
            * self.encoding_d
            / (self.L * self.encoding_n)
        )

    @property
    def lmfc_rate(self):
        return self.lane_rate / (self.encoding_d * self.F * self.K)

    @property
    def device_rate(self):
        return self.lane_rate / (
            self.data_path_width * self.encoding_d / self.encoding_n
        )

    ## Everything is based off sysref clock

    ############################## SCALERS

    @property
    def data_path_width(self):
        return self._data_path_width

    @data_path_width.setter
    def data_path_width(self, value):
        if int(value) != value:
            raise Exception("data_path_width must be an integer")
        self._data_path_width = value

    @property
    def K(self):
        return self._K

    @K.setter
    def K(self, value):
        if int(value) != value:
            raise Exception("K must be an integer")
        self._K = value

    @property
    def R(self):
        return self._R

    @R.setter
    def R(self, value):
        if int(value) != value:
            raise Exception("R must be an integer")
        self._R = value

    @property
    def D(self):
        return self._D

    @D.setter
    def D(self, value):
        if int(value) != value:
            raise Exception("D must be an integer")
        self._D = value

    @property
    def S(self):
        return self._S

    @S.setter
    def S(self, value):
        if int(value) != value:
            raise Exception("S must be an integer")
        self._S = value

    @property
    def C(self):
        return self._C

    @C.setter
    def C(self, value):
        if int(value) != value:
            raise Exception("C must be an integer")
        self._C = value

    @property
    def F(self):
        return self._F

    @F.setter
    def F(self, value):
        if int(value) != value:
            raise Exception("F must be an integer")
        self._F = value

    @property
    def L(self):
        return self._L

    @L.setter
    def L(self, value):
        if int(value) != value:
            raise Exception("L must be an integer")
        self._L = value

    @property
    def M(self):
        return self._M

    @M.setter
    def M(self, value):
        if int(value) != value:
            raise Exception("M must be an integer")
        self._M = value

    @property
    def N(self):
        return self._N

    @N.setter
    def N(self, value):
        if int(value) != value:
            raise Exception("N must be an integer")
        self._M = value

    @property
    def Np(self):
        return self._Np

    @Np.setter
    def Np(self, value):
        if int(value) != value:
            raise Exception("Np must be an integer")
        self._Np = value

    ########### CLOCKS
    @property
    def sysref_clock(self):
        return self._sysref_clock

    @sysref_clock.setter
    def sysref_clock(self, value):
        pass

    @property
    def multiframe_clock(self):
        return self.sysref_clock * self.R

    @multiframe_clock.setter
    def multiframe_clock(self, value):
        pass

    @property
    def device_clock(self):
        return self.multiframe_clock * self.D

    @device_clock.setter
    def device_clock(self, value):
        pass

    @property
    def frame_clock(self):
        return self.multiframe_clock * self.K

    @frame_clock.setter
    def frame_clock(self, value):
        pass

    @property
    def character_clock(self):
        return self.frame_clock * self.F

    @character_clock.setter
    def character_clock(self, value):
        pass

    @property
    def bit_clock(self):
        return self.character_clock * 10

    @bit_clock.setter
    def bit_clock(self, value):
        pass

    @property
    def sample_clock(self):
        return self.frame_clock * self.S

    @sample_clock.setter
    def sample_clock(self, value):
        pass

    @property
    def conversion_clock(self):
        return self.sample_clock * self.C

    @conversion_clock.setter
    def conversion_clock(self, value):
        pass

    def print_clocks(self):
        for p in dir(self):
            if p != "print_clocks":
                if "clock" in p and p[0] != "_":
                    print(p, getattr(self, p))
                if "rate" in p and p[0] != "_":
                    print(p, getattr(self, p))


# j = jesd()
# j.M = 8
# j.L = 4
# j.Np = 16
# j.F = 4
# j.K = 32
# j.sample_rate = 250e6
