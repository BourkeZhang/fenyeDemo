#coding:utf-8
from django.utils.safestring import mark_safe

def Page(page,all_pages_count):
    '''
    :param page:当前页
    :param all_pages_count:总页数
    :return:分页后的html字符串
    '''
    page_html=[]
    a_html = '''<a href="/appFenye/index/1">首页</a>'''
    page_html.append(a_html)
    if page>1:
        a_html = '''<a href="/appFenye/index/%d">上一页</a>'''%(page-1)
    else:
        a_html = '''<a href="#">上一页</a>'''
    page_html.append(a_html)
    #11个页码
    if all_pages_count<11:
        begain=0
        end=all_pages_count
    #总页数大于11
    else:
        if page<6:
            begain=0
            end =12
        else:
            if page+6>all_pages_count:
                begain=page-5
                end = all_pages_count
            else:
                begain=page -5
                end =page+5
    for i in range(begain,end):
        if page == i+1:
            a_html='''<a class='selected' href="/appFenye/index/%d">%d</a>'''%(i+1,i+1)
        else:
            a_html='''<a href="/appFenye/index/%d">%d</a>'''%(i+1,i+1)
        page_html.append(a_html)
    if page<all_pages_count:
        a_html = '''<a href="/appFenye/index/%d">下一页</a>'''%(page+1)
    else:
        a_html = '''<a href="#">下一页</a>'''
    page_html.append(a_html)
    a_html = '''<a href="/appFenye/index/%d">尾页</a>'''%all_pages_count
    page_html.append(a_html)
    page = mark_safe(' '.join(page_html))
    return  page