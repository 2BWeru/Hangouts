from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
# from cloudinary.models import CloudinaryField
# from django.forms import PasswordInput

# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)
#     username = None

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

class Category(models.Model):
    title = models.CharField(max_length=255, blank=True)
    

    def __str__(self):
        return f'{self.title} category'

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self, title):
        """
        updates category
        """
        self.update(title=title)

    @classmethod
    def find_category(cls, category_id):
        return cls.objects.filter(id=category_id)


class Event(models.Model):
    title = models.CharField(max_length=100)
    about = models.TextField(max_length=1000)
    due_date=models.DateField()
    photo = models.ImageField(upload_to='media/',default='',null=True,blank=True)
    Location=models.CharField(max_length=300)
    date = models.DateField(auto_now_add=True)   

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, related_name='filter')


    def __str__(self) -> str:
        return self.title

    @classmethod
    def save_event(cls, event):
        cls.save(event)

    @classmethod
    def delete_event(cls, event_id):
        cls.delete(id=event_id)

    @classmethod
    def find_event(cls, title):
        events = cls.objects.filter(title__icontains=title)
        return events

    @classmethod
    def update_event(cls, title, about, date, due_date, photo, Location):
        cls.update(title=title, about=about, date=date, due_date=due_date, photo=photo, Location=Location)




class Review(models.Model):
    # user= models.ForeignKey(User,on_delete=models.CASCADE)
    reviews = models.CharField(max_length=100)
    created=models.DateTimeField(auto_now=True)
    event=models.ForeignKey(Event,related_name='site',on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return f'{self.reviews} Review'

def upload_path(instance, filname):
    return'/'.join(['avatars',str(instance.title),filname])

class Profile (models.Model):
    fname = models.CharField(max_length=30)
    bio=models.TextField(max_length=300)
    instagram_acc=models.CharField(max_length=200)
    facebook_acc=models.CharField(max_length=200)
    idNo = models.IntegerField(default=0,primary_key=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    # emailaddress = models.CharField(max_length=50)
    avatar =models.ImageField(blank=True, upload_to=upload_path)
    

    def __str__(self):
        return f'{self.fname} Profile'

    def save_profile(self):
        self.save
    
    def delete_profile(self):
        self.delete()

    # search
    @classmethod
    def search_by_fname(cls,searched_term):
        profile = cls.objects.filter(fname__icontains=searched_term)
        return profile
        
class Posts(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ImageField(upload_to='post',default='',null=True,blank=True)
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'{self.title} Post'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

class Site(models.Model):
    title = models.CharField(max_length=100)
    id = models.IntegerField(default=0,primary_key=True)
    text = models.TextField(max_length=1000)
    photo = models.ImageField(upload_to='postSite',default='',null=True,blank=True)
    date = models.DateField(auto_now_add=True)
    Location=models.CharField(max_length=300)
    


    def __str__(self):
        return f'{self.title} Site'

    def save_site(self):
        self.save()

    def delete_site(self):
        self.delete()
    
    # search
    @classmethod
    def search_by_title(cls,searched_term):
        title = cls.objects.filter(title__icontains=searched_term)
        return title

class Review(models.Model):
    # user= models.ForeignKey(User,on_delete=models.CASCADE)
    reviews = models.CharField(max_length=100)
    created=models.DateTimeField(auto_now=True)
    site=models.ForeignKey(Site,related_name='site',on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return f'{self.user} Review'