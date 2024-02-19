import unittest
from business_logic import create_groups

test_names = ["aa", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]


class CreateGroupsTests(unittest.TestCase):
    def test_should_fail(self):
        self.assertIsNone(create_groups(test_names, 12))

    def test_should_suceed(self):
        n = 4
        groups = create_groups(test_names, n)

        self.assertIsNotNone(groups)

        # we check that final content is consistent
        self.assertCountEqual(
            [item for group in groups for item in group], test_names
        )

        # we check that the groups are the right size
        min_group_size = len(test_names) // n
        for group in groups:
            group_length = len(group)
            self.assertTrue(
                group_length == min_group_size
                or group_length == min_group_size + 1
            )


if __name__ == "__main__":
    unittest.main()
