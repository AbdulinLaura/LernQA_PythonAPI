class Test_example:
    def test_check_math(self):
        a = str(input())
        expected_result = len(a) < 15
        assert expected_result < 15, f"The entered value {expected_result} is greater than 15"