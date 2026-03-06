from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
from decimal import Decimal

register = template.Library()

@register.filter(name='currency')
def currency(value):
    """
    Format a number as USD currency.
    Example: 1234567.89 becomes $1,234,567.89
    """
    if value is None:
        return '$0.00'
    
    try:
        value = Decimal(str(value))
        # Format with 2 decimal places and add commas
        formatted = intcomma(f"{value:,.2f}")
        return f"${formatted}"
    except (ValueError, TypeError):
        return '$0.00'


@register.filter(name='currency_no_symbol')
def currency_no_symbol(value):
    """
    Format a number as currency without the dollar sign.
    Example: 1234567.89 becomes 1,234,567.89
    """
    if value is None:
        return '0.00'
    
    try:
        value = Decimal(str(value))
        return f"{value:,.2f}"
    except (ValueError, TypeError):
        return '0.00'


@register.filter(name='currency_short')
def currency_short(value):
    """
    Format large numbers in short form.
    Example: 1234567 becomes $1.23M
    """
    if value is None:
        return '$0'
    
    try:
        value = float(value)
        if value >= 1_000_000_000:
            return f"${value / 1_000_000_000:.2f}B"
        elif value >= 1_000_000:
            return f"${value / 1_000_000:.2f}M"
        elif value >= 1_000:
            return f"${value / 1_000:.2f}K"
        else:
            return f"${value:,.2f}"
    except (ValueError, TypeError):
        return '$0'
    


    