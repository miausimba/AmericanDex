from django.contrib.admin.apps import AdminConfig


class AmericandexAdminConfig(AdminConfig):
    default_site = "admin_panel.admin.AmericandexAdminSite"
