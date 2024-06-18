from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.
from item.models import Item
from .forms import ConversationMessageForm
from .models import Conversation

@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk = item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversation = Conversation.objects.filter(item =item).filter(members__in =[request.user.id])

    if conversation:
        # the conversation already exists
        return redirect('conversation:detail', pk = conversation.first().id)
    if request.method == 'POST':
        #creating a new conversation
        form = ConversationMessageForm(request.POST)
        
        if form.is_valid():

            conversation = Conversation.objects.create(item = item)

            # adding the user and the owner of the item to the members list
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit = False)
            #reference to the conversation and who created it
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk = item_pk)
    else:
        form = ConversationMessageForm()
    return render(request, 'conversation/new.html',{
        'form' : form,
    })


@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in =[request.user.id])

    return render(request, 'conversation/inbox.html',{
        'conversations' : conversations
    } )

#this pk is for the conversation not the item

@login_required
def detail(request,pk):
    conversation = Conversation.objects.filter(members__in =[request.user.id]).get(pk = pk)

    #if the send message form is submitted (when contacting seller)
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        
        #if the submitted form is valid then create a convo
        if form.is_valid():
            conversation_message = form.save(commit = False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()
        return redirect('conversation:detail',pk = pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/detail.html',{
        'conversation': conversation,
        'form':form
    })

