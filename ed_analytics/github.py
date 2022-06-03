
from typing import Sequence
from ed_analytics.abc import Commit


class Repository:
    def __init__(self, owner: str, reponame: str) -> None:
        self.owner: str = owner
        self.reponame: str = reponame
        
        self.__oauth_token: str = None

    def authenticate(self, oauth_token):
        self.__oauth_token: str = oauth_token

    def get_commits(self, author: str = None, since: str = None, per_page: int = None, page: int = None, until: str = None) -> Sequence[Commit]:
        """
        Parameters
        ----------
        author : str
            query parameter of commit author

        since : str
            since timestamp in ISO 8601 format YYYY-MM-DDTHH:MM:SSZ
        
        per_page : int
            number of responses per page

        page : int
            page of output

        until : str
            until timestamp in ISO 8601 format YYYY-MM-DDTHH:MM:SSZ

        References
        ----------
        https://docs.github.com/en/rest/commits/commits#list-commits--parameters
        """

        url = "https://api.github.com/repos/{}/{}/commits".format(
            self.owner, self.reponame)

        params = {
            "author": author,
            "since": since,
            "per_page": per_page,
            "page": page,
            "until": until
        }

        for i in params.copy():
            if params[i] is None:
                del params[i]

        r = requests.get(url, params=params, headers={"Authorization": "token {}".format(
            self.__oauth_token)} if self.__oauth_token is not None else {}).json()

        resp = []
        for cmt in r:
            resp.append(Commit(cmt))

        return resp
