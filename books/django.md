
frontier



https://youtu.be/px9HonWy_-4
https://youtu.be/cZfynVKMQ3Q
mohamedhegazy
geohistory010


gunicorn -b 0.0.0.0:8000 project.wsgi
## Admin info :
username : admin
password : rtgomTYHRV4%withALLAH010951@#*&631&#WE84h8%$#@@@#r

#### platrain-v2

admin
admin123456

drhebagamal
heba234567

 drwassam
Wassam123456

drghada
ghada123456

## convert md to docs:

```
Enter: pandoc -o output.docx -f markdown -t docx filename.md
```
 
## preparing django project:

1. to know python libraries you installed
   pip list

2. installing virtualenv:
   pip install virtualenv
3. creating virtualenv:
   virtualenv -p python3.8 dj4

4. cd dj4/

5. activate the virtualenv:
   source bin/activate

6. installing django:
   pip install django

7. if you need to clone a repo here , do it

   git clone ..........

8. cd reponame

9. making the src folder in dj4 :
   mkdir src

10. cd src

11. starting the project :
      django-admin startproject project .

12. runnig server :
       python manage.py runserver

13. to fix migrate error :
        python manage.py migrate

14. to run the page:
        http://127.0.0.1:8000/

15. to get in admin page :
        http://127.0.0.1:8000/admin

16. creating superuser with username & password:
        python manage.py createsuperuser
* note : if you need to change password of one user :
pythonmanage.py changepassword admin (admin is the user name)

17. to start new app :
        django-admin startapp post  ( post is the name of the app)

18. after making database for the app you need to migrate these updates :
        python manage.py makemigrations
        python manage.py migrate
--------
### django shell
if you need to apply something using django shell :
		python manage.py shell
		then do something like : 
			from tasks.models import Task    => then click enter
			Task.objects.create(title="first task")
-----------

## import :

* *from* django.contrib.auth.models *import* User
* from django.db **import** models
* from django.utils import timezone
* import datetime
* from django.shortcuts **import** render 
* from django.shortcuts import get_object_or_404 ,render
* from django.http import HttpResponse
* *from* django.http *import* HttpResponseRedirect
* from .models import Post
* from django.urls import path
* *from* django.db.models *import* Count
* from django import forms
* from django.contrib.auth.models import User
* from crispy_forms.helper import FormHelper
* from crispy_forms.layout import Submit
* *from* django.shortcuts *import* render, redirect, get_object_or_404
* *from* .forms *import* ClientForm, OperationForm
* *from* django.contrib.auth.decorators *import* login_required
* *from* django.contrib *import* messages
* *from* django.contrib.auth *import* authenticate, login, logout
* from django.views.generic import ListView, CreateView, UpdateView, DeleteView
* from django.urls import reverse_lazy
* from django.db.models import Q

----------

## HttpResponse :

### HTTP response error messages :
```

* HttpResponseNotModified  ==> a page hasn't been modified since the user's last request (status code 304).
* HttpResponseBadRequest  ==>  400 status code.
* HttpResponseNotFound  ==>  404 status code.
* HttpResponseNotAllowed  ==>  410 status code.
* HttpResponseServerError  ==> 500 status code.

```python
# ex :
from django.http import HttpResponse
def test(request):
	return HttpResponse('<h1>hi there</h1>')
# ex :
from django.shortcuts import render  
from django.http import HttpResponse, HttpResponseNotFound  
def index(request):  
    a = 1  
    if a:  
        return HttpResponseNotFound('<h1>Page not found</h1>')  
    else:  
        return HttpResponse('<h1>Page was found</h1>')
```

---

## require_http_methods :

```python
from django.views.decorators.http import require_http_methods  
@require_http_methods(["GET"])  
def show(request):  
    return HttpResponse('<h1>This is Http GET request.</h1>')  
```

---

## models :

```python
from django.db import models

types=[
    ('student','student'),
    ('doctor','doctor'),
]

class Property(models.Model):
id = models.CharField(max_length=10,primary_key=True) # to use your own pk
    owner= models.ForeignKey(User,related_name='property_owner',on_delete=models.CASCADE,queryset = User.objects.all())
    # on_delete types : https://www.javatpoint.com/django-on_delete
    name = models.CharField(max_length=100,verbose_name='property_name') # property_name 		will appear in admin pannel not title
    image =models.ImageField(upload_to='property/')
    file = image =models.FileField(upload_to='property/')
    price = models.DecimalField(max_digits=5,decimal_places=2,default=10.0) # float
	created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    #created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=2000)
    type = models.CharField(choices=types ,max_length=50)
    quantity = models.PositiveSmallIntegerField() # no negative number for quantity
    class Meta:
        verbose_name_plural = 'MyPosts' # MyPosts is the name that will be appear in the 				admin pannel(django by default takes the table name and add s to it )
    class Meta:
        ordering = ['created_at']
        ordering = ['-created_at'] # - means descend
    def __str__(self):
        return self.name
---------------------------------------
class Quiz(models.Model):
    number_of_questions = models.IntegerField()
    def get_questions(self):
        return self.question_set.all()[:self.number_of_questions] # question is the name of table Question that related to the table Quiz (get questions belomg to this quiz)
```

## choices :

```python
types=[
    ('student','student'),
    ('doctor','doctor'),
]

MEDIA_CHOICES = [
    ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
    ),
    ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
    ),
    ('unknown', 'Unknown'),
]

    type = models.CharField(choices=types ,max_length=50)
```

---------
## Meta :

```python

class Property(models.Model):
    name = models.CharField(max_length=100,verbose_name='property_name') # 
    class Meta:
        verbose_name_plural = 'MyPosts'
        ordering = ['-created_at'] 
        db_table = 'MyPosts'
        indexes = [
        models.Index(fields=['last_name','first_name'])
        ]
# for more Meta options search for django Meta
```

---

## admin customize:
* register model 

```python
from django.contrib import admin
from .models import Post
class PostAdmin(admin.ModelAdmin):
	fields = ['name', 'category', 'sub_category', 'price', 'description']

    list_display = ['image','name', 'category', 'sub_category', 'price','price_status']

	list_display_links = ['image','name']
	list_display_links =None # to prevent all fields from being links
    search_fields = ['name__startwith', 'description'] # startwith means search for the items(products) where the name starts with these letters.

	ordering = ['name','category']

    list_per_page = 10

    list_filter = ['category','sub_category']

    def image(self,obj):

        product_image = '/static/img/product_avatar.png'

        if obj.mainimage() != None:

            product_image = obj.mainimage().image.url

        return format_html(f'<img style="width:50px;height:50px;border-radius: 50%;object-fit: cover;" class="" src="{product_image}" alt="no image">')
admin.site.register(Post, PostAdmin)


	@admin.display(ordering='price') # means ordering of the next function(extra column) will depend on price column
	def price_status(self,obj): # don't forget to put price_status in list_display
		if obj.price <1000 :
			return "cheap"
		else:
			return "expensive"

```

* get number of products that this category contains and make it a link (when this link is clicked it will be reversed to the page ofproducts filtered by this category):
**for mor info go to mosh cource => part 1 =>admin site =>video 8**
```django
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name','product_number']

    list_display_links =None

    list_editable = ['name']

    def product_number(self,obj):

        return format_html('<a href="http://127.0.0.1:8000/admin/products/product/?category__id__exact={}">{}</a>',obj.id,obj.product_set.all().count())

admin.site.register(Category,CategoryAdmin)
```
* show table columns in related table admin :(like images for every product):

```django
class ProductImageAdmin(admin.StackedInline):

    model = ProductImage

class ProductAdmin(admin.ModelAdmin):

    inlines = [ProductImageAdmin]

    class Meta:

        model = Product

admin.site.register(Product,ProductAdmin)

@admin.register(ProductImage)

class ProductImageAdmin(admin.ModelAdmin):

    pass

admin.site.unregister(ProductImage)
```
* un register model 
``` django
#ex:
from django.contrib.auth.models import Group
admin.site.unregister(Group)
#ex:
from social_django.models import Association, Nonce, UserSocialAuth
admin.site.unregister(Association)

admin.site.unregister(Nonce)

admin.site.unregister(UserSocialAuth)
```
* change site header :
```django
admin.site.site_header = "hhhhh"
```
* change site title:
```django
admin.site.site_title = "hhhhh"
```
* show average column 

```python

from django.contrib import admin
from .models import Person
class PresonAdmin(admin.ModelAdmin):
    list_display = ['name', 'Average'] 
    def showaverage(self, obj):
	    from django.db.models import Avg
	    result = 

```

* in models.py :
```django
    class Meta:
	    verbose_name_plural = 'MyPosts'
        ordering = ['created_at']
        ordering = ['-created_at']
```

## add form style to admin form :

``` django
from .models import sizes_choices

from django import forms

class ProductAvailabilityForm(forms.ModelForm):

size = forms.ChoiceField(

label = 'Size',

choices = sizes_choices,

initial = 's',

widget = forms.RadioSelect,

)

class Meta:

model = ProductAvailability

fields = '__all__'

class ProductAvailabilityAdmin(admin.ModelAdmin):

form = ProductAvailabilityForm

