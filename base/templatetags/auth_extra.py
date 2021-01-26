from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    try:
        group =  Group.objects.get(name=group_name)
    except Group.DoesNotExist:
        return False

    return group in user.groups.all()


#{% if request.user|has_group:"mygroup" %} 
#    <p>User belongs to my group 
#{% else %}
#    <p>User doesn't belong to mygroup</p>
#{% endif %}