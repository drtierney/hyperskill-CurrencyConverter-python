from typing import List

from hstest.check_result import CheckResult
from hstest.stage_test import StageTest
from hstest.test_case import TestCase


class TestStage3(StageTest):

    def generate(self) -> List[TestCase]:
        list_tests = [
            TestCase(stdin=['13', '2'], attach=26),
            TestCase(stdin=['128', '3.21'], attach=410.88),
            TestCase(stdin=['75', '5.5'], attach=412.5)

        ]

        return list_tests

    def check(self, reply: str, attach) -> CheckResult:
        reply_parsed = [i.strip() for i in reply.split(':')]
        if len(reply_parsed) != 4:
            return CheckResult.wrong("Your output differs from the example")
        if "please, enter the number of conicoins you have" not in reply_parsed[0].lower():
            return CheckResult.wrong("The program should ask for the conicoins input")
        if "please, enter the exchange rate" not in reply_parsed[1].lower():
            return CheckResult.wrong("The program should ask for the exchange rate input")
        if "the total amount of dollars" not in reply_parsed[2].lower():
            return CheckResult.wrong("The program should output the total amount of dollars")
        try:
            dollars_amount = float(reply_parsed[3])
        except ValueError:
            return CheckResult.wrong("It seems that the output format for the amount of dollars is incorrect.")
        if abs(dollars_amount - attach) > 0.2:
            return CheckResult.wrong("The amount of dollars is wrong")
        return CheckResult.correct()


if __name__ == '__main__':
    TestStage3("cconverter.cconverter").run_tests()
