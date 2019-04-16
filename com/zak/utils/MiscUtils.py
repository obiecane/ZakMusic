import os


class MiscUtils:

    @staticmethod
    def root_path():
        root_path = os.path.abspath(os.path.dirname(__file__)).split('ZakMusic')[0]
        return "%s/ZakMusic/" % root_path
