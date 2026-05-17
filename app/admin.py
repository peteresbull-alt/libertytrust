from django.contrib import admin

from .models import (
    Account,
    Beneficiary,
    AuditLog,
    Card,
    ExchangeRate,
    Loan,
    Notification,
    LoanRepayment,
    SupportTicket,
    CustomUser,
    Transaction,
    DepositDetails,
)


# Register your models here.
admin.site.register(Account)
admin.site.register(Beneficiary)
admin.site.register(Card)
admin.site.register(ExchangeRate)
admin.site.register(Loan)
admin.site.register(LoanRepayment)
admin.site.register(Notification)
admin.site.register(SupportTicket)
admin.site.register(CustomUser)
admin.site.register(AuditLog)
admin.site.register(Transaction)


@admin.register(DepositDetails)
class DepositDetailsAdmin(admin.ModelAdmin):
    list_display = ['label', 'payment_method', 'user', 'is_active', 'created_at']
    list_filter = ['payment_method', 'is_active']
    list_editable = ['is_active']
    search_fields = ['label', 'user__email', 'bank_name', 'paypal_email', 'cashapp_cashtag', 'crypto_address']
    ordering = ['payment_method', 'label']
    fieldsets = (
        ('General', {
            'fields': ('user', 'payment_method', 'label', 'is_active'),
        }),
        ('Bank Transfer Details', {
            'fields': ('bank_name', 'account_name', 'account_number', 'routing_number', 'swift_code', 'iban', 'bank_address'),
            'classes': ('collapse',),
        }),
        ('PayPal Details', {
            'fields': ('paypal_email',),
            'classes': ('collapse',),
        }),
        ('Crypto Details', {
            'fields': ('crypto_currency', 'crypto_network', 'crypto_address'),
            'classes': ('collapse',),
        }),
        ('CashApp Details', {
            'fields': ('cashapp_cashtag', 'cashapp_name'),
            'classes': ('collapse',),
        }),
    )


