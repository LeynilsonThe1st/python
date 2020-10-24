import colors
text = str(input('Insert a phrase: ')).upper().replace(' ', '')
rev_text = text[::-1]
print('The reverse of {} is {}'.format(text, rev_text))

if text == rev_text:
    print('Yes, we have a palindrome!!')
else:
    print(colors.red, 'This is not a palindrome, STUPID!!')
