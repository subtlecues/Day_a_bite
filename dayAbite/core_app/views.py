from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from custom_user.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import BloodGlucoseMeasurementForm, BitesForm, InsulinShotForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from .models import BloodGlucoseMeasurement, BitesConsumedEntry, InsulinShot
from .forms import BloodGlucoseMeasurementForm, BitesForm, InsulinShotForm

def add_blood_glucose(request):
    if request.method == 'POST':
        form = BloodGlucoseMeasurementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome_page')
    else:
        form = BloodGlucoseMeasurementForm()
    return render(request, 'add_blood_glucose.html', {'form': form})

def add_bites_consumed(request):
    if request.method == 'POST':
        form = BitesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome_page')
    else:
        form = BitesForm()
    return render(request, 'add_bites_consumed.html', {'form': form})

def add_insulin_shot(request):
    if request.method == 'POST':
        form = InsulinShotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome_page')
    else:
        form = InsulinShotForm()
    return render(request, 'add_insulin_shot.html', {'form': form})






def index(request):
    print("View function 'index' is called.")
    blood_glucose_form = BloodGlucoseMeasurementForm(request.POST or None)
    bites_form = BitesForm(request.POST or None)
    insulin_shot_form = InsulinShotForm(request.POST or None)

    if request.method == 'POST':
        if blood_glucose_form.is_valid():
            blood_glucose_form.instance.user = request.user
            blood_glucose_form.save()
            messages.success(request, 'Blood glucose level submitted successfully!')

        if bites_form.is_valid():
            bites_form.instance.user = request.user
            bites_form.save()
            messages.success(request, 'Bites eaten submitted successfully!')

        if insulin_shot_form.is_valid():
            insulin_shot_form.instance.user = request.user
            insulin_shot_form.save()
            messages.success(request, 'Insulin shot submitted successfully!')

        # Redirect to the same page after form submission
        return redirect('index')

    return render(request, 'hello.html', {
        'blood_glucose_form': blood_glucose_form,
        'bites_form': bites_form,
        'insulin_shot_form': insulin_shot_form,
    })

def registration_handler(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        date_of_birth = request.POST['date_of_birth']
        user = User.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth
        )

        user.save()

    return render(request, 'register_user.html')



def login_handler(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  
        else:
            return render(request, 'login.html', {'error': 'Wrong username or password'})

    # If it's a GET request, show the login form
    return render(request, 'login.html')
def logout_handler(request):
    logout(request)
    return render(request, 'hello.html')

def my_measurements_view(request):
    user = request.user

    insulin_shots = InsulinShot.objects.filter(user=user)
    blood_glucose_measurements = BloodGlucoseMeasurement.objects.filter(user=user)
    bites_consumed_entries = BitesConsumedEntry.objects.filter(user=user)

    context = {
        'insulin_shots': insulin_shots,
        'blood_glucose_measurements': blood_glucose_measurements,
        'bites_consumed_entries': bites_consumed_entries,
    }

    return render(request, 'my_measurements.html', context)

@login_required
def my_profile_view(request):
    user = request.user
    fields = [field for field in user._meta.get_fields() if field.concrete]

    context = {
        'user': user,
        'fields': fields,
    }

    return render(request, 'my_profile.html', context)

def encyclopedia_view(request):
    advice_text = "Here is some advice about diabetes..."

    context = {
        'advice_text': advice_text,
    }

    return render(request, 'encyclopedia.html', context)

@login_required
def edit_measurement(request, model, pk):
    measurement = None
    if model == 'blood_glucose':
        measurement = get_object_or_404(BloodGlucoseMeasurement, pk=pk)
        form = BloodGlucoseMeasurementForm(request.POST or None, instance=measurement)
    elif model == 'insulin_shot':
        measurement = get_object_or_404(InsulinShot, pk=pk)
        form = InsulinShotForm(request.POST or None, instance=measurement)
    elif model == 'bites_entry':
        measurement = get_object_or_404(BitesConsumedEntry, pk=pk)
        form = BitesForm(request.POST or None, instance=measurement)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('my_measurements')

    template_name = 'edit_measurement.html'
    context = {'form': form, 'measurement': measurement, 'model': model}
    return render(request, template_name, context)

@login_required
def delete_measurement(request, measurement_type, measurement_id):
    user = request.user

    if measurement_type == 'blood_glucose':
        measurement = get_object_or_404(BloodGlucoseMeasurement, pk=measurement_id, user=user)
    elif measurement_type == 'insulin_shot':
        measurement = get_object_or_404(InsulinShot, pk=measurement_id, user=user)
    elif measurement_type == 'bites_entry':
        measurement = get_object_or_404(BitesConsumedEntry, pk=measurement_id, user=user)
    else:
        return render(request, 'error.html', {'error': 'Invalid measurement type.'})

    if request.method == 'POST':
        measurement.delete()
        messages.success(request, 'Measurement deleted successfully.')
        return redirect('my-measurements')

    return render(request, 'delete_measurement.html', {'measurement': measurement})