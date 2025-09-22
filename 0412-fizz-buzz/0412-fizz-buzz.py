class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            div_by_3 = (i % 3 == 0)
            div_by_5 = (i % 5 == 0)

            if div_by_3 and div_by_5:
                s = "FizzBuzz"
            elif div_by_3:
                s = "Fizz"
            elif div_by_5:
                s = "Buzz"
            else:
                s = str(i)
            result.append(s)
        
        return result
