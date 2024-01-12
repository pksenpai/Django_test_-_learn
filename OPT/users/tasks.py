import celery
from .utils import store_otp


@celery.shared_task
def send_customer_disabled_email(user):
    otp_code = store_otp(user.email)
    subject = f'confirm login! here your otp code {otp_code} put it in :/'
    html_message = render_to_string('opt_message.html', {'otp': otp_code})
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER
    to_email = [user.email]
    send_mail(subject, plain_message, from_email, to_email, html_message=html_message)
    
