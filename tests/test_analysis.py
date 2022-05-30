

class A:
    def __init__(self, owner, reponame):
        self.owner = owner
        self.reponame = reponame

    @property
    def httpURL(self):
        return f"https://github.com/{self.owner}/{self.reponame}"

    @property
    def apiURL(self):
        return f"https://api.github.com/repos/{self.owner}/{self.reponame}"


a = A("shreyass-rangnaatha", "quirky-algorihtms")
a.owner = "something"
print(a.httpURL, a.apiURL)
