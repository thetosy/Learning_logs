from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .forms import TopicForm, EntryForm
from .models import Topic, Entry


# Create your views here.
def index(request):
    """The main homepage"""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """show all the topics created"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """show a single topic and the associated entries"""
    topic = get_object_or_404(Topic, id=topic_id)
    # verifies if the topic belongs to the current user
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """Add new topic"""
    if request.method != 'POST':
        # create blank form
        form = TopicForm()
    else:
        # validate data in filled form and pass into database
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
    # display blank/invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry to a topic"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # create blank form
        form = EntryForm()
    else:
        # validate, and add to database
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            # link the topic to the entry
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # display blank/invalid forms
    context = {'form': form, 'topic': topic}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """edit existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # verifies if the entry belongs to the current user
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # fill the form with the previous entry data
        form = EntryForm(instance=entry)
    else:
        # update the form with the new data
        form = EntryForm(instance=entry, data=request.POST)
        # validate and save into database
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic.id)

    # display form to edit or if form is invalid
    context = {'form': form, 'topic': topic, 'entry': entry}
    return render(request, 'learning_logs/edit_entry.html', context)
