pip install DjangoTemplateConverter
python setup.py sdist
twine upload dist/\*

arguments :- all arguments without quotes

--rl = remove length
--rl [number] , example: --rl 7 :- remove starting length  
default = 7

--su = static url
--su [string] , example: --su staticfile :- replace "staticfile" string from urls
default = static

--md = mode :- there are only 2 mode
--md [anything] , example: --md any :- look for selected .extentions = ['css', 'png', 'jpg', 'json','ico']
default = ['css']
