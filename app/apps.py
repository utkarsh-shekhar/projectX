from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'app'
    #adding the Logout functionality
    def Logout(request)
        return render(request, 'apps/index.html')
