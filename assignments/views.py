from django.shortcuts import render, redirect
from .forms import AssignmentGiveForm


# from django.views.generic import ListView
# from django.views.generic import DetailView
# from .models import GiveAssignment, UploadedAssignment
# from django.shortcuts import get_object_or_404
#
# from .forms import AssignmentUploadForm
# from django.views.generic.edit import FormView
#
#
# class AssignmentListView(ListView):
#     model = GiveAssignment
#     context_object_name = 'assignment_list'
#     template_name = 'assignments/assignment_list.html'
#
#
# # def assignment_submit(request, pk):
# #     assignment = get_object_or_404(Assignment, pk=pk)
# #     if request.method == 'POST':
# #         # form is sent
# #         form = AssignmentUploadForm(data=request.POST)
# #         if form.is_valid():
# #             pass
# #             # # form data is valid
# #             # cd = form.cleaned_data
# #             # new_item = form.save(commit=False)
# #             #
# #             # # assign current user to the item
# #             # new_item.user = request.user
# #             # new_item.save()
# #             # create_action(request.user, 'bookmarked image', new_item)
# #             # messages.success(request, 'Image added successfully')
# #             #
# #             # # redirect to new created item detail view
# #             # return redirect(new_item.get_absolute_url())
# #     else:
# #         # build form with data provided by the bookmarklet via GET
# #         form = AssignmentUploadForm(data=request.GET)
# #     return render(request, 'assignments/assignment_detail.html', {'assignment':assignment, 'form':form})
#
# # class AssignmentDetailView(DetailView, FormView):
# #     model = Assignment
# #     context_object_name = 'assignment'
# #     form_class = AssignmentUploadForm
# #     success_url = '/assignments'
# #     template_name = 'assignments/assignment_detail.html'
# #
# #     def form_valid(self, form):
# #         form.save()
# #         return super(AssignmentDetailView, self).form_valid(form)
#
#
# def assignmentdetailview(request, pk):
#     assignment = get_object_or_404(GiveAssignment, pk=pk)
#
#     if request.method != 'POST':
#         form = AssignmentUploadForm(request.GET)
#     else:
#         # POST data submitted; process data.
#         form = AssignmentUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_entry = form.save(commit=False)
#             new_entry.assignment = assignment
#             new_entry.student = request.user
#             new_entry.save()
#             return render(request, 'assignments/submitted_list.html')
#     context = {'assignment': assignment, 'form': form}
#     return render(request, 'assignments/assignment_detail.html', context)
#
#
# def submittedassignment(request):
#     submitted_list = UploadedAssignment.objects.filter(student=request.user)
#     return render(request, 'assignments/submitted_list.html', {'submitted_list':submitted_list})
#

def give_assignment(request):
    if request.user.is_authenticated:
        if request.method != 'POST':
            form = AssignmentGiveForm()
        else:
            form = AssignmentGiveForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('dashboard')

    context = {
        'form': form,
    }
    return render(request, 'pages/assignment_give.html', context)
