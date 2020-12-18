from modeltranslation.translator import register, TranslationOptions
from deposit.models import Deposit

@register(Deposit)
class ThemeTranslationOptions(TranslationOptions):
    fields = ('deposit_amount','review',)
