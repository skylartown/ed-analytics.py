from context import pytest
import types

from ed_analytics.github import Commit, Repository


class TestRepository:
    def test_get_commits(self):
        cmts = Repository("skylartown", "ed-analytics.py") \
            .get_commits(
                author="singhpiyush998",
                since="2022-06-04T10:09:04Z",
                until="2022-06-04T10:09:06Z",
        )

        assert isinstance(
            cmts, types.GeneratorType), "Expect Generator type output"

        for cmt_page in cmts:
            assert any(isinstance(_, Commit)
                    for _ in cmt_page), "Expect Sequence of Commit objects"

            assert len(cmt_page) == 1, "Invalid Output Result"

            assert cmt_page[0].sha == "f6f93444cf182802801dbcde395beeb573ca46c8", "Invalid Output Result"
