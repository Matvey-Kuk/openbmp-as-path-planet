from django.contrib import admin
from rest.models import PathUpdate, Peer, Prefix, AS

admin.site.register(Peer)
admin.site.register(Prefix)
admin.site.register(AS)


# class ASInline(admin.TabularInline):
#     model = AS
#     extra = 4
#
#
class PathUpdateAdmin(admin.ModelAdmin):
    pass
#     # inlines = [
#     #     ASInline,
#     # ]

admin.site.register(PathUpdate, PathUpdateAdmin)
