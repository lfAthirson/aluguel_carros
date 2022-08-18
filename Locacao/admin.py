from django.contrib import admin

from .models import Locacao
from Carros.models import Carro

class LocacaoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'carro', 'data_retirada','data_entrega_prevista', 'data_entrega' ,'status')
    search_fields= ('cliente__nome',)
    list_filter = ('carro', 'data_retirada','data_entrega_prevista', 'data_entrega' ,'status')

    '''
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "carro" and  is None:
            kwargs["queryset"] = Carro.objects.filter(status='L')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
        
    '''

admin.site.register(Locacao, LocacaoAdmin)
