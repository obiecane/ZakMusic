import os


class MiscUtils:

    @staticmethod
    def root_path():
        root_path = os.path.abspath(os.path.dirname(__file__)).split('com')[0]
        return "%s/ZakMusic/" % root_path



if __name__ == "__main__":
    print(MiscUtils.root_path())
