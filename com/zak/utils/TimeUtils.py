class TimeUtils:

    # 把秒数转换为mm:ss格式的时间
    @staticmethod
    def second2minute(second: int):  # 定义方法
        second = int(second)
        if second <= 0:
            return "00:00"
        m = int(second / 60)
        s = second - m * 60
        if m < 10:
            m = '0' + str(m)
        if s < 10:
            s = '0' + str(s)
        return str(m) + ":" + str(s)