admin.site.register(ProductAvailability,ProductAvailabilityAdmin)
```

## customize any page in the admin :
https://realpython.com/customize-django-admin-python/#overriding-django-admin-templates

https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#admin-overriding-templates

* this image for help :
	![[Screenshot from 2022-10-20 22-34-15.png]]
## apply js to djanago admin:

https://stackoverflow.com/questions/16014719/adding-a-jquery-script-to-the-django-admin-interface

## theme :
https://www.dothedev.com/blog/django-admin-change-color/
-----

## urls :

* project urls.py :

  ```python
  from django.urls import path , include
  from django.contrib import admin 
  urlpatterns=[
  	path('admin/',admin.site.urls),
  	path('blog/' , include('blog.urls',namespace='blog')) ,
  ]
  ```

	* app url.py :

  ```python
  from django.urls import path
  from . import views 
  app_name = 'blog'
  urlpatterns = [
      path('',views.post_list,name = 'all_posts')
  ]
  ```

-----------

## views :

```python
from .models import Post 
def post_list(request):
    last_post= Post.objects.last()
    first_post= Post.objects.first()
    all_posts = Client.objects.values_list('id', 'title') # get only id ,title from every obj
    all_posts= Post.objects.all().order_by('lastname')
    all_posts= Post.objects.all().order_by('lastname', '-id')
    all_posts= Post.objects.all().str(count())
    all_posts= Post.objects.all().exclude(price=10)
    all_posts= Post.objects.filter(type='student')
    all_posts= Post.objects.filter(price__exact=50)
    all_posts= Post.objects.filter(price__in=[50,100])#price is 50 or 100
    all_posts= Post.objects.filter(price__range=(10,100))#price betwwen 10 and 100
    all_posts= Post.objects.filter(name__contains='ah')
    all_posts= Post.objects.filter(name__icontains='ah')
    posts = Post.objects.filter(lastname='Refsnes', price=2)
    # .filter(firstname__startswith='L')
    # .filter(firstname__endswith='s')
    # .filter(firstname__iendswith='s')
    # .filter(firstname__exact='Emil')  Get all records where firstname is exactly "Emil"
    # .filter(firstname__iexact='Emil')  
    # .filter(firstname__in=['Tobias', 'Linus', 'John'])
    # .filter(firstname__isnull=True)
    # .filter(id__gt=3)  greater than
    # .filter(id__gte=3) greater than or equal
    # .filter(id__lt=3)  less than
    # .filter(id__lte=3) less than or equal
    # .filter(id__range=(2, 4))
    # .filter(date_added__date='2-5-2022')
    # .filter(date_added__day='2')
    # .filter(date_added__month='5')
    # time 
    # weak
    # year
    # hour
    # minute
    # quarter (1-4)
    # second
    # other at :https://www.w3schools.com/django/django_queryset_filter.php
    return render(request,'post/all_posts.html' {'all_posts':all_posts})
# or
	return render(request,'post/posts.html' {'posts':all_posts.filter(name__contains='ah')})
# or 
	context = {
        'post':post,
    }
    return render(request,'post/all_posts.html',context)	

queryset = User.objects.filter(
    first_name__startswith='R'
).values('first_name', 'last_name')

def subject(request,id):
    subject=Subject.objects.get(id=id)
    subject=get_object_or_404(Subject,pk=id) 
    quizes = subject.quiz_set.all() # quiz is name of Quiz (related to Subject model) model but in lowercase 
    quizes = subject.subquizes.all() # subquizes is relationship name between Subject and Quiz model
    subject.title = 'ahmed'  # update
    subject.save()
###################################################
# create a new object that related with another model in relasionship
# if relationship is ManyToMany :
def lecture(request,id):
    lecture=Lecture.objects.get(id=id)
    file = File.objects.create(file=file)
    lecture.lecturefiles.add(file) # lecturefiles is relationship name between Lecture and File model
```

* Count :

  ``` python
  # models :
  class Client(models.Model):
      name = models.CharField(max_length=200,null=True,blank=True)
  
  class DailyOperation(models.Model):
      client = models.ForeignKey(Client, on_delete=models.CASCADE)
      one_kilo_price = models.FloatField()
  # views :
  from django.db.models import Count
  def clients(request):
      q = Client.objects.annotate(Count('dailyoperation'))
      print(q[0].name)
      print(q[0].dailyoperation__count) # number of dailyoperation that related to Client number 0
  # or views :
  from django.db.models import Count
  def clients(request):
      q = Client.objects.annotate(number_of_entries = Count('dailyoperation'))
  	print(q[0].number_of_entries)
  	
  # dailyoperation is the related table name in small or relation name .
  ```
  
  -----

## Q filter :

```python
  

class Topic(models.Model):

    name = models.CharField(max_length=200)


class Room(models.Model):

    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=200)

    description = models.TextField(null=True, blank=True)

    participants = models.ManyToManyField(

        User, related_name='participants', blank=True)

    updated = models.DateTimeField(auto_now=True)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ['-updated', '-created']

#########################################################
from django.db.models import Q
def home(request):

    q = request.GET.get('q') if request.GET.get('q') != None else ''

  

    rooms = Room.objects.filter(

        Q(topic__name__icontains=q) |

        Q(name__icontains=q) |

        Q(description__icontains=q)

    )

```

-----
## related_name & set :
EX : (related_name)
```python
class Quiz(models.Model):
    number_of_questions = models.IntegerField()
	# questions = ...   # django creates this field with the related_name you put in the child table(Question) for the ralation between Quiz and Question 

    def get_questions(self):
        return self.questions.all()[:self.number_of_questions]
        # questions is the related_name
class Question(models.Model):
	text = models.CharField() 
	quiz = models.ForignKey(Quiz,on_delete.CASCADE,related_name = 'questions')
```
Ex : (set)
```python
class Quiz(models.Model):
    number_of_questions = models.IntegerField()
	# question_set = ...   # django creates this field automaticaly for the ralation between Quiz and Question 

    def get_questions(self):
        return self.question_set.all()[:self.number_of_questions]
        # question_set is the default related_name 
class Question(models.Model):
	text = models.CharField() 
	quiz = models.ForignKey(Quiz,on_delete.CASCADE)
```
---
## template :

* where :

  1) in TEMPLATES in settings.py : 'DIRS': [BASE_DIR/'templates'],

  2) every app has folder templates/app-name then put html pages

  3) make general folder templates besides apps called templates and put general html files like base.html , nav.html

     ```python
     # base.html
     {% load static %}
     <!DOCTYPE html>
     <html lang="en">
       <head>
         <meta charset="UTF-8" />
         <meta http-equiv="X-UA-Compatible" content="IE=edge" />
         <meta name="viewport" content="width=device-width, initial-scale=1.0" />
         <title>{% block title %}{% endblock title %}</title>
         {% comment %} <link rel="icon" type="image/x-icon" href="{% static 'imgs/logo.ico' %}"> {% endcomment %}
         <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}" />
         <link rel="stylesheet" href="{% static 'css/bootstrap.min.css.map' %}" />
         <link rel="stylesheet" href="{% static 'css/all.min.css' %}" />
         <link rel="stylesheet" href="{% static 'css/main.css' %}" />
         <link rel="preconnect" href="https://fonts.googleapis.com">
         <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
         <link href="https://fonts.googleapis.com/css2?family=Dancing+Script&family=Pacifico&family=Roboto:ital,wght@0,100;0,300;0,400;1,100;1,300&family=Sansita+Swashed:wght@300&display=swap" rel="stylesheet">
     
       </head>
       <body>
         {% include "navbar.html" %}
     
         <script src="https://cdnjs.cloudflare.com/ajax/libs/sweetalert/2.1.2/sweetalert.min.js"> </script>
     
         {% if messages %}
             {% for message in messages %}
     
     
             {% if message.tags == 'info' %}
             <script>
               swal("done!", "{{message}}!", "success");
             </script>
             {% endif %}
             {% if message.tags == 'error' %}
             <script>
               swal("Error!", "{{message}}!", "error");
             </script>
             {% endif %}
             {% endfor %}
         {% endif %}
     
           <!-- Logout Modal -->
       <div class="modal" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
         <div class="modal-dialog">
         <div class="modal-content">
             <div class="modal-header">
             <h5 class="modal-title" id="exampleModalLabel">Logout</h5>
             <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
             </div>
             <div class="modal-body">
             are you sure you need to logout ?
             </div>
             <div class="modal-footer">
             <a class="btn btn-dark btn-sm" data-bs-dismiss="modal">Cancel</a>
             <a href="{% url 'accounts:logout' %}" class="btn btn-dark ">Logout</a>
             </div>
         </div>
         </div>
     </div>
     <!-- End Logout Modal -->
     
     
     
     
     {% block content %}
       
     {% endblock content %}
     
         <!-- js -->
         <script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
         <script src="{% static 'js/all.min.js' %}"></script>
         <script src="{% static 'js/script.js' %}"></script>
     
         
       </body>
     </html>
     
     ```

     ```python
     # nav.html
     {% load static %}
     <nav class="mb-5 navbar navbar-expand-lg sticky-top nav-color">
         <div class="container">
             {% if request.user.is_authenticated %}
             <a class="navbar-brand" href="{% url 'accounts:updateuser' %}">
                 <img class="profile-image" src="{{request.user.image.url}}" alt="" />
             </a>
             {% endif %}
             <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#main"
                 aria-controls="main" aria-expanded="false" aria-label="Toggle navigation">
                 <i class="fa-solid fa-bars"></i>
             </button>
             <div class="collapse navbar-collapse" id="main">
                 <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                   {% if request.user.is_authenticated %}
                     <li class="nav-item">
                         <a class="nav-link p-2 p-lg-3 {% if request.path == '/' %}active{% endif %}" aria-current="page" href="/">Home</a>
                     </li>
                     <li class="nav-item">
                         <a class="nav-link p-2 p-lg-3 {% if request.path == '/studyclass/subjects/' %}active{% endif %}" href="{% url 'studyclass:subjects' %}">Subjects</a>
                     </li>
                     <li class="nav-item">
                         <a class="nav-link p-2 p-lg-3 {% if request.path == '/emptyhall/' %}active{% endif %}" href="{% url 'emptyhall:hallfrontend' %}">halls</a>
                     </li>
                     {% endif %}
                     
                     {% if request.user.type == 'admin' %}
                     <li class="nav-item">
                         <a class="nav-link p-2 p-lg-3 {% if request.path == '/settings/' %}active{% endif %}" href="{% url 'settings:settings' %}">Settings</a>
                     </li>
                     {% endif %}  
                 </ul>
                 {% if request.user.is_authenticated %}
                 <a class="btn rounded-pill main-btn" data-bs-toggle="modal" data-bs-target="#exampleModal">Logout</a>
                 {% else %}
                 <a class="btn rounded-pill main-btn" href="{% url 'accounts:login' %}">Login</a>
                 
                 {% endif %}
                 
             </div>
     
     
         </div>
     </nav>
     ```

* call extended in html files :

  ```python
  {% extends 'base.html' %}
  {% load static %}
  {% load crispy_forms_tags %}
  {% block content %}
  
  
  {% endblock content %}
  ```
  
  
  
* html :

  ```python
  {% csrf_token %} 
  ----------
  {% for post in all_posts %}
      {{post}}
  {% empty %}
  	<p>no posts yet</P>
  {% endfor %}
  ----------------------------------------
  {% if request.user.is_authenticated %}
  Hello, {{ user.username }}
  {% else %}
  {{something}}
  {% endif %}
  -----------------------------------------
  {{operation.date_added|date:'m / j'}}
  --------------------------------------
  <h1>
  {% firstof x y z %} # Return the first of the three variables (x, y, z) whose value is not empty or false.
  </h1>
  ------------------------------------
  # autoescape ==> used mostly to prevent js commands to written in forms 
  # off => deal with programing keywords as normal words
  # on => execute programing keywords as should be in this programming lang.
  {% autoescape off %} 
    <h1>ahmed</h1>  # it prints <h1>ahmed</h1> , but if on , it prints ahmed
  {% endautoescape %}
  ------------------------------------
  {% block title %}
    platrain
  {% endblock %}
  ---------------------------------
  # truncate 
  {{propeerty.description|truncatewords:5}}
  {{propeerty.description|truncatechars:5}}
  # or in html directly
  <p class= "text-truncate"> {{propeerty.description}}</p>
  ------------------------------------------------------------------------
  # cycle : 
  <ul>
  {% for x in fruits %} #Add a new color for each iteration in a for loop
    <li style='color:{% cycle 'red' 'green' 'blue' 'pink' %}'>
      {{ x }}
    </li>
  {% endfor %}
  </ul>
  -------------------------------------
  # filter :
  {% filter upper %}
    <p>Have a great day!</p> #  Have a great day will printed in upper case
  {% endfilter %}
  
  # filter keywords : https://www.w3schools.com/django/ref_tags_filter.php
  -----------------------------------------------
  {{all_posts|slice:':5'}} # get first five elements (objects) on all_posts lost
  {% for post in all_posts %} 
      {{post|capfirst}}  # this capitalize the first letter of post output
      {{post|title}}  # this capitalize the first letter of post output
      {{post|default:'notfound'}}
      {{post|slice:':5'}} # get only first five letters 
      {{post|length}} # counts the length of this output
      {{post|add:'issa'}} # add issa after output
      {{post|cut:' '}} # remove the space from the output
      {{post.full_name|upper }} #this capitalize the first letter of the all full_name
      {{post.created_at|date:'F j Y'}}
      {{post|filesizeformat}} # suppose that post return the size of a file in kilopytes and need to transform it to giga or the nearst thing 
      {{post.created_at|date:'F j Y'}}# 
  {% endfor %}
  ----------------------------------------------------
  # forloop.first (do something if while the first iteration in the loop)
  <div class = "aa {% if forloop.first %} bb {% endif %}">
  </div>
