# 연관 Algorithm : Divine and Conquer Algorithm

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # 연산 후 result에 넣고 반환
        def compute(left, right, op):
            result = []

            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            return result

        if expression.isdigit():
            return [int(expression)]

        results = []
        # for문을 이용해 각 케이스 별로 연산이 가능함. 2+1-1 일때, 2 + 1-1과 2+1 - 1로 나눠져서 연산 후,
        for index, value in enumerate(expression):
            if value in "-*+":
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index + 1:])
                
                # return 받은 result를 여기서 results에 반환
                results.extend(compute(left, right, value))

        return results