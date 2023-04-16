from django import template

register = template.Library()

@register.filter(name="cuts")
def cuts(value,arg):
    " Cuts the arg<string> from value<string> "
    
    return value.replace(arg,"")

# register.filter('cuts',cuts)