----------------
{% if forloop.counter != 1 %}
  -------------------------------------------
  # request.path

request.path # gets path without parameters
request.get_full_path # gets path with parameters 
# shop/?category=children&page=2

  <li 
      {% if '/' == request.path %}
      # {% if 'products' in request.path %}
      class="nav-item active"
      {% else %}
      class="nav-item"
      {% endif %}
   >
         <a class="nav-link" aria-current="page" href="{% url 'home' %}">Home</a>
  </li>

----------------------------------------------------------
# math basics in template :

{% for student in students %}

<li>

<em>{{ student.name }}:</em> {{ student.score }}/{{ max_score }}

</li>

{% endfor %}

------------------------------------------------------------
# define variable in template :
# ex1:
{% with x=3 y=2 %}

{{x}}

{% endwith %}

# ex2:
{% with total=business.employees.count %}
    {{ total }} employee{{ total|pluralize }}
{% endwith %}
  ```

* urls :

  ```django
  href="{% url 'quiz:addquizquestions' subject.id quiz.id %}"
  {% url 'post_detai' id=id %}
  style="background-image: url({% static '/images/bg_5.jpg' %})
  {{property.image.url}}
  {{lecture.file.url}}
  ```
  
  

---

## static & media files:

* static folder :

  make a folder called static besides apps then put these on it :

  css

  js

  imgs

  fon

* static configuration :

in settings :

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
    '/var/www/static/',
]
MEDIA_URL = '/media/'
MEDIA_ROOT=BASE_DIR / "media"
```

then go to urls.py of your project to serve static files by this importing:

```python
from django.conf import settings
from django.conf.urls.static import static
```

also in the urls.py file put these after the list urlpatterns

```python
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

***note*** in the final of settings file of the main project you will find this link:

https://docs.djangoproject.com/en/3.2/howto/static-files/

that guids you in details to these things from documentation

---

## date & time :

```python
{{operation.date_added|date:'m / j'}}
------------------------------------------
import datetime 
now = datetime.datetime.now()  
------------------------------------------------
import calendar
def day(self):
        day = calendar.day_name[self.date_added.weekday()]
        if day == 'Saturday':
            day = 'السبت'
        elif day == 'Sunday':
            day = 'الاحد'
        elif day == 'Monday':
            day = 'الاثنين'
        elif day =='Tuesday':
            day = 'الثلاثاء'
        elif day == 'Wednesday':
            day = 'الاربعاء'
        elif day == 'Thursday':
            day = 'الخميس'
        elif day == 'Friday':
            day = 'الجمعة'

        return day
-----------------------------------
from datetime import timedelta, date
class Weak(models.Model):
    start = models.DateTimeField(auto_now=True)
    def end(self):
        return self.start + timedelta(days=6)
