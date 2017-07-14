from config import settings


def facebook_info(request):
    context = {
        'facebook_app_id': settings.FACEBOOK_APP_ID,
        'site_url': settings.SITE_URL,
    }
    return context