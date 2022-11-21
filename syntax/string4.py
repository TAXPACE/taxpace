#positional formatting
print('Lorem {} ipsum dolor sit {} amet, consectetur {} adipisicing elit, {} sed do eiusmod tempor {} incididunt ut labore et {} dolore magna aliqua.'.format('good', 'bad', 'news', 'letter', 'tax', 'corp'))


#Named placeholder
print('Lorem {name} ipsum dolor sit {name} amet, consectetur {age:d} adipisicing elit, {age:d} sed do eiusmod tempor {name} incididunt ut labore et {age:d} dolore magna aliqua.'.format(name='boki', age=38))
