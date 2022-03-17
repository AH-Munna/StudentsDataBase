from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from mainControl import srForm
from mainControl.models import Students, Students_Information

def home(request):
    return render(request, 'mainControl/index.html', {'title': 'Home'})

def studentRegistrationForm(request):
    new_form = srForm.sRegistrationForm()
    dict = {'title': 'Student Registration', 'form_info': new_form}

    if request.method == 'POST':
        new_form = srForm.sRegistrationForm(request.POST)
        dict.update({'form_info': new_form})

        if new_form.is_valid():
            new_form.save(commit=True)
            return home(request)

    return render(request, 'mainControl/srForm.html', dict)

def allStudents(request):
    student_list = Students.objects.order_by('id')
    student_info = Students_Information.objects.order_by('phone')
    dict = {'title': 'All students', 'student_list': student_list, 'student_info': student_info}

    return render(request, 'mainControl/allStudents.html', dict)

def siForm(request):
    new_form = srForm.sInformationForm()
    dict = {'title': 'Student Registration', 'form_info': new_form}

    if request.method == 'POST':
        new_form = srForm.sInformationForm(request.POST)
        dict.update({'form_info': new_form})

        if new_form.is_valid():
            new_form.save(commit=True)
            return home(request)

    return render(request, 'mainControl/siForm.html', dict)

class IndexView(TemplateView):
    template_name = 'mainControl/indexMC.html'

    # for context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'class based view'
        context['text'] = 'this is a class based view'
        return context

class StudentListView(ListView):
    context_object_name = 'studentList'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'list view'
        return context
    model = Students
    template_name = 'mainControl/listView.html'

# methode student information
def SiViews(request, pk):
    student_info = Students.objects.get(id=pk)
    student_infos = Students_Information()
    try:
        student_infos = Students_Information.objects.get(students_information_id=pk)
    except:
        student_infos.phone = '---'
        student_infos.registration_semester = '-'
        student_infos.registration_year = '-'
        student_infos.date_of_birth = '---'
    dict = {'title': "student informations", 'student_info': student_infos, 'student': student_info}

    return render(request, 'mainControl/siView.html', context=dict)
# class student informtaion
class SiView2(DetailView):
    context_object_name = 'student'
    model = Students
    template_name = 'mainControl/siView.html'
    
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = 'detail view'
            return context

# create view class, add student class
class AddStudent(CreateView):
    model = Students
    fields = '__all__'
    template_name = 'mainControl/srForm2.html'