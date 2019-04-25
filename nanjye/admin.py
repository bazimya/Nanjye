from django.contrib import admin
from .models import categories,product,image,productowner,buyer,client,welcomeimages


admin.site.register(categories)
admin.site.register(product)
admin.site.register(image)
admin.site.register(productowner)
admin.site.register(buyer)
admin.site.register(client)
admin.site.register(welcomeimages)


