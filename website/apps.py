from django.apps import AppConfig

class WebsiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'website'  # Ensure the name matches your app directory name
    verbose_name = "Website"  # Optional: Human-readable name for the app
