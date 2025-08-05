from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product,Category
from product.serializers import ProductSerializer,CategorySerializer
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin,ListModelMixin
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class ProductViewSet(ModelViewSet):
   queryset = Product.objects.all()
   serializer_class = ProductSerializer

   def destroy(self, request, *args, **kwargs):
      product  = self.get_object()
      if product.stock > 10:
         return Response({'message':'Product With stock more than 10 could not be deleted'})
      self.perform_destroy(product)
      return Response(status=status.HTTP_204_NO_CONTENT)




class CategoryViewSet(ModelViewSet):
   queryset = Category.objects.annotate(
      product_count = Count('products')
      ).all()
   serializer_class = CategorySerializer





# class ProductList(ListCreateAPIView):
   #jodi kokhono logical things handle kora na lage tahole ei attributes gula override korbo
   # queryset = Product.objects.all()
   # serializer_class = ProductSerializer

   # Jodi kokhono logical bepar means first user login tokhon function gula use korbo
   # def get_queryset(self):
   #    return Product.objects.select_related('category').all()
   # def get_serializer_class(self):
   #    return ProductSerializer
   # def get_serializer_context(self):
   #    return {'request':self.request}

# class ProductDetails(RetrieveUpdateDestroyAPIView):
#    queryset = Product.objects.all()
#    serializer_class = ProductSerializer
#    lookup_field = 'id'





# class CategoryList(ListCreateAPIView):
#    queryset = Category.objects.annotate(
#       product_count = Count('products')
#       ).all()
#    serializer_class = CategorySerializer



# class CategoryDetails(RetrieveUpdateDestroyAPIView):
#    queryset = Category.objects.annotate(
#       product_count = Count('products')
#       ).all()
#    serializer_class = CategorySerializer




# class ViewProduct(APIView):
#    def get(self,request):
#       products = Product.objects.select_related('category').all()
#       serializer = ProductSerializer(products,many=True)

#       return Response(serializer.data)
   
#    def post(self,request):
#       serializer = ProductSerializer(data=request.data)   #deserializer
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data,status=status.HTTP_201_CREATED)






# class ViewSpecificProduct(APIView):
#    def get(self,request,id):
#       product =get_object_or_404(Product,pk=id)
#       serializer = ProductSerializer(product)
#       return Response(serializer.data)
   
#    def put(self,request,id):
#       product =get_object_or_404(Product,pk=id)
#       serializer = ProductSerializer(product,data=request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data)
   
#    def delete(self,request,id):
#       product =get_object_or_404(Product,pk=id)
#       product.delete()
#       return Response(status=status.HTTP_204_NO_CONTENT)






# class ViewCategories(APIView):
#    def get(self,request):
#       categories = Category.objects.annotate(
#       product_count = Count('products')
#       ).all()
#       serializer = CategorySerializer(categories,many = True)
#       return Response(serializer.data)
   
#    def post(self,request):
#       serializer = CategorySerializer(data=request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data,status=status.HTTP_201_CREATED)



# class ViewSpecificCategory(APIView):
#    def get(self,request,id):
#       category = get_object_or_404(Category.objects.annotate(
#             product_count = Count('products')
#             ).all(),pk=id
#       )
#       serializer = CategorySerializer(category)
#       return Response(serializer.data)


#    def put(self,request,id):
#        category = get_object_or_404(Category.objects.annotate(
#             product_count = Count('products')
#             ).all(),pk=id
#           )
#        serializer = CategorySerializer(category,data=request.data)
#        serializer.is_valid(raise_exception=True)
#        serializer.save()
#        return Response(serializer.data)


#    def delete(self,request,id):
#       category = get_object_or_404(Category.objects.annotate(
#             product_count = Count('products')
#             ).all(),pk=id
#       )
#       category.delete()
#       return Response(status=status.HTTP_204_NO_CONTENT)



