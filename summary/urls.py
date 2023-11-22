from django.urls import path
from . import views



urlpatterns =[
   
    path('pdf2/generate_summary', views.generate_summary_view, name='generate_summary'),
    
    path('pdf2', views.process_pdf_view, name='pdf2'),
    path('', views.homepage, name='homepage'),
    path('text2', views.tool, name='text2'),
    #path('download_summary/', views.download_summary_as_word, name='download_summary_as_word'),
    #path('download_summary',views.download_summary,name="download_summary"),
    path("textsum/",views.tool,name="textsum_tool"),
    
    
    # path('download_summary/<str:text>/', views.download_summary_as_word, name='download_summary_as_word'),
    # path('download_summary/<str:text>/', views.download_summary_as_word, name='download')

    

    path('random',views.random, name='random' ),
    path('download_summary/', views.download_summary, name='download_summary'),

    
]