class string_with_title(str):

    """
    Custom string with title() method

    Based on code from
    https://ionelmc.wordpress.com/2011/06/24/custom-app-names
    """

    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance

    def title(self):
        return self._title

    def __copy__(self):
        return self

    def __deepcopy__(self, memodict):
        return self
