from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# from django.forms import PasswordInput

# class User(models.Model):
#     username = models.CharField(max_length=50, null=True)
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)
    # username = None

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
    
    # def __str__(self):
    #     return self.username

class Event(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    id = models.IntegerField(default=0,primary_key=True)
    Location=models.CharField(max_length=300)
    time=models.DateField()
    due_date=models.DateField()
    photo = CloudinaryField('image',default='',null=True,blank=True)
    date = models.DateField(auto_now_add=True)
    # neighbourhood = models.ForeignKey(,on_delete=models.CASCADE, default='', null=True, blank=True)


    def __str__(self):
        return f'{self.title} Event'

    def save_event(self):
        self.save()

    def delete_event(self):
        self.delete()
    # search
    @classmethod
    def search_by_title(cls,searched_term):
        title = cls.objects.filter(title__icontains=searched_term)
        return title

class Review(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    reviews = models.CharField(max_length=100)
    created=models.DateTimeField(auto_now=True)
    event=models.ForeignKey(Event,related_name='site',on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return f'{self.reviews} Review'

# def upload_path(instance, filname):
#     return'/'.join(['avatars',str(instance.title),filname])

class Profile (models.Model):
    fname = models.CharField(max_length=30)
    bio=models.TextField(max_length=300)
    instagram_acc=models.CharField(max_length=200)
    facebook_acc=models.CharField(max_length=200)
    id=models.AutoField(auto_created = True,primary_key = True,serialize = False) 
    # idNo = models.IntegerField(null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,default='')
    avatar = CloudinaryField('avatar')
    

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
    post = CloudinaryField('post',default='post',null=True,blank=True)
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
    photo = CloudinaryField('postSite',default='postsite',null=True,blank=True)
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

# class Review(models.Model):
#     user= models.ForeignKey(User,on_delete=models.CASCADE)
#     reviews = models.CharField(max_length=100)
#     created=models.DateTimeField(auto_now=True)
#     site=models.ForeignKey(Site,related_name='site',on_delete=models.CASCADE,null=True, blank=True)

#     def __str__(self):
#         return f'{self.user} Review'