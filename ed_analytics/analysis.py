import typing
import csv

from ed_analytics.abc import Submission


class ClassroomAssignment:
    def __init__(self, submissions: typing.Dict[str, Submission]) -> None:
        self.submissions = submissions

    @classmethod
    def from_assignment_grades(cls, path: str):
        with open(path, encoding="utf8") as file:
            redr = csv.DictReader(file)

            return cls(
                submissions={
                    ln["github_username"]: Submission(**ln)
                    for ln in redr
                }
            )

    def __getitem__(self, item):
        """`item` is github_id"""

        if item not in self.submissions:
            raise Exception()  # TODO: Enhance error

        return self.submissions[item]
