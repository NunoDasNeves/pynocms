# pynocms

"Its not cms unless its pynocms"

simple python-based designed for blogs

/------------------------------/  
/-------- dir structure -------/

<ul>
<li>main.py</li>
<li>dbconfig.py</li>
<li>/core  
	<ul>
    <li>dbclasses.py</li>  
    <li>admin.py</li>  
    <li>edit.py</li>  
    <li>/admin  
        <ul>    
        <li>edit.html</li>  
        <li>dashboard.html</li>    
        <li>login.html</li>  
        <li>style.css</li>  
        </ul></li>  
    <li>/setup  
        <ul>  
        <li>setup1.html</li>  
        <li>setup2.html</li>  
        <li>style.css</li>  
        </ul></li>      
    <li>/media  
        <ul>  
        <li>hamburger.png</li>
        </ul></li>
    </ul>
</li>
<li>/content
    <ul>  
    <li>/templates  
        <ul>  
        <li>page.py</li>  
        <li>post.py</li>  
        <li>blog.py</li>  
        <li>home.py</li>  
        </ul></li>
    <li>/theme  
        <ul>  
        <li>header.html</li>  
        <li>sidebar.html</li>  
        <li>footer.html</li>  
        <li>somescript.js</li>  
        <li>style.css</li>  
        </ul></li>
    <li>/uploads  
        <ul>
        <li>default.jpg</li>  
        </ul></li>
    </ul>
</ul>

/------------------------------/  
/-------- SQL structure -------/

dbname: pycms  

pages  
* id  
* title
* author
* createdate
* editeddate
* slug
* text
* template

posts  
* id
* author
* title
* createdate
* editeddate
* tags
* slug
* photo
* text

comments  
* id
* postid
* author
* date
* text

users  
* id
* joindate
* group
* username
* email
* password

sessions  
* id
* sid
* user
* date
    
options  
* pagetemplate
* posttemplate
* hometemplate
* allownewusers
* allowcomments
* categoryslug


/------------------------------/

apache config

make sure the following modules are enabled:
cgi
dir
rewrite

'''
<Directory "/srv/http">  

    Options Indexes FollowSymLinks  
    Allow Override All  
    
    Require all granted  
</Directory>
'''
