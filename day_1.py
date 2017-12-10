def captcha(int_nums):
    _sum = 0
    nums = list(str(int_nums))
    previous = nums[-1]
    for i in nums:
        if i == previous:
            _sum += int(i)
        previous = i
    return _sum     

def captcha2(int_nums):
    _sum = 0
    nums = list(str(int_nums))
    step = len(nums)/2
    nums.extend(nums[:step])
    # import ipdb; ipdb.set_trace()
    for index, digit in enumerate(nums[:-step]):
        if digit == nums[index+step]:
            _sum += int(digit)
    return _sum

if __name__ == '__main__':
    assert captcha(1122) == 3
    assert captcha(1111) == 4
    assert captcha(1234) == 0
    assert captcha(91212129) == 9

    assert captcha2(1212) == 6
    assert captcha2(1221) == 0
    assert captcha2(123425) == 4
    assert captcha2(123123) == 12
    assert captcha2(12131415) == 4
