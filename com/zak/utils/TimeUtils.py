class TimeUtils:

    @staticmethod
    def second2minute(second):
        m = int(second / 60)
        s = second - m * 60
        if m < 10:
            m = '0' + str(m)
        if s < 10:
            s = '0' + str(s)
        return str(m) + ":" + str(s)
