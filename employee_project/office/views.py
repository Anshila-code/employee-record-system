from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from django.db.models import Q

from .models import Employee


def index(request):

    employees = Employee.objects.all()

    return render(
        request,
        'office/index.html',
        {'employees': employees}
    )


def add_employee(request):

    if request.method == 'POST':

        name = request.POST['name']

        department = request.POST['department']

        salary = request.POST['salary']

        Employee.objects.create(

            name=name,

            department=department,

            salary=salary

        )

        return redirect('index')

    return render(
        request,
        'office/add_employee.html'
    )


def edit_employee(request, id):

    employee = Employee.objects.get(id=id)

    if request.method == 'POST':

        employee.name = request.POST['name']

        employee.department = request.POST['department']

        employee.salary = request.POST['salary']

        employee.save()

        return redirect('index')

    return render(
        request,
        'office/edit_employee.html',
        {'employee': employee}
    )


def delete_employee(request, id):

    employee = Employee.objects.get(id=id)

    employee.delete()

    return redirect('index')


def search_employee(request):

    query = request.GET.get('q')

    employees = Employee.objects.all()

    if query:

        employees = employees.filter(

            Q(id__icontains=query) |

            Q(name__icontains=query) |

            Q(department__icontains=query)

        )

    return render(

        request,

        'office/search.html',

        {
            'employees': employees,
            'query': query
        }

    )
