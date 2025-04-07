from django.shortcuts import render
# Create your views here.
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MSEMark, StudentProfile
from .forms import ExcelUploadForm
from django.contrib.auth.decorators import login_required, user_passes_test

# You can add a better check here to allow only teachers
def is_teacher(user):
    return user.is_staff

@login_required
@user_passes_test(is_teacher)
def upload_mse_marks(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                df = pd.read_excel(request.FILES['file'])
                df.columns = df.columns.str.strip()  # 👈 This line removes extra spaces
                for _, row in df.iterrows():
                    roll_no = row['Roll Number']
                    name = row['Name']  # 👈 used only for display
                    subject = row['Subject']
                    marks = row['Marks']
                    exam_type = row['Exam Type']

                    try:
                        student = StudentProfile.objects.get(roll_number=roll_no)
                        if not student.user.first_name:
                            student.user.first_name = name
                            student.user.save()
                        mse_mark, created = MSEMark.objects.update_or_create(
                        student=student,
                        subject=subject,
                        exam_type=exam_type,
                        defaults={'marks': marks}
                    )
                    except StudentProfile.DoesNotExist:
                        continue  # You could log this too
                messages.success(request, "MSE marks uploaded successfully!")
                return redirect('upload_mse_marks')
            except Exception as e:
                messages.error(request, f"Upload failed: {e}")
    else:
        form = ExcelUploadForm()
    return render(request, 'upload_marks.html', {'form': form})


#Now for students profile

@login_required
def my_marks(request):
    try:
        student = StudentProfile.objects.get(user=request.user)
        marks = MSEMark.objects.filter(student=student)
    except StudentProfile.DoesNotExist:
        student = None
        marks = []

    return render(request, 'my_marks.html', {
        'student': student,
        'marks': marks
    })
