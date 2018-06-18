import re
from django import template
from pyquery import PyQuery as pq   
from ..models import Blog  #导入模型

register = template.Library()

@register.simple_tag()
def get_blog_img(content):
    html = pq(content)
    reg = r"\/media\/upload.*?\.(?:jpg|png|bmp|gif)"
    imgre = re.compile(reg)
    img_path = imgre.search(html.html())
    if img_path:
        return img_path.group()
    else:
        return '/static/img/django.jpg'