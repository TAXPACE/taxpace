#!python
print("content-type:text/html")
print()

import cgi, os, view

form = cgi.FieldStorage()
if 'id' in form :
    pageId = form["id"].value
    description = open('data/' + pageId, 'r').read()
else :
    pageId = 'Welcome'
    description = 'Hello, Web'

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
    #URL Query String을 만들어 주는 URL Query 생성자
    <form action="process_update.py" method="post">
        <input type="hidden" name="pageId" value="{form_default_title}">
        <p><input type="text" name="title" placeholder="Title" value="{form_default_title}"></p>
        <p><textarea rows="4" name="description" placeholder="description">{form_default_description}</textarea></p>
        <p><input type="submit"></p>
    </form>
<h1>{title}</h1>
<p>{desc}</p>
</body>
</html>
 '''.format(title=pageId, desc=description, listStr=view.getList, form_default_title=pageId, form_default_description=description))
