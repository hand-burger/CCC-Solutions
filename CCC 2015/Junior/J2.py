input_text = str(input())

if input_text.count(':-)') > input_text.count(':-('):
    print('happy')
elif input_text.count(':-)') < input_text.count(':-('):
    print('sad')
elif input_text.count(':-)') == 0 and input_text.count(':-(') == 0:
    print('none')
else:
    print('unsure')
