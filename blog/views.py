from django.forms import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
from blog.models import Comment
from django.shortcuts import render, get_object_or_404


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')

# IMPLEMENT THE COMMENT VIEWS HERE. THANKS

def comment_add(request):
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = comment
            comment.save()
            return redirect('post_detail')
    else:
        form = CommentForm()
    return render(request, 'comments/comment.html', {'form': form})

# def comment_remove(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     comment.delete()
#     return redirect('post_detail', pk=comment.post.pk)  

