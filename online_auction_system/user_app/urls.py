from django.urls import path
from .views import CountryViweset, StateViweset, CityViweset, UserViweset, BankInformationViweset
urlpatterns = [
    path('country/', CountryViweset.as_view({'post':'create','get':'list'})),
    path('country/<int:pk>/', CountryViweset.as_view({'get':'retrieve','delete':'destroy','put':'update','patch':'partial_update'})),
    path('state/', StateViweset.as_view({'post':'create','get':'list'})),
    path('state/<int:pk>/', StateViweset.as_view({'get':'retrieve','delete':'destroy','put':'update','patch':'partial_update'})),
    path('city/', CityViweset.as_view({'post':'create','get':'list'})),
    path('city/<int:pk>/', CityViweset.as_view({'get':'retrieve','delete':'destroy','put':'update','patch':'partial_update'})),
    path('user/', UserViweset.as_view({'post':'create','get':'list'})),
    path('user/<int:pk>/', UserViweset.as_view({'get':'retrieve','delete':'destroy','put':'update','patch':'partial_update'})),
    path('bank/', BankInformationViweset.as_view({'post':'create','get':'list'})),
    path('bank/<int:pk>/', BankInformationViweset.as_view({'get':'retrieve','delete':'destroy','put':'update','patch':'partial_update'})),

    
]