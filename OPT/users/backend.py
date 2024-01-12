# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth import get_user_model
# from django.db.models import Q

# User = get_user_model()

# class EmailOrPhoneBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
        
#         try:
#             user = get_user_model().objects.get(Q(Email=username) | Q(phone_number=username))
#             if user.check_password(password):
#                 return user
        
#         except get_user_model().DoesNotExist:
#             return None
    
#     def get_user(self, user_id):
        
#         try:
#             return get_user_model().objects.get(pk=user_id)
    
#         except get_user_model().DoesNotExist:
#             return None
        
