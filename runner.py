from quizzes._1 import Solution as _1
from quizzes._2 import Solution as _2, ListNode
from quizzes._169 import Solution as _169

# if __name__ == "__main__":
#     input = [2, 2, 1, 1, 1, 2, 2]
#     print(f'quiz#169 (Majority Element): {input}, answer: {_169().majorityElement(input)}')


# if __name__ == "__main__":
#     input = [-3, 0, 1, 3, 4]
#     target = 0
#     print(f'quiz#1 (TwoSum): input={input}, target ={target}, answer: {_1().twoSum(input, target)}')


if __name__ == "__main__":
    #l1 = [2,4,3]
    #l2 = [5,6,4]
    
    l1=ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=None)))
    l2=ListNode(val=5, next=ListNode(val= 6, next=ListNode(val= 4, next= None)))
    print(f'quiz#2 (addTwoNumbers): l1={l1}, l2 ={l2}, answer: {_2().addTwoNumbers(l1, l2)}')


