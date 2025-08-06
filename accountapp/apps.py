from django.apps import AppConfig

class AccountappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accountapp'

    def ready(self):
        # 이 안에서 import 해야 앱 로딩 문제 없음
        from django.contrib.sessions.models import Session
        Session.objects.all().delete()  # 서버 시작 시 모든 세션 삭제 (개발용)