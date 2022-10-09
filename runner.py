from quizzes._1 import Solution as _1
from quizzes._169 import Solution as _169

if __name__ == "__main__":
    input = [2, 2, 1, 1, 1, 2, 2]
    print(f'quiz#169 (Majority Element): {input}, answer: {_169().majorityElement(input)}')


if __name__ == "__main__":
    input = [-3, 0, 1, 3, 4]
    target = 0
    print(f'quiz#1 (TwoSum): input={input}, target ={target}, answer: {_1().twoSum(input, target)}')
