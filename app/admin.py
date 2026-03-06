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


