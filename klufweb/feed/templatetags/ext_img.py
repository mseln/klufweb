from bs4 import BeautifulSoup
import re

from django import template
register = template.Library()

""" Extracts the html tag for the first image and
    sets width and height to 100% """
def ext_img(value):
    soup = BeautifulSoup(value)

    if(soup.img):
        img_tag = str(soup.img)

        img_tag = re.sub('width:(\d+)px', 'width:100%', img_tag)
        img_tag = re.sub('height:(\d+)px', 'height:100%' , img_tag)

        return img_tag
    else:
        return ''



register.filter('ext_img', ext_img)

