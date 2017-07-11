import json
import sys
import os
sys.path.append(os.path.join(os.getcwd(),'..','..'))
import watson_developer_cloud
conversation = watson_developer_cloud.ConversationV1(username='af8cb2e5-4feb-428c-968b-bac51e881bd6',password='NrNTEYonJpaY',version='2017-04-21')
# check workspace status (wait for training to complete)
workspace = conversation.get_workspace(workspace_id='dd52e3f6-fe5d-405f-acd3-98506b64a303')
print('The workspace status is: {0}'.format(workspace['status']))

iptext=raw_input("enter question")
message_input = {'text': iptext}
response = conversation.message(workspace_id='dd52e3f6-fe5d-405f-acd3-98506b64a303',message_input=message_input)

print response["output"]["text"][0]

p=message_input['text']
while p!= "exit":
	iptext=raw_input("enter question")
	message_input = {'text': iptext}
	response = conversation.message(workspace_id='dd52e3f6-fe5d-405f-acd3-98506b64a303',message_input=message_input)

	print response["output"]["text"][0]
