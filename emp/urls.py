from django.urls import path
from .views import emp_home, add_emp, delete_emp, update_emp, do_update_emp, feedback  # Explicitly import views

urlpatterns = [
    path("home/", emp_home, name="emp_home"),  # Named URL for better reference
    path("add-emp/", add_emp, name="add_emp"),  # Named URL for better reference
    path("delete-emp/<int:emp_id>/", delete_emp, name="delete_emp"),  # Named URL for better reference
    path("update-emp/<int:emp_id>/", update_emp, name="update_emp"),  # Named URL for better reference
    path("do-update-emp/<int:emp_id>/", do_update_emp, name="do_update_emp"),  # Named URL for better reference
    path("feedback/", feedback, name="feedback"),  # Added name for feedback view
]
