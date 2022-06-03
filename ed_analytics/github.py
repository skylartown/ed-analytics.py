#  https://api.github.com/repos/OWNER/REPO/commits
import requests
import json



from typing import Sequence


class Repository:
    def __init__(self, owner: str, reponame: str) -> None:
        self.owner: str = owner
        self.reponame: str = reponame
        
        self.__oauth_token: str = None

    def authenticate(self, oauth_token):
        self.__oauth_token: str = oauth_token

    
    def get_commits(self, author: str = None, since: str = None, per_page: int = None, page: int = None, until: str = None):
        
        
        
        
        url=" https://api.github.com/repos/{}/{}/commits".format(self.owner,self.reponame)

        res={
            'author':author,
            'since':since,
            'per_page':per_page,
            'page':page,
            'until':until
        }

        r=requests.get(url,params={
            h:r
            for h,r in res.items() 
            if r is not None
            }).json()
                    
        return r
