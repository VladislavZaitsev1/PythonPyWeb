import django
import os
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from apps.db_train_alternative.models import Blog, Author, AuthorProfile, Entry, Tag

    # TODO Сделайте здесь запросы

     #obj = Entry.objects.filter(author__name__contains='author')
     #print(obj)

obj = Entry.objects.filter(author__name__contains='author')
print(obj)
"""<QuerySet [<Entry: Оазисы Сахары: красота и опасность>, 
<Entry: Новые гаджеты и устройства: обзор рынка>]>"""

obj = Entry.objects.filter(author__authorprofile__city=None)
print(obj)

print(Entry.objects.filter(id__in=[1, 3, 4]))

print(Entry.objects.filter(number_of_comments__in='123'))

inner_qs = Blog.objects.filter(name__contains='Путешествия')
entries = Entry.objects.filter(blog__in=inner_qs)
print(entries)

start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2023, 12, 31)
print(Entry.objects.filter(pub_date__range=(start_date, end_date)))





