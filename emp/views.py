from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Emp
from .form import FeedbackForm

# Home Page View for Employee List
def emp_home(request):
    emps = Emp.objects.all()  # Fetch all employee records
    return render(request, "emp/home.html", {
        'emps': emps  # Pass employee list to the template
    })

# Add New Employee View
def add_emp(request):
    if request.method == "POST":
        # Data fetching from form
        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working") == 'on'  # Convert checkbox to boolean
        emp_department = request.POST.get("emp_department")

        # Input validation: Check for missing required fields
        if not emp_name or not emp_id or not emp_phone or not emp_department:
            return HttpResponse("Missing required fields", status=400)

        # Create and save new employee object
        Emp.objects.create(
            name=emp_name,
            emp_id=emp_id,
            phone=emp_phone,
            address=emp_address,
            department=emp_department,
            working=emp_working  # Handle working status directly
        )

        # Redirect to employee home page after successful submission
        return redirect("emp_home")  # Use named URL for better maintainability
    
    # Render the add employee form on GET request
    return render(request, "emp/add_emp.html", {})

# Delete Employee View
def delete_emp(request, emp_id):
    # Use get_object_or_404 for better error handling
    emp = get_object_or_404(Emp, pk=emp_id)
    emp.delete()  # Delete the employee

    # Redirect to the home page after deletion
    return redirect("emp_home")  # Use named URL for better maintainability

# Update Employee View (Displays update form)
def update_emp(request, emp_id):
    # Use get_object_or_404 for better error handling
    emp = get_object_or_404(Emp, pk=emp_id)
    return render(request, "emp/update_emp.html", {
        'emp': emp
    })

# Handle Employee Update Form Submission
def do_update_emp(request, emp_id):
    if request.method == 'POST':
        # Data fetching from form
        emp_name = request.POST.get("emp_name")
        emp_id_temp = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working") == 'on'  # Convert checkbox to boolean
        emp_department = request.POST.get("emp_department")

        # Fetch the existing employee object
        emp = get_object_or_404(Emp, pk=emp_id)

        # Update employee details
        emp.name = emp_name
        emp.emp_id = emp_id_temp
        emp.phone = emp_phone
        emp.address = emp_address
        emp.department = emp_department
        emp.working = emp_working  # Handle working status directly

        # Save the updated employee object
        emp.save()

        # Redirect to employee home page after updating
        return redirect("emp_home")  # Use named URL for better maintainability
    
    # If not a POST request, redirect to home
    return redirect("emp_home")


def feedback(request):
    if request.method=='GET':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['email'])
            print(form.cleaned_data['name'])
            print(form.cleaned_data['feedback'])
            print("DATA SAVED....")
        else:
            return render(request,"emp/feedback.html",{'form':form})
    else:
        form=FeedbackForm()
        return render(request,"emp/feedback.html",{'form':form})