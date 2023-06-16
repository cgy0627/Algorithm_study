def solution(arr, delete_list):
    delete_key = dict(zip(delete_list, delete_list))
    
    return [num for num in arr if num not in delete_key ]