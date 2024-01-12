from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views import View
from .forms import LoginForm
from django.contrib.auth.models import User
import redis


class LoginView(View):
    template_name = 'login.html'
    form_class = LoginForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})
        
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.filter(email=email).first()
            if user:
                
                print('welcome!!!! :3')
                # go too profile
            else:
                messages.error(
                        request, 
                        f'{email} does not EXIST!!! :D',
                        'danger'
                    )

        return render(request, self.template_name, {'form': form})
    
        


# from django.
# from redis_om import (
#     Field,
#     get_redis_connection,
#     HashModel,
#     Migrator
# )

# # from redis_om import (
# # Field,
# # get_redis_connection,
# # HashModel,
# # Migrator
# # )
# # redis_connection = get_redis_connection()
# class Customer(HashModel):
#     first_name: str
#     last_name: str = Field(index=True)
#     age: int