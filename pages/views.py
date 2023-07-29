import json
import os
import re

import PyPDF2
import pdfplumber
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormMixin

from assignments.forms import AssignmentUploadForm, StatusChangeForm
from assignments.models import GiveAssignment, UploadAssignment
from college.models import Subject
from .preprocessing import data_processing
from django.conf import settings


def jaccard_similarity(list1, list2):
    union = len(list1) + len(list2)
    intersection = 0
    if len(list2) >= len(list1):
        for i in list1:
            if i in list2:
                intersection += 1
    else:
        for i in list2:
            if i in list1:
                intersection += 1
    return int(round((intersection / (union - intersection)) * 100))


class HomePageView(TemplateView):
    template_name = 'home.html'


class SubjectListView(ListView):
    model = Subject
    context_object_name = 'subjects'
    template_name = 'pages/subject_list.html'


class AssignmentListView(DetailView):
    model = Subject
    context_object_name = 'assignments'
    template_name = 'pages/assignment_list.html'


def delete_assignment(request, pk):
    delete_ass = UploadAssignment.objects.get(pk=pk)
    print('his sfdd')
    delete_ass.delete()

    return redirect('dashboard')


class AssignmentDetailView(FormMixin, DetailView):
    model = GiveAssignment
    context_object_name = 'assignment'
    form_class = AssignmentUploadForm
    template_name = 'pages/assignment_detail.html'

    def get_success_url(self):
        return reverse_lazy('assignment_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, *args, **kwargs):
        context = super(AssignmentDetailView, self).get_context_data(*args, **kwargs)
        check_ass = UploadAssignment.objects.filter(assignment__title=self.get_object().title,
                                                    student=self.request.user)

        if check_ass.exists():
            assignment_uploaded = UploadAssignment.objects.get(assignment__title=self.get_object().title,
                                                               student=self.request.user)
            context['assignment_uploaded'] = assignment_uploaded
            filename = assignment_uploaded.upload_file.name
            x = re.sub("/", " ", filename)
            x = re.split("\s", x)
            context['filename'] = x[2]

        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        user = UploadAssignment.objects.filter(assignment__title=self.get_object().title, student=self.request.user)
        if user.exists():
            messages.info(self.request, "You have already submitted your assignment✔")
        else:
            new_entry = form.save(commit=False)
            new_entry.assignment = self.get_object()
            new_entry.student = self.request.user
            new_entry.save()
            messages.success(self.request, "Thank you for submitting!!!")

        return super(AssignmentDetailView, self).form_valid(form)

    def form_invalid(self, form):
        # put logic here
        return super(AssignmentDetailView, self).form_invalid(form)


def extractPDF(filename):
    text = ""
    with pdfplumber.open(filename) as pdf:
        num_pages = len(pdf.pages)
        count = 0
        while count < num_pages:
            pageObj = pdf.pages[count]
            count += 1
            text += pageObj.extract_text()
        if text != "":
            text = text
    return text


directory =  os.path.join(settings.BASE_DIR, 'pages', 'hash_value.txt')


def check_plagiarism(request, pk):
    assignment = UploadAssignment.objects.get(pk=pk)
    filename = assignment.upload_file.name
    pdf_text = extractPDF('media/' + filename)
    finger_print1 = data_processing(pdf_text, 3)

    x = re.sub("/", " ", filename)
    x = re.split("\s", x)
    pdf_score = dict()

    with open(directory, 'r') as f:
        datasets = json.loads(f.read())
        f.close()
    for k, v in datasets.items():
        pdf_score[k] = jaccard_similarity(finger_print1, v)

    score = sorted(pdf_score.items(), key=lambda x: x[1], reverse=True)[:3]
    form = StatusChangeForm(request.POST or None, request.FILES or None, instance=assignment)
    if form.is_valid():
        form.save()
        return redirect('assignment_detail', pk=assignment.assignment.id)

    context = {
        'assignment': assignment,
        'filename': x[2],
        'score': score,
        'form': form
    }
    return render(request, 'pages/check_plagiarism.html', context)
