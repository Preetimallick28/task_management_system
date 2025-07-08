from django.shortcuts import render , redirect
from base.models import add , HistoryModel , CompleteModel
# Create your views here.
def home(request):
    data=add.objects.all()
    return render(request,'home.html',{'data':data})

def details(request,pk):
    details_read = add.objects.get(id=pk)
    return render(request,'details_page.html',{'details_read':details_read})

def add_task(request):
    if request.method == 'POST':
        title_data = request.POST['title']
        desc_data = request.POST['desc']
        print(title_data,desc_data)
        add.objects.create(
            title = title_data,
            desc = desc_data
        )
        return redirect('home')
    return render(request,'add.html')

def update_task(request,pk):
    data = add.objects.get(id=pk)
    if request.method == 'POST':
        title_Data = request.POST['title']
        desc_Data = request.POST['desc']

        # override
        # student.sname - old data
        # name_Data - new data
        data.title = title_Data  
        data.desc = desc_Data
        data.save()
        return redirect('home')

    return render(request,'update.html',{'data':data})

def confirm_del(request,pk):
    task=add.objects.get(id=pk)
    return render(request,'confirm_del.html',{'task':task})



def delete_(request,pk):
    student = add.objects.get(id=pk)
    HistoryModel.objects.create(title=student.title,desc=student.desc)
    student.delete()

    return redirect('home')

def history(request):
    history_data = HistoryModel.objects.all()
    return render(request,'history.html',{'historydata':history_data})

def restore_all(request):
    restore_all_task = HistoryModel.objects.all()
    for i in restore_all_task:
        
        add.objects.create(
            title = i.title,
            desc = i.desc
        )
    restore_all_task.delete()
    return redirect('home')

def restore_task(request,pk):
    restore_task = HistoryModel.objects.get(id=pk)
    add.objects.create(
        title = restore_task.title,
        desc = restore_task.desc
    )
    restore_task.delete()
    return redirect('home')

def clear_all(request):
    clear_all_task = HistoryModel.objects.all()
    clear_all_task.delete()
    return redirect('home')

def delete_task(request,pk):
    delete_task = HistoryModel.objects.get(id=pk)
    delete_task.delete()

    return redirect('history')

def completed(request,pk):
    complete_task = add.objects.get(id=pk)
    CompleteModel.objects.create(
        title = complete_task.title,
        desc = complete_task.desc
    )
    complete_task.delete()
    return redirect('complete_task')

def complete_task(request):
    complete_task = CompleteModel.objects.all()
    return render(request,'complete_task.html',{'complete_task':complete_task})