-----------------------------------------
from django.utils import timezone
class Quiz(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    def quiz_status(self):
        if self.end >= timezone.now() and self.start <= timezone.now() :
            status = 'active'
        elif self.start > timezone.now():
            status = 'soon'
        elif self.end < timezone.now():
            status = 'finished'
        return status
------------------------------------------
from django.utils import timezone
def home(request):
    now= timezone.now()
    offers = Discount.objects.filter(discount_end__gte = now , discount_start__lte = now)

```

----

Forms :

* function crud with html :

  ```python
  # models :
  class Client(models.Model):
      name = models.CharField(max_length=200,null=True,blank=True)
      one_kilo_price = models.FloatField(default=0.0)
      date_added = models.DateTimeField(auto_now=True)
  class Weak(models.Model):
      start = models.DateTimeField(auto_now=True)
      def end(self):
          return self.start + timedelta(days=6)
      class Meta:
          ordering = ['-start']
  class DailyOperation(models.Model):
      client = models.ForeignKey(Client, on_delete=models.CASCADE)
      weak = models.ForeignKey(Weak, on_delete=models.CASCADE)
      date_added = models.DateField(auto_now=True)
      kilos_of_milk = models.FloatField()
  # views :
  @login_required
  def dailyoperations(request,client_pk):
      client = get_object_or_404(Client, id=client_pk)
      weak = Weak.objects.first()
      operations = DailyOperation.objects.filter(client=client, weak=weak) 
      l = []
      weaktotalprice = 0
      onetimeprice = 0
      for operation in operations :
          onetimeprice = operation.kilos_of_milk * operation.one_kilo_price
          l.append(onetimeprice)
      weaktotalprice = sum(l)
      context = {
          'operations' : operations,
          'weaktotalprice' : weaktotalprice,
          'client': client,
          'weak': weak,
      }
      return render(request,'milk/operations.html',context)
  
  def addnewoperation(request,client_pk, weak_pk):
      client = get_object_or_404(Client, id=client_pk)
      weak = Weak.objects.first()
      if request.method == 'POST':
          kilos_of_milk = request.POST.get('numberofkilos')
          data = DailyOperation(client=client, weak=weak, one_kilo_price = client.one_kilo_price, kilos_of_milk=kilos_of_milk)
          data.save()
          messages.info(request, 'تم اضافة عملية جديدة')
          return redirect('milk:clients')
      context = {
      'client': client,
      'weak': weak,
  	}
      return render(request, 'milk/add_new_operation.html', context)
  
  @login_required
  def editoperation(request,operation_pk):
      operation = get_object_or_404(DailyOperation, id=operation_pk)
      if request.method == 'POST':
          kilos_of_milk = request.POST.get('numberofkilos')
          if form.is_valid():
              operation.kilos_of_milk = kilos_of_milk
              operation.save()
              messages.info(request, 'تم تعديل العملية')
              return redirect('milk:clients')
      else:
          messages.info(request, 'تأكد من صحة البيانات')
          return redirect('milk:editoperation',subject_pk=subject.id, quiz_pk=quiz.id)
          
  
      context = {
  		'form': form,
  		'operation': operation,
  	}
      return render(request, 'milk/edit_operation.html', context)
  
  @login_required
  def deleteoperation(request, operation_pk):
      operation = get_object_or_404(DailyOperation, id=operation_pk)
      operation.delete()
      return redirect('milk:clients')
  
  # urls :
  path('operations/<str:client_pk>/', views.dailyoperations, name="operations"),
  path('operations/<str:client_pk>/addnew', views.addnewoperation, name="addnewoperation"),
  path('operations/<str:operation_pk>/edit', views.editoperation, name="editoperation"),
  path('operations/<str:operation_pk>/deleteoperation', views.deleteoperation, name="deleteoperation"),
      
  # templates :
  # all operations and delete :
  {% for operation in operations %}
      <a class="link-change">{{operation.date_added|date:'m / j'}}</a>
       <a href="{% url 'milk:editoperation' operation.id %}" class="btn btn-primary btn-block btn-sm m-1"><i class="fa-solid fa-pencil"></i></a>
      <a data-bs-toggle="modal" data-bs-target="#deleteModal{{operation.id}}" class="btn btn-danger btn-block btn-sm m-1"><i class="fa-solid fa-trash"></i></a>
   
  <!-- Delete Modal -->
   <div class="modal" id="deleteModal{{operation.id}}" tabindex="-1" aria-labelledby="deleteModalLabel{{operation.id}}" aria-hidden="true">
   <div class="modal-dialog">
   <div class="modal-content">
   <div class="modal-header">
   <h5 class="modal-title" id="deleteModalLabel{{operation.id}}">DELETE!</h5>
   <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
  </div>
  <div class="modal-body">هل تريد حذف هذا العنص</div>
  <div class="modal-footer"><a class="btn btn-dark btn-sm" data-bs-dismiss="modal">الغاء</a>
  <a href="{% url 'milk:deleteoperation' operation.id %}" class="btn btn-dark ">حذف</a>                             
  </div>
  </div>
  </div>
   </div>
  <!-- End Delete Modal -->
  
  {% endfor %}
  # add operation and edit:
  
  <div class="container-fluid centerize">
    <p class="font-monospace fs-1">  اضافة عملية جديدة</p>
    <div class="login-div-color">
      <form action="" method="POST" enctype="multipart/form-data">
        {% csrf_token %}
          <br>
          <label for="numberofkilos">عدد الكيلوات</label>
          <br>
          <input id="numberofkilos" type="text" name='numberofkilos'>
          <br>
          <br>
          <label for="pricetext">ادخل سعر الكيلو</label>
          <br>
          <input id="pricetext" type="text" name='pricetext'>
          <br>
          <label for="pricechoice">او اختار سعر الكيلو</label>
          <br>
          <select class="form-control" name="pricechoice" value="pricechoice">
              <option></option>
              {% for price in prices %}
                  <option>
                      {{price.one_kilo_price}}
                  </option>
              {% endfor %}
          </select>
          <br>
          <input type="submit" value='حفظ'>
      </form>
    </div>
  </div>
  
  ```

* function crud with django forms :

  ```python
  # views :
  def addclient(request):
      user = request.user
      if user.username == '' :
          return redirect('milk:login')
      else :
          form = ClientForm()
          if request.method == 'POST':
              form = ClientForm(request.POST)
              if form.is_valid():
                  name = form.cleaned_data.get('name')
                  one_kilo_price = form.cleaned_data.get('one_kilo_price')
                  c = Client.objects.create(name=name,one_kilo_price=one_kilo_price)
                  c.save()
                  messages.info(request, 'تم اضافة عميل جديد')
                  return redirect('milk:clients')
          else:
              form = ClientForm()
  
          context = {
              'form': form,
          }
          return render(request, 'milk/add_client.html', context)
  
  def editoperation(request,operation_pk):
      operation = get_object_or_404(DailyOperation, id=operation_pk)
      if request.method == 'POST':
          form = OperationForm(request.POST,instance=operation)
          if form.is_valid():
              operation.save()
              messages.info(request, 'تم تعديل العملية')
              return redirect('milk:clients')
      else:
          form = OperationForm(instance=operation)
  
      context = {
  		'form': form,
  		'operation': operation,
  	}
      return render(request, 'milk/edit_operation.html', context)
  # forms :
  from django import forms
  from django.contrib.auth.models import User
  from .models import Client, DailyOperation
  from crispy_forms.helper import FormHelper
  from crispy_forms.layout import Submit
  
  class ClientForm(forms.ModelForm):
  	def __init__(self, *args, **kwargs):
  		super().__init__(*args, **kwargs)
  		self.helper = FormHelper(self)
  		self.helper.add_input(Submit('submit', 'حفظ'))
  	name = forms.CharField()
  	class Meta:
  		model = Client
  		fields = ('name','one_kilo_price')
  class OperationForm(forms.ModelForm):
  	def __init__(self, *args, **kwargs):
  		super().__init__(*args, **kwargs)
  		self.helper = FormHelper(self)
  		self.helper.add_input(Submit('submit', 'حفظ'))
  	kilos_of_milk = forms.FloatField()
  	class Meta:
  		model = DailyOperation
  		fields = ('kilos_of_milk',)
  #html :
  {% extends 'base.html' %} 
  {% load static %}
  {% load crispy_forms_tags %}
  {% block content %}
  
  <div class="container-md container-change">
    <p class="font-monospace fs-1 p-change">تعديل بيانات العملية</p>
    <div class="login-div-color">
      <form action="" method="POST" enctype="multipart/form-data">
        {% csrf_token %} 
      {% crispy form %} # or { form.as_p }}
      </form>
    </div>
  </div>
  
  {% endblock content %}
  ```

---

## pass parameter in url :
```html
                <div class="card">

                    <div class="card-header">Categories</div>

                    <ul class="list-group list-group-flush">

                        <li class="list-group-item">

                            <a href="{% url 'usermanager:categorycontent' %}">All</a>

                        </li>

                        {% for category in categories %}

                          <li class="list-group-item">

                            <a

                              href="{% url 'usermanager:categorycontent' %}?category={{ category.name }}"

                              >{{ category.name }}</a

                            >

                          </li>

                        {% endfor %}

                        <a href="{% url 'usermanager:addfile' %}" class="btn btn-dark btn-block btn-sm m-1">Add File</a>

                        <a href="{% url 'usermanager:addlink' %}" class="btn btn-dark btn-block btn-sm m-1">Add Link</a>

                        <a href="{% url 'usermanager:addnote' %}" class="btn btn-dark btn-block btn-sm m-1">Add Note</a>

                    </ul>

                </div>

            </div>
``` 
```python
def categoryContent(request):

    images = []

    images_number = 0

    user = request.user

    category = request.GET.get('category')

    filesize=0

    listsize=[]

    fullsize=0

    if category == None:

        files = File.objects.filter(category__user=user)

        for file in files:

            filesize=int(os.path.basename(str(file.file.size)))

            listsize.append(filesize)

        fullsize=sum(listsize)

        files_number = files.count()

        links = Link.objects.filter(category__user=user)

        links_number = links.count()

        notes = Note.objects.filter(category__user=user)

        notes_number = notes.count()

    else:

        files = File.objects.filter(category__name=category, category__user=user)

        files_number = files.count()

        links = Link.objects.filter(category__name=category, category__user=user)

        links_number = links.count()

        notes = Note.objects.filter(category__name=category, category__user=user)

        notes_number = notes.count()

  

    categories = Category.objects.filter(user=user)
```

-----
## forms.py :



-----

## get_or_create :

```python
def post_detail(request, post_id):
    post, created = Post.objects.get_or_create(pk=post_id)
    print(created)
    return render(request, 'template.html')
```

---

## ForeignKey :

```python
{% for image in object.property_image.all %} # property_image is the related_name
```

----

## ManyToMany :

```python
# models
class Post(models.Model):
    title = models.CharField(max_length=255)
class Category(models.Model):
    title = models.CharField(max_length=255)
    posts = models.ManyToManyField(Post)
###################################################
#views  
category = Category.objects.get(title='django')
category_posts = category.posts.all()
```

```python
# create a new object that related with another model in relasionship
# if relationship is ManyToMany :
def lecture(request,id):
    lecture=Lecture.objects.get(id=id)
    file = File.objects.create(file=file)
    lecture.lecturefiles.add(file) # lecturefiles is relationship name between Lecture and File model
```

```python
# models
import os
class AssignmentFile(models.Model):
	file = models.FileField(upload_to='assignmentfiles/')
	def get_file_name(self):
		return os.path.basename(self.file.name)

class Assignment(models.Model):
    title = models.CharField(max_length=150,null=True,blank=True)
    files = models.ManyToManyField(AssignmentFile)
# views
def newAssignment(request, pk):
	user = request.user
	subject = get_object_or_404(Subject, id=pk)
	assignmentfiles = []
	if user != subject.doctor:
		return HttpResponseForbidden()
	else:
		if request.method == 'POST':
			form = NewAssignmentForm(request.POST, request.FILES)
			if form.is_valid():
				title = form.cleaned_data.get('title')
				files = request.FILES.getlist('files')
				for file in files:
					file_instance = AssignmentFile(file=file, user=user)
					file_instance.save()
					assignmentfiles.append(file_instance)
				a = Assignment.objects.create(title=title, content=content, points=points, due=due, subject=subject ,user=user)
				a.files.set(assignmentfiles)
				a.save()
				return redirect('studyclass:subjectlectures',pk=subject.id)
		else:
			form = NewAssignmentForm()
	context = {
		'form': form,
	}
	return render(request, 'assignment/newassignment.html', context)
#forms
class NewAssignmentForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.add_input(Submit('submit', 'Save'))
	files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
	class Meta:
		model = Assignment
		fields = ('title', 'files')

# html
{% for file in lecture.files.all %}
<a class="lecture-link" href="{{file.file.url}}">{{file.get_file_name}}</a>
{% endfor %}
```



---

## bootstrap with django :

* install :

  pip install django-crispy-forms

  pip install django-crispy-bootstrap5

* in installed apps :

  "crispy_for

--------------
## get file name , type , size

```python
import os

class File(models.Model):

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    file = models.FileField(null=False, blank=False)

    description = models.TextField(null=True, blank=True)

    added = models.DateTimeField(auto_now_add=True)

    def get_file_type(self):

        file_name = os.path.basename(self.file.name)

        if file_name[-5:] in ['.apng','.avif','.jpeg','.jfif','.webp','.tiff'] or file_name[-4:] in ['.gif','.jpg','.pjp','.png','.svg','.tif','.bmp','.ico','.cur']:

            type = 'image'

        else:

            type = 'file'

        return type

    def get_file_name(self):

        return os.path.basename(self.file.name)

    def get_file_size(self):

        size=int(os.path.basename(str(self.file.size)))

        return size

    class Meta:

        verbose_name = 'File'

        verbose_name_plural = 'Files'

  

    def __str__(self):

        return os.path.basename(self.file.name)
```
----
## slug :

```python
# ex :
from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
```

then go to admin.py where you register oyur table and make it like this to make slug be done automatically in admin panel :

```python
from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',) # put all columns you need to appear in the admin panel 
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
```

-----------------

## going to details by clicking the base :

* ### get_absolute_url : and using slug in moving from page to another

انت شغال مثلا فى صفحة الهوم وبتستخدم كلاس معين بتاخد منه البيانات زى ده :

```python
#models.py
from django.urls import reverse
class Post(models.Model):
    title=models.CharField(max_length=150)
    slug = models.SlugField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
	    return reverse('blog:post_detail', kwargs={'slug':self.slug})
    
#####################3
# views.py
class PostList(ListView):
    model = Post
    template_name = "blog/post_list.html"
class PostDetail(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
###################################
# urls.py   of the app
path('',views.PostList.as_view(),name='post_list'),
path('<slug:slug>',views.PostDetail.as_view(),name='post_detail'),
###############################
# html
{{property.get_absolute_url}}
```

* ### the normal way :

```python
{% for post in all posts %}
	{{post.name}}
    <a href ="{% url 'post_detai' id=id %}">details</a>
{% endfor %}
 # post_detai is name of url of detail 
```

-------

## get_context_data :

to override a class based view . 

### example: related cards

suppose we need to show cards related to the current card (related by category for example)

```python
class PropertyDetail(DetailView):
    #getting details of properties
    model= Property
    #getting related by the same category
    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        context["related"] = Property.objects.filter(category=self.get_object().category)[:2]         # result is a list you can loop on it
        return context
########################
# html
{% for property in related %}

{% endfor %}
```

another way to get related cards :

get all properties and make the for loop in html to be like this :

```python
{% for property in properties|slice:":6" %} # it comes with first 6 properties in the database but if you need the last 6 properties added you should make negative ordering to date_added in Propery model. 
```



### another example:

Ex : we show all subjects then we click any subject it takes us to  a page that contains all lectures of this subject

in models.py

```python
class Subject(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    description = models.TextField(max_length=1000)
    doctor_name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Lecture(models.Model):
    name = models.CharField(max_length=150)
    date_added = models.DateTimeField(auto_now=True, auto_now_add=False)
    # = models.DateTimeField(default=timezone.now)# from django.utils import timezone  
    subject_name = models.ForeignKey(Subject, related_name='subject', on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    file = models.FileField(upload_to='media/', null=True, blank=True)
    video = models.CharField(max_length=1000, null=True, blank=True)
    assignment_content = models.TextField(max_length=1000 , null=True)
    assignment_end_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.name
```

in views.py

```python
class SubjectDetail(DetailView):
    model = Subject
    context_object_name = 'lectures'
    template_name = 'subjects/subject_lectures.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lectures"] = Lecture.objects.filter(subject_name=self.get_object().id)
        return context
```

in urls.py of the project

```python
    path('subjects/' ,include('subjects.urls',namespace="subjects")),
```

in urls.py of the app

```python
path("subjects/", SubjectList.as_view(), name="subjects"),
path("lectures/<int:pk>", SubjectDetail.as_view(), name="lectures"),
```

in html file  ( subject_list.html )

```html
{% for subject in subjects %}
             <h4 class="card-title card-h4-change">{{subject.name}}</h4>
             <h5 class="card-h5-change">Dr : <span>{{subject.doctor_name}}</span></h5>       
             <a href="{% url 'subjects:lectures' subject.id %}" </a>
{% endfor %}
```

in html file (  )

```html
{% for lecture in lectures %}
			<h4 class="card-title card-h4-change">{{lecture.name}}</h4>
             <h5 class="card-h5-change">Dr : <span>{{lecture.doctor_name}}</span></h5>
{% endfor %}
```

### another example:

```python
class PostDetail(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["categories"] = Category.objects.all().annotate(post_count=Count('post_category'))
        context["recent_posts"] = Post.objects.all()[:3]
        return context
```

---------

## favicon :

```python
#in main urls :
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
path('favicon.ico/', RedirectView.as_view(url=staticfiles_storage.url('imgs/logo.ico'))),
```

or :

```html
# in base.html
<link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}"/>
```

----

## api :

```

```

--------------

## filter :
```python

class UserList(ListView):

    model = User

    context_object_name = 'users'

    template_name = 'settings/all_users.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        search_input_name = self.request.GET.get('search-area_name') or ''

        search_input_year = self.request.GET.get('search-area_year') or ''

        search_input_department = self.request.GET.get('search-area_department') or ''

        search_input_branch = self.request.GET.get('search-area_branch') or ''

        search_input_type = self.request.GET.get('search-area_type') or ''

        departments = Department.objects.all()

        branches = Branch.objects.all()

        if search_input_name:

            context['users'] = context['users'].filter(

                username__icontains=search_input_name

            )

        if search_input_year:

            context['users'] = context['users'].filter(

                year__icontains=search_input_year

            )

        if search_input_department:

            context['users'] = context['users'].filter(

                department__name=search_input_department

            )

        if search_input_branch:

            context['users'] = context['users'].filter(

                branch__name=search_input_branch

            )

        if search_input_type:

            context['users'] = context['users'].filter(

                type=search_input_type

            )

        context['search_input_name'] = search_input_name

        context['search_input_year'] = search_input_year

        context['search_input_department'] = search_input_department

        context['search_input_branch'] = search_input_branch

        context['search_input_type'] = search_input_type

        context['departments'] = departments

        context['branches'] = branches

        return context
```


-----

## pagination :

### function :

```python
from django.core.paginator import Paginator
def subjects(request):
    #profile = Profile.objects.get(user = request.user)
    subjects = Subject.objects.all()
    paginator = Paginator(subjects, 6)
    page = request.GET.get('page')
    subjects = paginator.get_page(page)
    context = {
        'subjects':subjects,
    }
    return render(request,'studyclass/subjects.html', context)
```

```html
 <!--paginator -->
            <div class="pagination">
                <span class="step-links">
                    {% if subjects.has_previous %}
                        <a href="?page=1">&laquo; first</a>
                        <a href="?page={{ subjects.previous_page_number }}">previous</a>
                    {% endif %}
            
                    <span class="current">
                        Page {{ subjects.number }} of {{ subjects.paginator.num_pages }}.
                    </span>
            
                    {% if subjects.has_next %}
                        <a href="?page={{ subjects.next_page_number }}">next</a>
                        <a href="?page={{ subjects.paginator.num_pages }}">last &raquo;</a>
                    {% endif %}
                </span>
            </div>
            <!--End pagunator -->
```

### class :



----

## DElete modal :

```html
<a class="btn btn-danger btn-sm m-1" data-bs-toggle="modal" data-bs-target="#deleteModal{{subject.id}}">Delete</a>


<!-- Delete Modal -->
    <div class="modal" id="deleteModal{{subject.id}}" tabindex="-1" aria-labelledby="deleteModalLabel{{subject.id}}" aria-hidden="true">
        <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
            <h5 class="modal-title" id="deleteModalLabel{{subject.id}}">Logout</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
            are you sure you need to delete item ?
            </div>
            <div class="modal-footer">
            <a class="btn btn-dark btn-sm" data-bs-dismiss="modal">Cancel</a>
            <a href="/studyclass/deletesubject/{{subject.id}}" class="btn btn-dark ">Delete</a>
            </div>
        </div>
        </div>
    </div>
    <!-- End Delete Modal -->
```



---

## @login_required:

```python
from django.contrib.auth.decorators import login_required
@login_required
def subjects(request):
	pass
```

--------------
## custom form validator :

in form.py :

```python

def three_words(value):

	space_counter=0

	for space in value:

		if space == " ":

			space_counter+=1

	if space_counter <2:

		raise forms.ValidationError("name must contains from 3 words or more")

  

class RegisterUserForm(UserCreationForm):

	def __init__(self, *args, **kwargs):

		super().__init__(*args, **kwargs)

		self.helper = FormHelper(self)

		self.helper.add_input(Submit('submit', 'Register'))

	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate'}), required=True,validators =[three_words])

# email = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate'}), required=True)

	class Meta:

		model = User

		fields = ['name', 'username', 'email', 'password1', 'password2']

```

----

## class based view :

```
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class DepartmentList(ListView):
    model = Department
    context_object_name = 'departments'
    template_name = 'settings/department-settings.html'

class DepartmentCreate(CreateView):
    model = Department
    template_name = 'settings/create_department.html'
    fields ='__all__'
    success_url = reverse_lazy('settings:department-settings')

class DepartmentEdit(UpdateView):
    model = Department
    template_name = 'settings/edit_department.html'
    fields ='__all__'
    success_url = reverse_lazy('settings:department-settings')

def DepartmentDelete(request, pk):
    dapartment = get_object_or_404(Department, id=pk)
    if request.user.type != 'admin':
        messages.error(request, 'you are not allowed here')
        return redirect('settings:department-settings')
    else:
        dapartment.delete()
    return redirect('settings:department-settings')
```

```html
# create , edit department forms :

<form method="POST">
        {% csrf_token %}
        {{form.as_p}}
        <input type="submit" id="submit" value="create">
    </form>
    
```



----

### html buttons with icons :

```html
 <a href="" class="btn btn-dark btn-block btn-sm m-1"><i class="fa-solid fa-pencil"></i></a>

<a class="btn btn-danger btn-block btn-sm m-1" href=""><i class="fa-solid fa-trash"></i></a>

<button type="submit" class="btn btn-dark ms-2"><i class="fa-solid fa-magnifying-glass"></i></button>
<a class="btn btn-dark ms-1" href=""><i class="fa-solid fa-arrows-rotate"></i></a>
```

----

## csv :

### import :

```python
def csvimportusers(request):
    if request.method == "POST":
        csv_file = request.FILES["csv_upload"]
        if not csv_file.name.endswith('.csv'):
            messages.warning(request, 'The wrong file type was uploaded')
            return HttpResponseRedirect(request.path_info)
        file_data = csv_file.read().decode("utf-8")
        csv_data = file_data.split("\n")
        for x in csv_data:
            fields = x.split(",")
            if len(fields) != 1 :
                try:
                    created = User.objects.update_or_create(
                    name = fields[0],
                    username = fields[1],
                    national_id = fields[2],
                    email = fields[3],
                    password = fields[4],
                    type = fields[5],
                    department =Department.objects.get(name=fields[6]),
                    branch =Branch.objects.get(name=fields[7]),
                    year = fields[8],
                    term = fields[9],
                    )
                    user=User.objects.get(username = fields[1])
                    # password = User.objects.make_random_password()
                    # user.set_password(password)
                    user.set_password(fields[4])
                    user.save()

                    # for cloud part
                    cloud_created = CloudUser.objects.update_or_create(
                    cloudusername = fields[1],
                    cloudpassword = fields[4],
                    )
                    cloud_created.save()
                    # end cloud part

                except:
                    user=User.objects.get(username = fields[1])
                    user.name=fields[0]
                    user.username=fields[1]
                    user.national_id=fields[2]
                    user.email=fields[3]
                    user.set_password(fields[4])
                    user.type=fields[5]
                    user.department=Department.objects.get(name=fields[6])
                    user.branch=Branch.objects.get(name=fields[7])
                    user.year = fields[8]
                    user.term = fields[9]
                    user.save()


                    # # for cloud part
                    # clouduser=CloudUser.objects.get(cloudusername = fields[1])
                    # clouduser.cloudusername=fields[1]
                    # clouduser.cloudpassword = fields[4],
                    # clouduser.save()
                    # # end cloud part


        return redirect('settings:allusers')
    csvform = CsvImportUsers()
    data = {
        "csvform": csvform,
        }
    return render(request, "settings/csv_users.html", data)

------------------------------
class CsvImportUsers(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Save'))
    csv_upload = forms.FileField()
------------------------------
path("csv-users", views.csvimportusers, name="csv-users"),
-------------------------
<div class="container">
    <div class="container" style="width:600px">
      <form action="" method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        {% crispy csvform %}
    </form>
    </div>
</div>
```



### export :

https://docs.djangoproject.com/en/4.0/howto/outputting-csv/

----

## pdf :

```html
<a id="userspdf" href="#" class="btn btn-dark btn-block btn-sm m-1">PDF</a>


<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"
        integrity="sha512-GsLlZN/3F2ErC5ifS5QtgpiJtWd43JWSuIgh7mbzZ8zBps+dvLusV+eNQATqgA/HdeKFVgA5v3S/cIrLF7QnIg=="
        crossorigin="anonymous" referrerpolicy="no-referrer"></script>

    <script>
        const userspdf = document.getElementById('userspdf')
        userspdf.addEventListener('click', (e) => {downloadPdf(e)})
        const downloadPdf = (e) => {
            e.preventDefault()
            const element = document.getElementById('users')
            html2pdf().set({filename: users.pdf}).from(element).save()
        }
    </script>



# note : users is the id of the div we want to print .
```



---

## reset password :

1) in urls.py of project :

```
from django.contrib.auth import views as auth_views

path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
        name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
        name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), 
        name="password_reset_complete"),

```

2) html files :from any previous project

----

## import , export django models to excel and json :

### export :

1) export data to json file : (db-dump.json)

   ```
   python manage.py dumpdata > db-dump.json
   ```

2)  update your "settings.py" file. Remove the information about Sqlite, and insert the correct information so you can connect to your new database.

   for example if you use mysql :

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'platrain',
           'USER': 'platrain',
           'PASSWORD': 'withALLAH',
           'HOST': '127.0.0.1',
           'PORT': '',
       }
   }
   ```

3) migrate your empty tables (tables without data )

   ```
   python manage.py migrate
   ```

4) open the shell :

   ```
   python manage.py shell
   ```

5) remove something called ContentType.

   ```
   >>> from django.contrib.contenttypes.models import ContentType
   >>> ContentType.objects.all().delete()
   ```


