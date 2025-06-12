from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(field, css_class):
    """Adds a CSS class to the specified field."""
    return field.as_widget(attrs={'class': css_class})
