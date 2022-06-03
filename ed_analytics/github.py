
from typing import Sequence
import requests

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

        params = {
            "author": author,
            "since": since,
            "per_page": per_page,
            "until": until
        }

        for i in range(*(
                (1, 10+1) if page is None 
                else (page, page+1)
            )):

            params["page"] = i
            
            rq = requests.get(
                    "https://api.github.com/repos/{}/{}/commits".format(self.owner, self.reponame),
                    params={
                        k: v
                        for k, v in params.items() if v is not None
                    },
                    headers={"Authorization": f"token {self.__oauth_token}"} if self.__oauth_token else None
                )

            if not rq.json():
                return

            yield [Commit(cmt) for cmt in rq.json()]