### import :

import the json file to your models :

```
python manage.py loaddata db.json
```

----
## footer :
لو عندنا جزء ثابت فى كل اصفحات زى الفوتر فاخنا هنعمله مرة واحد ونستدعيه بعد كدة

1) create a new file in app settings with the name ==>footer_context_processor.py

2) write this function in this file: (هنرجع بيانات جدول السيتنجس اللى هنملأ بيها الفوتر)

```python
from .models import Settings

def myfooter(request):

	myfooter = Settings.objects.last()

	return {'myfooter':myfooter} # هنا بنرجع البيانات دى ككونتكست بس يعنى معملنلهاش رندر فى اى صفحة ات تى ام ال
```

3) go to settings of the project and look for TEMPLATES and find 'context_processors' in it

then add this to them:

'settings.footer_context_processor.myfooter',

4) go to base.html (because all other files inherit from it) and call data on it

for example the name will be called like this ==> myfooter.site_name

where myfooter is the context data from the function and site_name is the name of the site from settings models



----------------------
## stars :

```django
<div class="text-primary mr-2">

                        {% for i in star_range %}

                        <small class="fas fa-star"></small>

                        {% endfor %}

                        {% if product_rate_float_part > 0 %}

                        <small class="fas fa-star-half-alt"></small>

                        {% for i in empty_star_range_if_there_is_half_star %}

                        <small class="far fa-star"></small>

                        {% endfor %}

                            {% else %}

                            {% for i in empty_star_range_if_no_half_star %}

                            <small class="far fa-star"></small>

                            {% endfor %}

                            {% endif %}

                    </div>
```
```python

# simplified product model
class Product(models.Model):

    name = models.CharField(max_length=100)

    def get_product_rate(self):

        ratings = self.rating_set.all()

        rate = 0.0

        rating_list = []

        for rating in ratings:

            rating_list.append(rating.star_number)

        if len(rating_list) > 0 :

            rate = round(sum(rating_list)/len(rating_list),1)

        return rate

#####################################################
def productdetail(request,product_id):

    product = Product.objects.get(id = product_id)

    context = {

        'product' : product,

        'product_rate' :product.get_product_rate(),

        'product_rate_int_part' :int(str(product.get_product_rate())[0]),

        'product_rate_float_part' :int(str(product.get_product_rate())[-1]),

        'star_range' :range(0,int(str(product.get_product_rate())[0])),

        'empty_star_range_if_no_half_star' :range(0,5-int(str(product.get_product_rate())[0])),

        'empty_star_range_if_there_is_half_star' :range(0,4-int(str(product.get_product_rate())[0])),

    }

    return render(request,'products/detail.html',context)
```


