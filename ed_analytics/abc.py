

class Commit(dict):
    """
    Attributes
    ----------
    sha : str
        SHA of the commit

    timestamp : datetime.datetime
        Timestamp of the commit

    author : dict
        The author dictionary in the commit

    author_github_username : str
        GitHub username of the author

    htmlURL : str
        HTML URL of the commit
    """


class Submission:
    """Class to contain individual assignment submission operations"""

    def __init__(self, **kw) -> None:
        self.kw = kw
