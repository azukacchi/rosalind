# LargestNumber(Digits):
# answer ← empty string
# while Digits is not empty:
# maxDigit ← −∞
# for digit in Digits:
# if digit ≥ maxDigit:
# maxDigit ← digit
# append maxDigit to answer
# remove maxDigit from Digits
# return answer

# s = '''2
s = '''4
54 235 31 320'''

digits = sorted([int(i) for i in s.split('\n')[1:][0].split()],reverse=True)

# digits = []

def IsGreaterOrEqual(digit,max_digit):
    if int(str(digit)+str(max_digit))>= int(str(max_digit)+str(digit)):
        return True

def LargestNumber(digits):
    answer = ''
    while len(digits)>0:
        digits_1 = digits.copy()
        digits_2 = digits.copy()
        while len(digits_2)>0:
            max_digit = 0
            i=0
            for digit in digits_1:
                if IsGreaterOrEqual(digit,max_digit) == True:
                    max_digit,k = digit,i
                digits_2.pop(0)
                i+=1
        answer+=str(max_digit)
        digits.pop(k)
    return answer

print(LargestNumber(digits))