----------------------------
## update user without using form.py  

```html

<form class="form" action="" method="POST" enctype="multipart/form-data">

                {% csrf_token %}

                <label>Username:</label>

                </br>

                <input type="text" name="username" value = "{{user.username}}" />

                </br>

                <label>mail:</label>

                </br>

                <input type="email" name="email" value = "{{user.email}}" />

                </br>

                <label for="exampleFormControlFile1">image : {{im}}</label>

                </br>

                <input type="file" class="form-control-file" name = "image" id="exampleFormControlFile1">

  

                <a class="btn btn--dark" href="/">Cancel</a>

                </br>

                <button class="btn btn--main" type="submit">Update</button>

        </form>```

```python

from django.db import models

from django.contrib.auth.models import User


class UserAdditionalInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    image = models.ImageField(null=True,upload_to='userimages/' ,default="/static/img/avatar.jpeg")


############################################

@login_required(login_url='login')

def updateUser(request):

    user = request.user

    user_additional_information = UserAdditionalInfo.objects.get(user = user)

    im = user_additional_information.image.url

    if request.method == 'POST':

        username = request.POST.get('username')

        email = request.POST.get('email')

        image = request.FILES.get('image')

        user.username = username

        user.email = email

        user_additional_information.image = image

        user_additional_information.save()

        user.save()

        # user.useradditionalinfo.save()

        return redirect('/')

  

    return render(request, 'accounts/update-user.html', {'user': user,'im': im})
```


-----------
## OneToOneField :

```python

from django.contrib.auth.models import User

class UserAdditionalInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    image = models.ImageField(null=True,default="/static/img/avatar.jpeg")

#############################
def updateUser(request):

    user = request.user

    image = user.useradditionalinfo.image.url

# or

def updateUser(request):

    user = request.user

    user_additional_information = UserAdditionalInfo.objects.get(user = user)

    image = user_additional_information.image.url
```

---------------

## on_delete :
EX : 
```python
class Product(models.Model):
    host = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
```
* CASCADE  => when the Category (parent) is deleted ,delete all related children (products)
* SET_NULL => when the Category (parent) is deleted ,keep the children (products) but set the Category field to be null for every related product (child) 
 => the best example is the orders related to an user , if the user is deleted ,we need to keep the orders .
* SET_DEFAULT => when the Category (parent) is deleted ,give default value for the children 
* PROTECT => Parent (Category) can't be deleted before deleting the children (all related products)
--------------
## django social app :
follow this link :
https://simpleisbetterthancomplex.com/tutorial/2016/10/24/how-to-add-social-login-to-django.html

