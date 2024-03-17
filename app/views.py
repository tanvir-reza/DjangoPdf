from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
from django.shortcuts import redirect
import csv  
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
# Create your views here.
def index(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request,'index.html',context=context)

def PrintPdf(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    html_string = render_to_string('pdf.html', context)

    # Create a WeasyPrint HTML object
    html = HTML(string=html_string)

    # Generate the PDF
    pdf_file = html.write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="students.pdf"'

    return response

def exportCSV(request):
    Stds = Student.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID','Name','Email','Phone'])
    for student in Stds:
        writer.writerow([student.id,student.name,student.email,student.phone])
    return response

def InsertStudentFromCSV(request):
    if request.method == 'POST' and request.FILES['myfile']:
        print('HI') 
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        with open('media/'+filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                _, created = Student.objects.get_or_create(
                    name=row[0],
                    email=row[1],
                    phone=row[2],
                    age = row[3],
                    address = row[4]
                )
        if filename:
            print('File Name:',filename)
            fs.delete(filename)
        
        return HttpResponse('File Uploaded Successfully')
    else:
        return redirect('Index')

