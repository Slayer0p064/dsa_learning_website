from django.shortcuts import render, get_object_or_404
from .models import DSATopic
from django.http import HttpResponse
from django.template.loader import render_to_string

def home(request):
    topics = [
        "Arrays", "Strings", "Linked Lists", "Stacks", "Queues", "Recursion",
        "Sorting Algorithms", "Searching Algorithms", "Hashing", "Trees", "Graphs",
        "Dynamic Programming", "Greedy Algorithms", "Backtracking",
        "Bit Manipulation", "Trie (Prefix Tree)"
    ]
    return render(request, 'dsa/home.html', {'topics': topics})

def topic_detail(request, topic_name):
    return render(request, f'dsa/topics/{topic_name.lower().replace(" ", "_")}.html', {'topic_name': topic_name})


def topic_view(request, topic_name):
    return render(request, f'topics/{topic_name}.html')