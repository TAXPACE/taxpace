#!C:\Program Files\Python311\python.exe

print("content-type:text/html")
print()

#refactoring

import cgi, os, view

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
    description = description.replace('<', '&lt;')
    description = description.replace('>', '&Gt;')
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action = '''
    <form action="process_delete.py" method="post">
        <input type="hidden" name="pageId" value="{}">
        <input type="submit" value="delete">
    </form>
    '''.format(pageId)
else:
    pageId = 'Welcome'
    description = 'Hello, Web'
    update_link = ''
    delete_action = ''
print('''<!DOCTYPE html>
<html>
<head>
  <title>WEB-1 - html</title>
  <meta charset="euc-kr/n">

</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
    <ol>
        {listStr}
    </ol>
    <a href="create.py">Create</a>
    {update_link}
    {delete_action}
<h1>{title}</h1>
<p>{desc}</p>
</body>
</html>
 '''.format(
 title=pageId,
 desc=description,
 listStr=view.getList(),
 update_link=update_link,
 delete_action=delete_action))
