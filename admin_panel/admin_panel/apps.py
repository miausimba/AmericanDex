from django.contrib.admin.apps import AdminConfig


class UniversedexAdminConfig(AdminConfig):
    default_site = "admin_panel.admin.UniversedexAdminSite"
