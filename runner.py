from quizzes._26 import Solution


if __name__ == "__main__":
    s = Solution()
    k, nums = s.remove_duplicated_from_sorted_array([1, 1, 2, 2, 2])
    print(f"k={k}", "|", f"nums={nums}")
