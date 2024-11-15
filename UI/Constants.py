class Constants:

    def __setattr__(self, __name: str, __value: any):
        raise AttributeError("Cannot modify Constants")

    def __new__(self, *args, **kwargs):
        raise AttributeError("Cannot create instance of Constants")

    ROOT_TABLE_NAME= "Motors"