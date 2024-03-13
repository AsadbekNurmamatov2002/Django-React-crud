# Django-React-Redis

- Redis orqali APIni cach qilamiz

redis-server ni o'rnatamiz

>      sudo apt-get install redis-server

djangorestframework va redis ni loyihamizga o'rnatamiz

>      pip install django djangorestframework redis

settings.py
>    REDIS_HOST = 'localhost'
>    REDIS_PORT = 6379

>    from django.urls import path
>    from rest_framework.urlpatterns import format_suffix_patterns
>    from .views import manage_items, manage_item
>
>    urlpatterns = {
>         path('', manage_items, name="items"), # lets us create entries and view all entries
 >        path('<slug:key>', manage_item, name="single_item") #manages each entry
>    } 
>    urlpatterns = format_suffix_patterns(urlpatterns)


- views.py
  >    import rides
  >    redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
  >                               port=settings.REDIS_PORT, db=0)
  >
  >     @api_view(['GET', 'POST']) 
>      def manage_items(request, *args, **kwargs): #defining manage_items
>          if request.method == 'GET':
>            items = {}
 >           count = 0
 >           for key in redis_instance.keys("*"):
 >               items[key.decode("utf-8")] = redis_instance.get(key)
 >               count += 1
 >           response = {'count': count,'msg': f"Found {count} items.",'items': items}
 >         return Response(response, status=200)
  >        elif request.method == 'POST':
  >            item = json.loads(request.body)               #passing json object to create an item
  >            key = list(item.keys())[0]
 >             value = item[key]
 >             redis_instance.set(key, value)
  >            response = {'msg': f"{key} successfully set to {value}" }
  >        return Response(response, 201)
