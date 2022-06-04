
from textwrap import indent
from typing import Sequence
from ed_analytics.abc import Commit
import requests


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
        repo_dict={
            'author':author,
            'since':since,
            'per_page':per_page,
            'page':page,
            'until':until
        }
        commit_list=[]
        url= requests.get('https://api.github.com/repos/{}/{}/commits'.format(self.owner,self.reponame),params=repo_dict)
        x = url.json()
        for i in x:
            commit_class=Commit(i)
            commit_list.append(commit_class)
        
        return commit_list
