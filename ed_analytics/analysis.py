"""

P.S. Srinivasan Sir's Notes
----------------------
What will class method return.
it returns a customized class.
x = classAssignment()

class methods of class will return a object of Classroom Assignment.
__init__ - returns object of the class

Object frominit has submissions as a dictionary python object.
Object from_assignment_grade 
"""

import csv
from typing import Dict

from ed_analytics.abc import Submission


class ClassroomAssignment:
    def __init__(self, submissions: Dict[str, Submission]) -> None:
        self.submissions = submissions

    @classmethod
    def from_assignment_grades(cls, path: str):
        with open(path, encoding="utf8") as file:
            redr = csv.DictReader(file)

            # next(redr)  # ignore heading row

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

