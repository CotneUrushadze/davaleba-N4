from django.shortcuts import render
import random

def get_random_students():
    myList = []  
    for i in range(100):
        name = 'cotne'
        surname = 'urushadze'
        gpa = round(random.uniform(1.0, 4.0), 2)
        course = random.randint(1, 4)
        
        student = {
            "name" : name, 
            "surname" : surname,
            "gpa" : gpa,
            "course" : course
        }
        
        myList.append(student)  
    return myList   


        
def main_page_view(request):
    list = get_random_students()
    context = random.choice(list)
    return render(request, 'main_page.html', {'student': context})


def students_page_view(request):
    context = get_random_students()
    return render(request, 'students_page.html', {'students': context})