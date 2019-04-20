import re

from com.zak.utils.MiscUtils import MiscUtils


class LrcUtils:
    pattern = re.compile(r'\[\d{,3}:\d{,3}[.:]\d{,3}]')
    ti_pattern = re.compile(r'\[ti:.*]\n')
    ar_pattern = re.compile(r'\[ar:.*]\n')
    al_pattern = re.compile(r'\[al:.*]\n')
    by_pattern = re.compile(r'\[by:.*]\n')
    offset_pattern = re.compile(r'\[offset:.*]\n')

    def __init__(self):
        pass

    @staticmethod
    def read_lrc(style):
        with open(style, 'r', encoding="UTF-8") as f:
            lrc = f.read()
            lrc.replace(r"\[\d\d\:\d\d\.\d\d]", "")
            lrc = re.sub(LrcUtils.pattern, '', lrc)
            lrc = re.sub(LrcUtils.ti_pattern, '', lrc)
            lrc = re.sub(LrcUtils.ar_pattern, '', lrc)
            lrc = re.sub(LrcUtils.al_pattern, '', lrc)
            lrc = re.sub(LrcUtils.by_pattern, '', lrc)
            lrc = re.sub(LrcUtils.offset_pattern, '', lrc)
            lrc = re.sub(LrcUtils.by_pattern, '', lrc)
            return lrc


if __name__ == "__main__":
    lrc_ = MiscUtils.root_path() + "/download/lrc/Chris Medina/What Are Words.lrc"
    print(lrc_)
    LrcUtils.read_lrc(MiscUtils.root_path() + "/download/lrc/Chris Medina/What Are Words.lrc")
