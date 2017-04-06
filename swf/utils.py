import boto.swf
import os

from swf.event import Event

aws_swf_l1 = boto.swf.layer1.Layer1(
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'))


def fetch_events(domain, run_id, workflow_id):
    events = {}
    completed = False
    while not completed:
        history = aws_swf_l1.get_workflow_execution_history(
            domain=domain,
            run_id=run_id,
            workflow_id=workflow_id)
        for event in history['events']:
            if event['eventId'] not in events:
                yield event
            events.update({event['eventId']: Event(event)})

            if event['eventType'] == 'WorkflowExecutionCompleted':
                completed = True


def all_regions():
    return boto.swf.get_regions('swf')
