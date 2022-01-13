# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1. Merge Sort(60ms)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode() # val=0인 ListNode(ListNode 정의 참조)
        curr = ans
        while list1 or list2:
            if list1 and list2:
                if list1.val > list2.val:
                    curr.next = list2
                    list2 = list2.next
                else:
                    curr.next = list1
                    list1 = list1.next
                
                # ans.next가 수정된다. 하지만 우변에 직접 ans.next를 할당할 경우 값이 틀어지므로 주의!
                curr = curr.next
                
            elif list1:
                # 좌변 ans.next 계속 ans.next 값만 변경하므로 금지!
                curr.next = list1
                list1 = None
            
            else:
                curr.next = list2
                list2 = None
        
        return ans.next


# 2. Merge Sort fixed(61ms)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode() # val=0인 ListNode(ListNode 정의 참조)
        curr = ans
        while list1 and list2:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next

            # ans.next가 수정된다. 하지만 우변에 직접 ans.next를 할당할 경우 값이 틀어지므로 주의!
            curr = curr.next
                
        curr.next = list1 or list2
        
        return ans.next


# 3. recursive (38ms)
# a) list1이 비었으면, 남은 값은 list2 뿐이므로 list2를 반환한다.(반대의 경우도 같음) 하나씩 번갈아가며 보내기 때문에 list1과 list2의 None값 확인 순서는 변경되어도 상관이 없다.
# b) list1.val > list2.val이라면 (list2.val이 더 작으므로) list2.val을 유지하고 list2.next와 list1을 재귀함수로 확인한다.(반대의 경우 list1)
# c) 재귀가 끝나고 마지막 return문에서 완성된 list1과 list2 중 하나를 반환하는데, else문에서 비교했던 val값과 같은 부등호를 사용하여 val값을 비교하여 더 작았던 list를 반환한다.
# tip) 여기선 list1.val > list2.val을 비교했는데, 만약 return문에서 list1.val >= list2.val로 비교한다면 둘의 첫 값이 같았을 때 먼저 return하는 값을 누구로 정했는 지에 따라 오류가 생길 수 있어 부등호를 통일해주어야 한다.
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # recursive문의 마무리
        if list1 is None:
            return list2
        elif list2 is None:
            return list1 
        else:
            if list1.val > list2.val:
                list2.next = self.mergeTwoLists(list1, list2.next)
            else:
                list1.next = self.mergeTwoLists(list1.next, list2)
        
        return list2 if list1.val > list2.val else list1