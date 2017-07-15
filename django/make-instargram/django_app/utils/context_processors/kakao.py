from config import settings


def kakao_info(request):
    context = {
        'kakao_app_id': settings.KAKAO_APP_ID,
        'redirect_uri': settings.KAKAO_REDIRECT_URI,
    }
    return context