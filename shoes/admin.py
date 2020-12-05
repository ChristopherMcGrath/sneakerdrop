from django.contrib import admin
from .models import Shoe, ShoeSpecs, ShoeImage


class ShoeImageInline(admin.StackedInline):
    model = ShoeImage


class ShoeSecsInline(admin.StackedInline):
    model = ShoeSpecs


class ShoeAdmin(admin.ModelAdmin):
    inlines = [ShoeSecsInline, ShoeImageInline]

    class Meta:
        model = Shoe


admin.site.register(Shoe, ShoeAdmin)


# admin.site.register(ShoeSpecs)
# admin.site.register(ShoeImage)
