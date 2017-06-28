from ed4all.models import Appointment, Counselor, Educator, Incident, Student, Studentprofile
from django.core.urlresolvers import reverse_lazy, reverse
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.core.mail import send_mail


# ========== home =========

def home(request, template_name='ed4all/home.html'):
    incidents = Incident.objects.all()
    contents = {}
    contents["incidents"] = incidents
    return render(request, template_name, contents)


# ========== form =========

class IncidentForm(ModelForm):
    class Meta:
        model = Incident
        fields = ['incidentid', 'studentid', 'incidenttype', 'location', 'educatorid', 'counselorid', 'status']

class IncidentEditForm(ModelForm):
    class Meta:
        model = Incident
        fields = [ 'studentid', 'incidenttype', 'location', 'educatorid', 'counselorid', 'status']

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['studentid', 'studentlname', 'studentfname', 'studentemailaddress', 'studentage', 'studentdob',
                  'street', 'city', 'zip', 'program', 'trackrepid', 'studentpassword', 'studenttype']


# =========== student login home ==========
@csrf_exempt
def student_home(request):
    err = True
    ctx = {}
    ctx["error"] = err
    if 'sid' in request.session:
        sid = request.session['sid']
        ctx["sid"] = sid
        student = Student.objects.get(studentid=sid)
        ctx['student'] = student
        return render(request, "ed4all/student_home.html", ctx)
    else:
        try:
            if request.method == 'POST':
                sid = request.POST['sid']
                pwd = request.POST['spwd']
                student = Student.objects.get(studentid=sid)
                if pwd == student.studentpassword:
                    ctx['sid'] = sid
                    ctx['student'] = student
                    request.session['sid'] = sid
                    request.session['spwd'] = pwd
                    return render(request, "ed4all/student_home.html", ctx)
                else:
                    err = False
                    ctx["error"] = err
                    ctx["message"] = "Wrong Password/Username"
                    return render(request, 'index.html', ctx)
            else:
                err = False
                ctx["error"] = err
                ctx["message"] = "Wrong Password/Username"
                return render(request, 'index.html', ctx)
        except Student.DoesNotExist:
            err = False
            ctx["error"] = err
            ctx["message"] = "Wrong Password/Username"
            return render(request, 'index.html', ctx)

# =========== faculty login home ==========
@csrf_exempt
def educator_home(request):
    err = True
    ctx = {}
    ctx["error"] = err
    if 'eid' in request.session:
        eid = request.session['eid']
        ctx["eid"] = eid
        educator = Educator.objects.get(educatorid=eid)
        ctx['educator'] = educator
        return render(request, "ed4all/educator_home.html", ctx)
    else:
        try:
            if request.method == 'POST':
                eid = request.POST['eid']
                pwd = request.POST['epwd']
                educator = Educator.objects.get(educatorid=eid)
                if pwd == educator.educatorpassword:
                    ctx['eid'] = eid
                    ctx['educator'] = educator
                    request.session['eid'] = eid
                    request.session['epwd'] = pwd
                    return render(request, "ed4all/educator_home.html", ctx)
                else:
                    err = False
                    ctx["error"] = err
                    ctx["message"] = "Wrong Password/Username"
                    return render(request, 'index.html', ctx)
            else:
                err = False
                ctx["error"] = err
                ctx["message"] = "Wrong Password/Username"
                return render(request, 'index.html', ctx)
        except Student.DoesNotExist:
            err = False
            ctx["error"] = err
            ctx["message"] = "Wrong Password/Username"
            return render(request, 'index.html', ctx)


# =========== counselor login home ==========
@csrf_exempt
def counselor_home(request):
    err = True
    ctx = {}
    ctx["error"] = err
    if 'cid' in request.session:
        cid = request.session['cid']
        ctx["cid"] = cid
        counselor = Counselor.objects.get(counselorid=cid)
        ctx['counselor'] = counselor
        return render(request, "ed4all/counselor_home.html", ctx)
    else:
        try:
            if request.method == 'POST':
                cid = request.POST['cid']
                pwd = request.POST['cpwd']
                counselor = Counselor.objects.get(counselorid=cid)
                if pwd == counselor.counselorpassword:
                    ctx['cid'] = cid
                    ctx['counselor'] = counselor
                    request.session['cid'] = cid
                    request.session['cpwd'] = pwd
                    return render(request, "ed4all/counselor_home.html", ctx)
                else:
                    err = False
                    ctx["error"] = err
                    ctx["message"] = "Wrong Password/Username"
                    return render(request, 'index.html', ctx)
            else:
                err = False
                ctx["error"] = err
                ctx["message"] = "Wrong Password/Username"
                return render(request, 'index.html', ctx)
        except Counselor.DoesNotExist:
            err = False
            ctx["error"] = err
            ctx["message"] = "Wrong Password/Username"
            return render(request, 'index.html', ctx)

# ========== Forms =========

#class IncidentForm(ModelForm):
#    class Meta:
#        model = Incident
#        fields = '__all__'

#class StudentForm(ModelForm):
#    class Meta:
#       model = Student
#        fields = '__all__'

class CounselorForm(ModelForm):
    class Meta:
        model = Counselor
        fields = '__all__'

