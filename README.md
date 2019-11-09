# Zsanta_blog
Zsanta_blog Test

关于第五章Django ORM

需要安装 pip install jupyter notebook django-extensions

修改settings.py 文件：
   <p><code>
        INSTALLED_APPS += ['django_extensions']
   </p></code>
   <p><code>
        NOTEBOOK_ARGUMENTS = [
            '--ip', '127.0.0.1',
            '--port', '9001',
        ]
    </code></p>
命令行运行：
python manage.py shell_plus --notebook
新建ipynb文件
    <p><code>import os, sys</code><p>
    <p><code>MYPROJECT = os.getcwd()[:os.getcwd().find('此处填写你的绝对路径')]</code><p>
    <p><code>os.environ["DJANGO_SETTINGS_MODULE"]= "Zsanta_blog.settings"</code><p>
    <p><code>import django</code><p>
    <p><code>django.setup()</code><p>
