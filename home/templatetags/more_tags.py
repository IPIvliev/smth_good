# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django import template
from home.models import Act
from django.utils.html import format_html


register = template.Library()

@register.simple_tag
def accessory(current, customer):
    """
    Generate an individual page index link in a paginated list.
    """
    if current == customer:
        return format_html('<span class="badge badge-sm bg-gradient-success">>>>></span>')
    else:
        return format_html('<span class="badge badge-sm bg-gradient-primary">>>>></span>')
    
@register.simple_tag
def act_finish(act_id):
    """
    Generate an individual page index link in a paginated list.
    """
    # act_id = str(act_id)
    # act = Act.objects.get(id=act_id)
    # if act.customer_sign == True:
    #     return format_html('<span class="badge badge-sm bg-gradient-success">>>>></span>')
    # else:
    #     return format_html('<span class="badge badge-sm bg-gradient-primary">>>>></span>')
    
    if act_id:
        act = Act.objects.get(id=act_id)

        if act.customer_sign == False and act.executor_sign == False:
            answer = '<span class="badge badge-sm bg-gradient-primary">Выставлен</span>'
        elif act.customer_sign == True and act.executor_sign == True:
            answer = '<span class="badge badge-sm bg-gradient-success">V</span><span style="margin-left: 5px;" class="badge badge-sm bg-gradient-success">V</span>'
        elif act.customer_sign == True and act.executor_sign == False:
            answer = '<span class="badge badge-sm bg-gradient-success">V</span><span style="margin-left: 5px;" class="badge badge-sm bg-gradient-danger">X</span>'
        elif act.customer_sign == False and act.executor_sign == True:
            answer = '<span class="badge badge-sm bg-gradient-danger">X</span><span style="margin-left: 5px;" class="badge badge-sm bg-gradient-success">V</span>'
        else:
            answer = 'end'
    else:
        answer = '<span class="badge badge-sm bg-gradient-dark">Не выставлен</span>'


    return format_html(answer)
