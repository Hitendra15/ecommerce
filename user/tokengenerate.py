from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

class EmailVerificationToken(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        print('USER ID',user)
        userid = text_type(user.pk)
        timestamp = text_type(timestamp)
        is_active = text_type(user.is_active)
        return f"{userid}{timestamp}{is_active}"
    
account_activation_token = EmailVerificationToken()
