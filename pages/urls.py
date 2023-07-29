from django.urls import path
from .views import HomePageView, SubjectListView, AssignmentListView, AssignmentDetailView, delete_assignment, \
    check_plagiarism
from assignments.views import give_assignment

# app_name = "pages"
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('delete-assignment/<pk>/', delete_assignment, name='delete_ass'),
    path('check-plagiarism/<pk>/', check_plagiarism, name='check_plag'),
    path('give-assignment/', give_assignment, name='give-assignment'),
    path('dashboard/', SubjectListView.as_view(), name='dashboard'),
    path('<uuid:pk>/', AssignmentDetailView.as_view(), name='assignment_detail'),
    path('<slug:slug>/', AssignmentListView.as_view(), name='assignment_list'),

]