som information from ecommerce app :

  

Client ID

42d9be03d377c15a8ca3

Client secrets

010953e8e3cfd4bd7a413370e76c2c718745e349

https://github.com/settings/applications/1980199   # to manage next data

    Homepage URL : http://127.0.0.1:8000/

    Authorization callback URL : http://localhost:8000/


-------------------
## reset password :
1 - in project urls :
```python

from django.contrib.auth import views as auth_views

from django.views.generic.base import RedirectView

    path('reset_password/',

        auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),

        name="reset_password"),

  

    path('reset_password_sent/',

        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),

        name="password_reset_done"),

  

    path('reset/<uidb64>/<token>/',

        auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),

        name="password_reset_confirm"),

  

    path('reset_password_complete/',

        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),

        name="password_reset_complete"),
```
2 - in settings:
```python

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'platraincloud@gmail.com'

EMAIL_HOST_PASSWORD = 'meczfpooichwkudl'
```


------------------
## form action :

```html
 <form method='post' action="{% url 'products:addtocard' product.id %}">

                {% csrf_token %}

                <div class="d-flex mb-3">

                    <p class="text-dark font-weight-medium mb-0 mr-3">Sizes:</p>

                    {% for size in product.get_product_sizes %}

                        <div class="custom-control custom-radio custom-control-inline">

                            <input type="radio" class="custom-control-input" id="size-{{size}}" name="size" value="{{size}}">

                            <label class="custom-control-label" for="size-{{size}}">{{size}}</label>

                        </div>

                    {% endfor %}

                </div>

                <div class="d-flex mb-4">

                    <p class="text-dark font-weight-medium mb-0 mr-3">Colors:</p>

                    {% for color in product.get_product_colors %}

                        <div class="custom-control custom-radio custom-control-inline">

                            <input type="radio" class="custom-control-input" id="color-{{color}}" name="color" value="{{color}}">

                            <label class="custom-control-label" for="color-{{color}}">{{color}}</label>

                        </div>

                    {% endfor %}

                    <button type="submit" class="btn btn-primary px-3"><i class="fa fa-shopping-cart mr-1"></i> Add To Cart</button>

                </div>

            </form>
```
```python
def addtocard(request,product_id):

    product = Product.objects.get(id = product_id)

    size = request.POST.get('size') or ''

    color = request.POST.get('color') or ''

    quantity = request.POST.get('quantity') or ''

    if size and color:

        print(size)

        print(color)

        print('======================')

        messages.info(request, 'added successfully to your cart')

        return redirect('products:detail' ,product.id )

    else:

        messages.error(request, 'some data is lost')

        return redirect('products:detail' ,product.id )
```
```python
path('shop/<str:product_id>/addtocart/',views.addtocard,name = 'addtocard'),
```

--------------------
## add objects to ManyToMany:
```python
class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

class Entry(models.Model):
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)

###############################################

>>> john = Author.objects.create(name="John")
>>> paul = Author.objects.create(name="Paul")
>>> george = Author.objects.create(name="George")
>>> ringo = Author.objects.create(name="Ringo")
>>> entry.authors.add(john, paul, george, ringo)
#####################################################
# to loop it :
for i in entry.authers.all:
print(i.name)
```

------------------------------
## update_or_create():
```python
obj, created = Person.objects.update_or_create(
    first_name='John', last_name='Lennon',
    defaults={'first_name': 'Bob'},
)
```
## generate random coupon every time :

```python

class CouponDiscount(models.Model):

    coupon = models.CharField(max_length = 100,blank=True,null=True,

        editable=False)

    discount_value = models.FloatField(null = True , blank = True)

    def save(self, *args, **kwargs):

        self.coupon = create_random_coupon()

        super().save(*args, **kwargs)


def create_random_coupon():

    letters = string.ascii_lowercase # small letters

    nums = ['0','2','3','4','5','6','7','8','9']

    marks = ['@','#','$','%','&','*']

    return 'TRENDY'.join(random.choice(letters)+random.choice(nums)+random.choice(marks) for i in range(5))
```

--------------------------

## social share :
using js : 

follow this link :
https://www.cssscript.com/social-share-buttons-shareon/

or follow these steps:

```js

<!-- social share CDN -->

    <link

    href="https://cdn.jsdelivr.net/npm/shareon@2/dist/shareon.min.css"

    rel="stylesheet"/>

    <script

      src="https://cdn.jsdelivr.net/npm/shareon@2/dist/shareon.iife.js"

      defer

      init>

    </script>

<!-- end social share CDN -->

--------------------------------------------------
<div class="shareon">

                        <a class="facebook" data-url="http://localhost:8000{{request.path}}"></a>

                        <a class="linkedin"></a>

                        <a class="mastodon"></a>

                        <a class="messenger" data-fb-app-id="FACEBOOK APP IDD"></a>

                        <a class="odnoklassniki"></a>

                        <a class="pinterest"></a>

                        <a class="pocket"></a>

                        <button class="reddit"></button>

                        <button class="telegram"></button>

                        <button class="twitter"></button>

                        <button class="viber"></button>

                        <button class="vkontakte"></button>

                        <button class="whatsapp"></button>

                    </div>
```

------------------------------

## PayPal :

```
general :
mail : ahmedibra010951@gmail.com
password : withALLAH010
---------------------------------
personal :
mail : sb-zywuj20723022@personal.example.com
password : 6FoX,&_y

visa info :
4032037781863655
01/2024
286

----------------------------------
business :
mail : sb-gozq018060437@business.example.com
password : XmvA0^J@
```


* paypal button : https://developer.paypal.com/docs/checkout/standard/integrate/
* in previous link you will find instructions guid , follow it or follow these steps :
* create personal account to test as client  https://developer.paypal.com/developer/accounts/
* create business account to test as business owner  https://developer.paypal.com/developer/accounts/
* get paypal button html code from here : https://developer.paypal.com/docs/checkout/standard/integrate/  and put it in checkout page.
* create paypal app : https://developer.paypal.com/developer/applications  (choose sandbox for test or live for live) (choose merchant in app type) 
* after creating app you will get  client_id :
AW-zyA6aI_dwtHWc6v_cU-guoLMsZCW4W_IKTChAfD8vYSibIszie05pKMhOvvexmD2JeYxSyk99fCu1
* modify these parts in the  paypal button html code :
	* value should be  the value of the pill : {{pill.get_pill_price}}  
	```js

	amount: {
           value: '{{pill.get_pill_price.3}}',

            },
    ```
    * in this line :
                    <script src="https://www.paypal.com/sdk/js?client-id=test&currency=USD&intent=capture&enable-funding=venmo" data-sdk-integration-source="integrationbuilder"></script>
    replace test word with the code from the app you created to be like this :
                    <script src="https://www.paypal.com/sdk/js?client-id=Aczqv5O8ivCnjaomR95x95SZuXGg_dytelJW-jRXZQpvvTdX9C8CGFTYmsFbxsHX6TcIhPm6xX-1OcmJ&currency=USD&intent=capture&enable-funding=venmo" data-sdk-integration-source="integrationbuilder"></script>
------
## js :
* live search
```html

<input type="text" class="form-control" name="live_search" id="live_search"  placeholder="Search by name">

{% for product in products %}
<div class="col-lg-4 col-md-6 col-sm-12 pb-1" id="{{product.id}}">
{{product.name}}
</div>
{% endfor %}




<script>

        const data = "{{data}}" // get data from backend

        const products = JSON.parse(data.replace(/&#x27;/g,'"')) // beautify the data to be readable

        const live_search = document.getElementById("live_search");

        let searchList = []

        live_search.addEventListener('keyup', ()=>{

            // get non searched data then loop them and get getElementById(id of these non searched data )

            // we gave every card id = "this card id"

            // then we said get these non searched cards and hide them.

            nonSearchedProductList = products.filter(info=> info['name'].includes(live_search.value) == false)

            if (nonSearchedProductList.length > 0){

                nonSearchedProductList.map(pro=>{

                document.getElementById(pro['id']).style.display="none";

            })          

            }

        })

    </script>

```

```python

def shop(request):

    products = paginate(request)

    data= []

    for product in products:

        item = {

            'id' : product.id,

            'name' : product.name,

            'price' : product.price,
            'mainimage' : str(product.mainimage()),

            'priceafterproductdiscount' : product.priceafterproductdiscount(),

        }

        data.append(item)

    context = {

        'products' : products,

        'data' : data,

    }

    return render(request,'products/shop.html',context)


# OR :

def shop(request):

    products = paginate(request)

	data = json.dumps(list(Product.objects.values('name','price')))

    context = {

        'products' : products,

        'data' : data,

    }

    return render(request,'products/shop.html',context)

# OR :

from django.core import serializers

def shop(request):

    products = paginate(request)

	data = serializers.serialize('json',products)

    context = {

        'products' : products,

        'data' : data,

    }

    return render(request,'products/shop.html',context)

```

* add to love and delete from love :

