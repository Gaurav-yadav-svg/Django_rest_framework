# from django.shortcuts import render
# from .models import Student
# from .serializers import StudetSerializer
# from rest_framework.renderers import JSONRenderer
# from django.http import HttpResponse,JsonResponse

# for retrieve data
# def Student_Detail(request, pk):

#     stu = Student.objects.get(id = pk) # Fetching data from database
#     serializer = StudetSerializer(stu) # converting model instance into native python datatype
#     json_data = JSONRenderer().render(serializer.data) # convert python datatype dict into json 
#     return HttpResponse(json_data,content_type = 'application/json')
#     # return JsonResponse(serializer.data)


# def Student_List(request):
#     stu = Student.objects.all()  
#     serializer = StudetSerializer(stu,many = True)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data,content_type = 'application/json')
#     # return JsonResponse(serializer.data,safe=False)

# from django.shortcuts import render
# import io
# from rest_framework.parsers import JSONParser
# from .serializers import StudetSerializer
# from rest_framework.renderers import JSONRenderer
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def Student_Create(request):
#     if request.method == 'POST':

#         json_data = request.body # json data from third party application
#         print("body:-",json_data)

#         stream = io.BytesIO(json_data)# it shows id of object
#         print("stream:-",stream)

#         pythondata = JSONParser().parse(stream)# converted json data into python native data
#         print("pythondata:-",pythondata)

#         serializer = StudetSerializer(data = pythondata)# converted python data into complex data
#         print("serializer:-",serializer)

#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data Saved'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type = 'application/json')
        
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type = 'application/json')

from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudetSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(csrf_exempt,name='dispatch')
class StudentAPI(View):

    """Read Data"""
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)

        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudetSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type = 'application/json' )
        
        stu = Student.objects.all()
        serializer = StudetSerializer(stu,many =True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type = 'application/json')  

    """Create Data"""
    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudetSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Saved'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type = 'application/json')

    """Update Post"""
    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id = id)
        serializer = StudetSerializer(stu, data = pythondata, partial = True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Data Updated !!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type = 'application/json')

    """Delete Post"""
    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        res = {'msg' : 'Data Deleted !!'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type = 'application/json')


# @csrf_exempt
# def Student_api(request):
    
#     """Read Data"""
#     if request.method == 'GET':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id', None)

#         if id is not None:
#             stu = Student.objects.get(id = id)
#             serializer = StudetSerializer(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data,content_type = 'application/json' )
        
#         stu = Student.objects.all()
#         serializer = StudetSerializer(stu,many =True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data,content_type = 'application/json')

#     """Create Data"""
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = StudetSerializer(data = pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data Saved'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type = 'application/json')

#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type = 'application/json')

#     """Update Data"""
#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         stu = Student.objects.get(id = id)
#         serializer = StudetSerializer(stu, data = pythondata, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg' : 'Data Updated !!'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type = 'application/json')

#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type = 'application/json')

#     """Delete Data"""
#     if request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         stu = Student.objects.get(id = id)
#         stu.delete()
#         res = {'msg' : 'Data Deleted !!'}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data,content_type = 'application/json')
    