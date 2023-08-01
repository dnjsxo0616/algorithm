def solution(phone_book):

    hash_phone = {}
    for num in phone_book:
        hash_phone[num] = 1
    
    for num in phone_book:
        res = ""
        for number in num:
            res += number
            if res in hash_phone and res != num:
                return False
    return True