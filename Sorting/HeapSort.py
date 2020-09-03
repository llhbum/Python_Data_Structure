# HeapSort.py
'''
힙정렬(HeapSort)
O(nlogn)
'''
# 변수 설명
# list = unsorted된 리스트
# i = heapify의 대상이 되는 노드
# n = len(list)
def heapify(list, n , i):
    largest = i
    # 왼쪽 자식과 오른쪽 자식의 인덱스 계산 식
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and list[i] < list[l]:
        largest = l

    if r < n and list[largest] < list[r]:
        largest = r

    if largest != i:
        list[i], list[largest] = list[largest] , list[i]

        heapify(list, n , largest)






def HeapSort_min(list):
    n = len(list)

    for i in range(n,-1,-1):
        heapify(list,n,i)

    for i in range(n - 1, 0, -1):
        list[i], list[0] = list[0], list[i]
        heapify(list,i,0)




if __name__ == '__main__':

    #정렬할 리스트 선언
    list = [1, 3, 2, 4, 5, 7, 6, 9, 8]
    list2 = [1, 3, 2, 4, 5, 7, 6, 9, 8]

    # 정렬 전 리스트 출력
    print('- Before Sorting -')
    print(list)
    '''
    - Before Sorting -
    [1, 3, 2, 4, 5, 7, 6, 9, 8]
    '''

    HeapSort_min(list)

    # 정렬 후 리스트 출력
    print('- After Sorting -')
    print(list)
    '''
    - After Sorting -
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    '''