``` html

{% for product in products %}

{{product.name}}

 <a id="addtolovelink{{product.id}}" onclick="addto{{product.id}}love()" class="btn btn-sm text-dark p-0" style="display:block;"><i class="fas fa-heart text-primary mr-1"></i> Love</a>

<a id="removefromlovelink{{product.id}}" onclick="removefrom{{product.id}}love()" class="btn btn-sm text-dark p-0" style="display:none;"><i class="fas fa-trash text-primary mr-1"></i> Remove</a>

  

<script>

	function addto{{product.id}}love(){

		var url = "{% url 'products:addtolove' %}"

		var product_id = {{product.id}};

		fetch (url , {

			method:"POST",

			headers:{

				'Content-type':'application/json' ,

				'X-CSRFToken': csrftoken,

			},

			body:JSON.stringify({'product_id':product_id})

		})

		.then((body) => {

			document.getElementById('removefromlovelink{{product.id}}').style.display="block";

			document.getElementById('addtolovelink{{product.id}}').style.display="none";

		})

	}

	function removefrom{{product.id}}love(){

		var url = "{% url 'products:deletefromloved' %}"

		var product_id = {{product.id}};

		fetch (url , {

			method:"POST",

			headers:{

				'Content-type':'application/json' ,

				'X-CSRFToken': csrftoken,

			},

			body:JSON.stringify({'product_id':product_id})

		})

		.then((body) => {
			document.getElementById('removefromlovelink{{product.id}}').style.display="none";

			document.getElementById('addtolovelink{{product.id}}').style.display="block";

		})

	}

</script>

                             

   {% endfor %}

```

``` python

def addtolove(request):

    body = json.loads(request.body)

    user = request.user

    product = Product.objects.get(id = body['product_id'])

    if user.username != "" :

        loved = Love.objects.update_or_create(product = product , user = user)

        loved[0].save()

    return JsonResponse("done",safe=False)
  

def deletefromloved(request):

    body = json.loads(request.body)

    product = Product.objects.get(id=body['product_id'])

    loved_product = Love.objects.filter(product=product)[0]

    loved_product.delete()

    return JsonResponse("done",safe=False)

```

* send form data to backend :

``` python

from django.http import HttpResponse
def subscribe(request):

    user = request.user

    email = request.POST.get("subscribe-mail")

    subscriber = NewsLetter.objects.create(email=email,user=user)

    subscriber.save()

    return HttpResponse("done")

```

``` html

    <!-- Subscribe Start -->

    <div class="container-fluid bg-secondary my-5" id="subscribe-div" {% if subscribestatus == "subscribed" %}style="display:none;"{% endif %}>

        <div class="row justify-content-md-center py-5 px-xl-5">

            <div class="col-md-6 col-12 py-5">

                <div class="text-center mb-2 pb-2">

                    <h2 class="section-title px-5 mb-3"><span class="bg-secondary px-2">Stay Updated</span></h2>

                    <p>We will send you our new products or or offers or coupons .</p>

                </div>

                <form action="{% url 'contact:subscribe' %}" id="subscribe-form">

                    {% csrf_token %}

                    <div class="input-group">

                        <input type="text" class="form-control border-white p-4" name="subscribe-mail" id="subscribe-mail" placeholder="Email Goes Here">

                        <div class="input-group-append">

                            <button class="btn btn-primary px-4" id="subscribe-submit">Subscribe</button>

                        </div>

                    </div>

                </form>

            </div>

        </div>

    </div>

    <!-- Subscribe End -->

        <!-- what will be shown after Subscribe  Start -->

        <div class="container-fluid bg-secondary my-5" id="subscribe-alternative-div" {% if subscribestatus == "unsubscribed" %}style="display:none;"{% endif %}>

            <div class="row justify-content-md-center py-5 px-xl-5">

                <div class="col-md-6 col-12 py-5">

                    <div class="text-center mb-2 pb-2">

                        <h2 class="section-title px-5 mb-3"><span class="bg-secondary px-2">You are a subdcrber</span></h2>

                        <p>you will be updated by new products or or offers or coupons .</p>

                    </div>

                </div>

            </div>

        </div>

        <!--what will be shown after Subscribe End -->

  
   <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.1/jquery.min.js" integrity="sha512-aVKKRRi/Q/YV+4mjoKBsE4x3H+BkegoM/em46NNlCqNTmUYADjBbeNefNxYV7giUp0VxICtqdrbqU7iVaeZNXA==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>

    <script>

        function getCookie(name) {

            let cookieValue = null;

            if (document.cookie && document.cookie !== '') {

                const cookies = document.cookie.split(';');

                for (let i = 0; i < cookies.length; i++) {

                    const cookie = cookies[i].trim();

                    // Does this cookie string begin with the name we want?

                    if (cookie.substring(0, name.length + 1) === (name + '=')) {

                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));

                        break;

                    }

                }

            }

            return cookieValue;

        }

        const csrftoken = getCookie('csrftoken');

        // subscribe form

        var subscribemail = document.getElementById('subscribe-mail');

        var subscribesubmit = document.getElementById('subscribe-submit');

        var subscribeform = document.getElementById('subscribe-form');

        var subscribediv = document.getElementById('subscribe-div');

        var subscribealternativediv = document.getElementById('subscribe-alternative-div');

  

        $("#subscribe-form").submit(function(e) {

  

            e.preventDefault(); // avoid to execute the actual submit of the form.

            var form = $(this);

            var actionUrl = form.attr('action');

            //console.log(actionUrl)

            $.ajax({

                type: "POST",

                url: actionUrl,

                data: form.serialize(), // serializes the form's elements.

                success: function(data)

                {

                    subscribediv.style.display = "none";

                    subscribealternativediv.style.display = "block";

                }

            });

        });

 

    </script>

```

--------------------
## send email message :

```html

<form name="sentMessage" id="contactForm" method="POST">
{% csrf_token %}

<input type="text" name="name" />

<input type="email" name="email" />

<input type="text" name="subject" />

<textarea name="message" ></textarea>

<button type="submit">Send Message</button>
</form>

```

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'platraincloud@gmail.com'

EMAIL_HOST_PASSWORD = 'meczfpooichwkudl'

# PlatRain010
```

```python

from django.core.mail import send_mail
from django.conf import settings

def contact(request):

if request.method == 'POST':

	subject = request.POST.get('subject')

	name = request.POST.get('name')

	email = request.POST.get('email')

	message = request.POST.get('message')

	send_mail(

		subject,

		f'message from {name} \n email : {email} \n Message : {message}',

		email,

		[settings.EMAIL_HOST_USER],

		fail_silently=False,

	)

	return redirect('/')

return render(request,'contact/contact.html')
```

```python
path('contact',views.contact, name = 'contact'),
```

### send multable email messages from one mail to many others :

```python
def sendnewproductsmails(request):

	newsletterobjects = NewsLetter.objects.all()
	
	emails =[]
	
	for obj in newsletterobjects:
	
		emails.append(obj.email)
	
	send_mail(
	
		'new products', # title
		
		'http://127.0.0.1:8000/shop/?sort=latest', # mssage
		
		settings.EMAIL_HOST_USER, # from
		
		emails, #to
		
		fail_silently=False,
	
	)

	return redirect('/admin/products/product/')
```


-------------
## celery :

#### install celery :
	pip install celery
#### install redis server:
	sudo apt install redis-server
#### install redis :
	pip install redis
#### run redis in another terminal (run it in normal terminal) :
	redis-server
#### create celery.py file in project folder and put : 

```python
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
# ecommerce is the name of the project

app = Celery('ecommerce')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
# should have a `CELERY_` prefix.

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task(bind=True)

def debug_task(self):

print(f'Request: {self.request!r}')
```

#### add this in __init__.py file in project folder :

```python
from .celery import app as celery_app

__all__ = ('celery_app',)
```

#### add celery settings in setting.py :

```python
CELERY_BROKER_URL = "redis://localhost:6379"

CELERY_RESULT_BACKEND = "redis://localhost:6379"
```

#### check if celery is working in your project or not :
*next command should be run in new terminal of the project => activate the environment and make all things as if you will run django server but run this command instesd*
*now should be 3 terminals opened => django server , redis server , and celery info*

	celery -A ecommerce worker -l info   (ecommerce is the name of the project)

### now we have a function that we need torun it in celery server :

```python
def sendnewproductsmails(request):

	newsletterobjects = NewsLetter.objects.all()
	
	emails =[]
	
	for obj in newsletterobjects:
	
		emails.append(obj.email)
	
	send_mail(
	
		'new products', # title
		
		'http://127.0.0.1:8000/shop/?sort=latest', # mssage
		
		settings.EMAIL_HOST_USER, # from
		
		emails, #to
		
		fail_silently=False,
	
	)

	return redirect('/admin/products/product/')
```

#### solution is :
* create a file (tasks.py for example) and put in it :
```python
from celery import shared_task

from django.core.mail import send_mail

from django.conf import settings

from django.shortcuts import redirect

from contact.models import NewsLetter

  
  

@shared_task

def sendmailstask():

newsletterobjects = NewsLetter.objects.all()

emails =[]

for obj in newsletterobjects:

emails.append(obj.email)

  

send_mail(

'new products', # title

'http://127.0.0.1:8000/shop/?sort=latest', # mssage

settings.EMAIL_HOST_USER, # from

emails, #to

fail_silently=False,

)
```

* the main function that we are working on (sendnewproductsmails) will remain in views but will be reformed like that :
```python
def sendnewproductsmails(request):

sendmailstask.delay()

return redirect('/admin/products/product/')
```

* so when sendnewproductsmails function is called by url , it will call sendmailstask from tasks.py and execute it in celery server .

----------------
## Google drive as your progect storage :

https://django-googledrive-storage.readthedocs.io/en/latest/

---------------
## drive api :
*we created google cloud project : 
	https://console.cloud.google.com/welcome?project=platrain
information of this project:
	name : platrain
	Project number: 648039689590
	Project ID: platrain

------
## generate demo data :

mockaroo.com

----
## generate upload folder name based on the parent that the files related to : 

```python
def exam_file_path(instance, filename):
    """
    Returns the path where the file should be uploaded for the given Files instance.
    The file will be uploaded to a directory named after the exam's ID or title.
    """  
    exam = instance.exam
    exam_id = str(exam.id)
    exam_title = exam.title.replace(' ', '_')
    return os.path.join('examfiles', exam_id + '_' + exam_title, filename)

class Exam(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان الامتحان')
class Files(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE,null=True)
    file = models.FileField(upload_to=exam_file_path)
```


the king
the ooutlow king