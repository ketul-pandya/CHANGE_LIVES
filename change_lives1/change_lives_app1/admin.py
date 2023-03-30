from django.contrib import admin

# Register your models here.
from change_lives_app1.models import Signup,Contact,Registration,Payment_model,Patient_Model
admin.site.register(Signup)
admin.site.register(Contact)
admin.site.register(Registration)
admin.site.register(Payment_model)
# admin.site.register(uplaod_file)

admin.site.register(Patient_Model)