class EducatorCreateForm(ModelForm):
    incidentid = forms.CharField(label='incidentid')
    educatorid = forms.ModelChoiceField(queryset=Educator.objects.all(), label='ID')
    studentid = forms.ModelChoiceField(queryset=Student.objects.all(), required=False, label='Student ID')
    counselorid = forms.ModelChoiceField(queryset=Counselor.objects.all(), required=False,
                                         label='Counselor')
    location = forms.CharField(label='Location')
    incidenttype = forms.CharField(label='Type')

    class Meta:
        model = Incident
        fields = ['incidentid','educatorid', 'studentid', 'counselorid', 'incidenttype', 'location', 'status']
        widgets = {
            'incidenttype': forms.TextInput,
            'location': forms.TextInput
        }

class StudentProfileForm(ModelForm):
        class Meta:
            model = Studentprofile
            fields = '__all__'

# =========== counselor view student profile and crud incident ==========

def student_list(request,template_name='ed4all/student_list.html'):
    student = Student.objects.all()
    ctx = {}
    ctx['student'] = student
    return render(request, template_name, ctx)

def student_view(request, pk, template_name='ed4all/student_view.html'):
    student= get_object_or_404(Student, studentid=pk)
    trackrep = get_object_or_404(Student,studentid=student.trackrepid)
    profile = Studentprofile.objects.filter(studentid=pk)
    ctx = {}
    ctx["student"] = student
    ctx["trackrep"] = trackrep
    ctx["profile"] = profile
    return render(request, template_name, ctx)

def incident_list(request,template_name='ed4all/incident_list.html'):
    ctx={}
    incident= Incident.objects.all()
    ctx['incident']=incident
    return render(request,template_name,ctx)

def incident_view(request, pk, template_name='ed4all/incident_view.html'):
    incident= get_object_or_404(Incident, incidentid=pk)
    student = Student.objects.filter(incident=pk)
    counselor=Counselor.objects.filter(incident=pk)
    ctx = {}
    ctx["i"] = incident
    ctx["s"] = student
    ctx['c']=counselor
    return render(request, template_name, ctx)

def incident_edit(request, pk, template_name='ed4all/incident_edit.html'):
    incident= get_object_or_404(Incident, incidentid=pk)
    form = IncidentEditForm(request.POST or None, instance=incident)
    if form.is_valid():
        form.save()
        return redirect('ed4all:incident_list')
    ctx = {}
    ctx["form"] = form
    ctx["incident"] = incident
    return render(request, template_name, ctx)

def incident_delete(request, pk, template_name='ed4all/incident_delete.html'):
    incident = get_object_or_404(Incident, incidentid=pk)
    if request.method=='POST':
        incident.delete()
        return redirect('ed4all:incident_list')
    ctx = {}
    ctx["incident"] = incident
    return render(request, template_name, ctx)

def incident_create(request, template_name='ed4all/incident_form.html'):
    form = IncidentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ed4all:counselor_home')
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)

# =========== student view own profile ============
def student_view_detail(request, template_name='ed4all/student_view_detail.html'):
    pk = request.session['sid']
    student = get_object_or_404(Student, studentid=pk)
    trackrep = get_object_or_404(Student, studentid=student.trackrepid)
    profile = Studentprofile.objects.filter(studentid=pk)
    ctx = {}
    ctx["student"] = student
    ctx["trackrep"] = trackrep
    ctx["profile"] = profile
    return render(request, template_name, ctx)

def student_view_incident(request, template_name='ed4all/student_view_incident.html'):
    sid = request.session['sid']
    incident = Incident.objects.filter(studentid=sid)
    ctx = {}
    ctx["incident"] = incident
    return render(request, template_name, ctx)

# ============ educator reports an incident ==========
def educator_create_incident(request, template_name='ed4all/educator_create_incident.html'):
    ctx = {}
    ctx['error'] = "error"
    eid = request.session['eid']
    form = EducatorCreateForm(request.POST or None, initial={'educatorid': eid})
    form.fields['educatorid'].queryset = Educator.objects.filter(educatorid=eid)
    if form.is_valid():
        form.save()
        return redirect('ed4all:educator_home')
    ctx["form"] = form
    return render(request, template_name, ctx)


# ============ educator views students ==========
def educator_student_list(request,template_name='ed4all/educator_student_list.html'):
    student = Student.objects.all()
    ctx = {}
    ctx['student'] = student
    return render(request, template_name, ctx)

# ============ educator views incidents ==========
def educator_incident_list(request,template_name='ed4all/educator_incident_list.html'):
    eid = request.session['eid']
    incident = Incident.objects.filter(educatorid=eid)
    ctx={}
    ctx["incident"] = incident
    return render(request,template_name,ctx)

# ============ educator views student profile ==========
def educator_student_view(request, pk, template_name='ed4all/educator_student_view.html'):
    student= get_object_or_404(Student, studentid=pk)
    trackrep = get_object_or_404(Student,studentid=student.trackrepid)
    profile = Studentprofile.objects.filter(studentid=pk)
    ctx = {}
    ctx["student"] = student
    ctx["trackrep"] = trackrep
    ctx["profile"] = profile
    return render(request, template_name, ctx)

