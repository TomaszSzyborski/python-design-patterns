"""Bank class."""
import random
import string
import time
from dataclasses import dataclass, field

# from banking.account import Account

#
# @dataclass
# class Bank:
#     accounts: dict[str, Account] = field(default_factory=dict)
#
#
#     def create_account(self, name: str) -> Account:
#         number = "".join(random.choices(string.digits, k=12))
#         account = Account(name, number)
#         self.accounts[number] = account
#         return account
#
#     def get_account(self, account_number: str) -> Account:
#
#         return self.accounts[account_number]
#
# class D(dict):
#     def __setattr__(self, __name, __value):
#         if __name not in self:
#             super().__setattr__(__name, __value)
#

class D(dict):
    def __setattr__(self, __name, __value):
        if self.__contains__(__name):
            super().__setattr__(__name, __value)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        compliments = dict()
        for i in range(len(nums)):
            try:
                return [compliments.pop(target - nums[i]), i]
            except KeyError:
                compliments[nums[i]] = i

t1 = time.perf_counter()
e = Solution().twoSum([2,7,11,15], 9)
print(time.perf_counter() - t1)
print(e)
