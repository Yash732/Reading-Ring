from django.contrib.auth.models import User
from django.db import models
from item.models import Item
# item: A foreign key to the Item model, indicating which item the conversation is about. 
# The related_name='conversations' allows accessing all conversations related to a particular item using item.conversations.

class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name = 'conversations',on_delete= models.CASCADE)
    #members of the convo
    members = models.ManyToManyField(User, related_name = 'conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',) #most recently updated conversations appear first (- means descending order)

class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name = 'messages', on_delete =models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name = 'created_messages',on_delete = models.CASCADE) # if the user is deleted then delete all the messages



