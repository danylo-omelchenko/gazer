class BaseAttribute:
    def __init__(self, attributes):
        self.attributes = attributes


class ChildWorkflowExecutionCompletedEventAttributes(BaseAttribute):
    @property
    def workflow_type(self):
        return self.attributes['workflowType']

    @property
    def started_event_id(self):
        return self.attributes['startedEventId']

    @property
    def workflow_execution(self):
        return self.attributes['workflowExecution']

    @property
    def result(self):
        return self.attributes['result']

    @property
    def initiated_event_id(self):
        return self.attributes['initiatedEventId']


class WorkflowExecutionCanceledEventAttributes(BaseAttribute):
    @property
    def decision_task_completed_event_id(self):
        return self.attributes['decisionTaskCompletedEventId']

    @property
    def details(self):
        return self.attributes['details']


class ActivityTaskCanceledEventAttributes(BaseAttribute):
    @property
    def latest_cancel_requested_event_id(self):
        return self.attributes['latestCancelRequestedEventId']

    @property
    def details(self):
        return self.attributes['details']

    @property
    def started_event_id(self):
        return self.attributes['startedEventId']

    @property
    def scheduled_event_id(self):
        return self.attributes['scheduledEventId']


class ChildWorkflowExecutionTerminatedEventAttributes(BaseAttribute):
    @property
    def workflow_type(self):
        return self.attributes['workflowType']

    @property
    def started_event_id(self):
        return self.attributes['startedEventId']

    @property
    def workflow_execution(self):
        return self.attributes['workflowExecution']

    @property
    def initiated_event_id(self):
        return self.attributes['initiatedEventId']


class RequestCancelExternalWorkflowExecutionFailedEventAttributes(BaseAttribute):
    @property
    def decision_task_completed_event_id(self):
        return self.attributes['decisionTaskCompletedEventId']

    @property
    def cause(self):
        return self.attributes['cause']

    @property
    def control(self):
        return self.attributes['control']

    @property
    def run_id(self):
        return self.attributes['runId']

    @property
    def workflow_id(self):
        return self.attributes['workflowId']

    @property
    def initiated_event_id(self):
        return self.attributes['initiatedEventId']


class MarkerRecordedEventAttributes(BaseAttribute):
    @property
    def decision_task_completed_event_id(self):
        return self.attributes['decisionTaskCompletedEventId']

    @property
    def details(self):
        return self.attributes['details']

    @property
    def marker_name(self):
        return self.attributes['markerName']


class LambdaFunctionScheduledEventAttributes(BaseAttribute):
    @property
    def decision_task_completed_event_id(self):
        return self.attributes['decisionTaskCompletedEventId']

    @property
    def input(self):
        return self.attributes['input']

    @property
    def id(self):
        return self.attributes['id']

    @property
    def name(self):
        return self.attributes['name']

    @property
    def start_to_close_timeout(self):
        return self.attributes['startToCloseTimeout']


class ChildWorkflowExecutionFailedEventAttributes(BaseAttribute):
    @property
    def details(self):
        return self.attributes['details']

    @property
    def workflow_execution(self):
        return self.attributes['workflowExecution']

    @property
    def initiated_event_id(self):
        return self.attributes['initiatedEventId']

    @property
    def reason(self):
        return self.attributes['reason']

    @property
    def workflow_type(self):
        return self.attributes['workflowType']

    @property
    def started_event_id(self):
        return self.attributes['startedEventId']


class WorkflowExecutionFailedEventAttributes(BaseAttribute):
    @property
    def decision_task_completed_event_id(self):
        return self.attributes['decisionTaskCompletedEventId']

    @property
    def details(self):
        return self.attributes['details']

    @property
    def reason(self):
        return self.attributes['reason']


class TimerCanceledEventAttributes(BaseAttribute):
    @property
    def decision_task_completed_event_id(self):
        return self.attributes['decisionTaskCompletedEventId']

    @property
    def timer_id(self):
        return self.attributes['timerId']

    @property
    def started_event_id(self):
        return self.attributes['startedEventId']


class ScheduleActivityTaskFailedEventAttributes(BaseAttribute):
    @property
    def activity_id(self):
        return self.attributes['activityId']

    @property
    def cause(self):
        return self.attributes['cause']

    @property
    def activity_type(self):
        return self.attributes['activityType']

    @property
    def decision_task_completed_event_id(self):
        return self.attributes['decisionTaskCompletedEventId']


class WorkflowExecutionCompletedEventAttributes(BaseAttribute):
    @property
    def decision_task_completed_event_id(self):
        return self.attributes['decisionTaskCompletedEventId']

    @property
    def result(self):
        return self.attributes['result']


class StartChildWorkflowExecutionFailedEventAttributes(BaseAttribute):
    @property
    def decision_task_completed_event_id(self):
        return self.attributes['decisionTaskCompletedEventId']

    @property
    def cause(self):
        return self.attributes['cause']

    @property
    def control(self):
        return self.attributes['control']

    @property
    def workflow_type(self):
        return self.attributes['workflowType']

    @property
    def workflow_id(self):
        return self.attributes['workflowId']

    @property
    def initiated_event_id(self):
        return self.attributes['initiatedEventId']


class StartChildWorkflowExecutionInitiatedEventAttributes(BaseAttribute):
    @property
    def child_policy(self):
        return self.attributes['childPolicy']

    @property
    def execution_start_to_close_timeout(self):
        return self.attributes['executionStartToCloseTimeout']

    @property
    def input(self):
        return self.attributes['input']

    @property
    def lambda_role(self):
        return self.attributes['lambdaRole']

    @property
    def task_start_to_close_timeout(self):
        return self.attributes['taskStartToCloseTimeout']

    @property
    def decision_task_completed_event_id(self):
        return self.attributes['decisionTaskCompletedEventId']

    @property
    def tag_list(self):
        return self.attributes['tagList']

    @property
    def control(self):
        return self.attributes['control']

    @property
    def workflow_type(self):
        return self.attributes['workflowType']

    @property
    def task_priority(self):
        return self.attributes['taskPriority']

    @property
    def workflow_id(self):
        return self.attributes['workflowId']

    @property
    def task_list(self):
        return self.attributes['taskList']


class DecisionTaskCompletedEventAttributes(BaseAttribute):
    @property
    def started_event_id(self):
        return self.attributes['startedEventId']

    @property
    def scheduled_event_id(self):
        return self.attributes['scheduledEventId']

    @property
    def execution_context(self):
        return self.attributes['executionContext']


class DecisionTaskScheduledEventAttributes(BaseAttribute):
    @property
    def start_to_close_timeout(self):
        return self.attributes['startToCloseTimeout']

    @property
    def task_priority(self):
        return self.attributes['taskPriority']

    @property
    def task_list(self):
        return self.attributes['taskList']


class StartTimerFailedEventAttributes(BaseAttribute):
    @property
    def decision_task_completed_event_id(self):
        return self.attributes['decisionTaskCompletedEventId']

    @property
    def cause(self):
        return self.attributes['cause']

    @property
    def timer_id(self):
        return self.attributes['timerId']


class WorkflowExecutionCancelRequestedEventAttributes(BaseAttribute):
    @property
    def cause(self):
        return self.attributes['cause']

    @property
    def external_workflow_execution(self):
        return self.attributes['externalWorkflowExecution']

    @property
    def external_initiated_event_id(self):
        return self.attributes['externalInitiatedEventId']


class LambdaFunctionStartedEventAttributes(BaseAttribute):
    @property
    def scheduled_event_id(self):
        return self.attributes['scheduledEventId']


class ChildWorkflowExecutionTimedOutEventAttributes(BaseAttribute):
    @property
    def workflow_type(self):
        return self.attributes['workflowType']

    @property
    def started_event_id(self):
        return self.attributes['startedEventId']

    @property
    def workflow_execution(self):
        return self.attributes['workflowExecution']

    @property
    def initiated_event_id(self):
        return self.attributes['initiatedEventId']

    @property
    def timeout_type(self):
        return self.attributes['timeoutType']


class RequestCancelActivityTaskFailedEventAttributes(BaseAttribute):
    @property
    def activity_id(self):
        return self.attributes['activityId']

    @property
    def cause(self):
        return self.attributes['cause']

    @property
    def decision_task_completed_event_id(self):
        return self.attributes['decisionTaskCompletedEventId']


class SignalExternalWorkflowExecutionInitiatedEventAttributes(BaseAttribute):
    @property
    def decision_task_completed_event_id(self):
        return self.attributes['decisionTaskCompletedEventId']

    @property
    def run_id(self):
        return self.attributes['runId']

    @property
    def control(self):
        return self.attributes['control']

    @property
    def input(self):
        return self.attributes['input']

    @property
    def workflow_id(self):
        return self.attributes['workflowId']

    @property
    def signal_name(self):
        return self.attributes['signalName']


class TimerStartedEventAttributes(BaseAttribute):
    @property
    def decision_task_completed_event_id(self):
        return self.attributes['decisionTaskCompletedEventId']

    @property
    def timer_id(self):
        return self.attributes['timerId']

    @property
    def start_to_fire_timeout(self):
        return self.attributes['startToFireTimeout']

    @property
    def control(self):
        return self.attributes['control']


class ActivityTaskScheduledEventAttributes(BaseAttribute):
    @property
    def activity_id(self):
        return self.attributes['activityId']

    @property
    def decision_task_completed_event_id(self):
        return self.attributes['decisionTaskCompletedEventId']

    @property
    def activity_type(self):
        return self.attributes['activityType']

    @property
    def control(self):
        return self.attributes['control']

    @property
    def task_priority(self):
        return self.attributes['taskPriority']

    @property
    def input(self):
        return self.attributes['input']

    @property
    def schedule_to_close_timeout(self):
        return self.attributes['scheduleToCloseTimeout']

    @property
    def schedule_to_start_timeout(self):
        return self.attributes['scheduleToStartTimeout']

    @property
    def heartbeat_timeout(self):
        return self.attributes['heartbeatTimeout']

    @property
    def start_to_close_timeout(self):
        return self.attributes['startToCloseTimeout']

    @property
    def task_list(self):
        return self.attributes['taskList']


class ChildWorkflowExecutionCanceledEventAttributes(BaseAttribute):
    @property
    def details(self):
        return self.attributes['details']

    @property
    def started_event_id(self):
        return self.attributes['startedEventId']

    @property
    def workflow_execution(self):
        return self.attributes['workflowExecution']

    @property
    def initiated_event_id(self):
        return self.attributes['initiatedEventId']

    @property
    def workflow_type(self):
        return self.attributes['workflowType']


class WorkflowExecutionTerminatedEventAttributes(BaseAttribute):
    @property
    def cause(self):
        return self.attributes['cause']

    @property
    def child_policy(self):
        return self.attributes['childPolicy']

    @property
    def reason(self):
        return self.attributes['reason']

    @property
    def details(self):
        return self.attributes['details']


class WorkflowExecutionTimedOutEventAttributes(BaseAttribute):
    @property
    def child_policy(self):
        return self.attributes['childPolicy']

    @property
    def timeout_type(self):
        return self.attributes['timeoutType']


class LambdaFunctionTimedOutEventAttributes(BaseAttribute):
    @property
    def started_event_id(self):
        return self.attributes['startedEventId']

    @property
    def scheduled_event_id(self):
        return self.attributes['scheduledEventId']

    @property
    def timeout_type(self):
        return self.attributes['timeoutType']


class ExternalWorkflowExecutionSignaledEventAttributes(BaseAttribute):
    @property
    def workflow_execution(self):
        return self.attributes['workflowExecution']

    @property
    def initiated_event_id(self):
        return self.attributes['initiatedEventId']


class WorkflowExecutionSignaledEventAttributes(BaseAttribute):
    @property
    def input(self):
        return self.attributes['input']

    @property
    def signal_name(self):
        return self.attributes['signalName']

    @property
    def external_workflow_execution(self):
        return self.attributes['externalWorkflowExecution']

    @property
    def external_initiated_event_id(self):
        return self.attributes['externalInitiatedEventId']


class DecisionTaskStartedEventAttributes(BaseAttribute):
    @property
    def identity(self):
        return self.attributes['identity']

    @property
    def scheduled_event_id(self):
        return self.attributes['scheduledEventId']


class CompleteWorkflowExecutionFailedEventAttributes(BaseAttribute):
    @property
    def decision_task_completed_event_id(self):
        return self.attributes['decisionTaskCompletedEventId']

    @property
    def cause(self):
        return self.attributes['cause']


class LambdaFunctionCompletedEventAttributes(BaseAttribute):
    @property
    def scheduled_event_id(self):
        return self.attributes['scheduledEventId']

    @property
    def started_event_id(self):
        return self.attributes['startedEventId']

    @property
    def result(self):
        return self.attributes['result']


class ActivityTaskCancelRequestedEventAttributes(BaseAttribute):
    @property
    def activity_id(self):
        return self.attributes['activityId']

    @property
    def decision_task_completed_event_id(self):
        return self.attributes['decisionTaskCompletedEventId']


class RecordMarkerFailedEventAttributes(BaseAttribute):
    @property
    def decision_task_completed_event_id(self):
        return self.attributes['decisionTaskCompletedEventId']

    @property
    def cause(self):
        return self.attributes['cause']

    @property
    def marker_name(self):
        return self.attributes['markerName']


class LambdaFunctionFailedEventAttributes(BaseAttribute):
    @property
    def details(self):
        return self.attributes['details']

    @property
    def started_event_id(self):
        return self.attributes['startedEventId']

    @property
    def scheduled_event_id(self):
        return self.attributes['scheduledEventId']

    @property
    def reason(self):
        return self.attributes['reason']


class RequestCancelExternalWorkflowExecutionInitiatedEventAttributes(BaseAttribute):
    @property
    def decision_task_completed_event_id(self):
        return self.attributes['decisionTaskCompletedEventId']

    @property
    def run_id(self):
        return self.attributes['runId']

    @property
    def workflow_id(self):
        return self.attributes['workflowId']

    @property
    def control(self):
        return self.attributes['control']


class ChildWorkflowExecutionStartedEventAttributes(BaseAttribute):
    @property
    def workflow_type(self):
        return self.attributes['workflowType']

    @property
    def workflow_execution(self):
        return self.attributes['workflowExecution']

    @property
    def initiated_event_id(self):
        return self.attributes['initiatedEventId']


class FailWorkflowExecutionFailedEventAttributes(BaseAttribute):
    @property
    def decision_task_completed_event_id(self):
        return self.attributes['decisionTaskCompletedEventId']

    @property
    def cause(self):
        return self.attributes['cause']


class WorkflowExecutionStartedEventAttributes(BaseAttribute):
    @property
    def child_policy(self):
        return self.attributes['childPolicy']

    @property
    def continued_execution_run_id(self):
        return self.attributes['continuedExecutionRunId']

    @property
    def execution_start_to_close_timeout(self):
        return self.attributes['executionStartToCloseTimeout']

    @property
    def input(self):
        return self.attributes['input']

    @property
    def lambda_role(self):
        return self.attributes['lambdaRole']

    @property
    def task_start_to_close_timeout(self):
        return self.attributes['taskStartToCloseTimeout']

    @property
    def parent_initiated_event_id(self):
        return self.attributes['parentInitiatedEventId']

    @property
    def tag_list(self):
        return self.attributes['tagList']

    @property
    def task_list(self):
        return self.attributes['taskList']

    @property
    def parent_workflow_execution(self):
        return self.attributes['parentWorkflowExecution']

    @property
    def workflow_type(self):
        return self.attributes['workflowType']

    @property
    def task_priority(self):
        return self.attributes['taskPriority']


class WorkflowExecutionContinuedAsNewEventAttributes(BaseAttribute):
    @property
    def decision_task_completed_event_id(self):
        return self.attributes['decisionTaskCompletedEventId']

    @property
    def child_policy(self):
        return self.attributes['childPolicy']

    @property
    def tag_list(self):
        return self.attributes['tagList']

    @property
    def task_list(self):
        return self.attributes['taskList']

    @property
    def execution_start_to_close_timeout(self):
        return self.attributes['executionStartToCloseTimeout']

    @property
    def task_priority(self):
        return self.attributes['taskPriority']

    @property
    def input(self):
        return self.attributes['input']

    @property
    def lambda_role(self):
        return self.attributes['lambdaRole']

    @property
    def workflow_type(self):
        return self.attributes['workflowType']

    @property
    def task_start_to_close_timeout(self):
        return self.attributes['taskStartToCloseTimeout']

    @property
    def new_execution_run_id(self):
        return self.attributes['newExecutionRunId']


class CancelWorkflowExecutionFailedEventAttributes(BaseAttribute):
    @property
    def decision_task_completed_event_id(self):
        return self.attributes['decisionTaskCompletedEventId']

    @property
    def cause(self):
        return self.attributes['cause']


class TimerFiredEventAttributes(BaseAttribute):
    @property
    def timer_id(self):
        return self.attributes['timerId']

    @property
    def started_event_id(self):
        return self.attributes['startedEventId']


class ScheduleLambdaFunctionFailedEventAttributes(BaseAttribute):
    @property
    def decision_task_completed_event_id(self):
        return self.attributes['decisionTaskCompletedEventId']

    @property
    def cause(self):
        return self.attributes['cause']

    @property
    def id(self):
        return self.attributes['id']

    @property
    def name(self):
        return self.attributes['name']


class ActivityTaskCompletedEventAttributes(BaseAttribute):
    @property
    def scheduled_event_id(self):
        return self.attributes['scheduledEventId']

    @property
    def started_event_id(self):
        return self.attributes['startedEventId']

    @property
    def result(self):
        return self.attributes['result']


class DecisionTaskTimedOutEventAttributes(BaseAttribute):
    @property
    def started_event_id(self):
        return self.attributes['startedEventId']

    @property
    def scheduled_event_id(self):
        return self.attributes['scheduledEventId']

    @property
    def timeout_type(self):
        return self.attributes['timeoutType']


class ContinueAsNewWorkflowExecutionFailedEventAttributes(BaseAttribute):
    @property
    def decision_task_completed_event_id(self):
        return self.attributes['decisionTaskCompletedEventId']

    @property
    def cause(self):
        return self.attributes['cause']


class SignalExternalWorkflowExecutionFailedEventAttributes(BaseAttribute):
    @property
    def decision_task_completed_event_id(self):
        return self.attributes['decisionTaskCompletedEventId']

    @property
    def cause(self):
        return self.attributes['cause']

    @property
    def control(self):
        return self.attributes['control']

    @property
    def run_id(self):
        return self.attributes['runId']

    @property
    def workflow_id(self):
        return self.attributes['workflowId']

    @property
    def initiated_event_id(self):
        return self.attributes['initiatedEventId']


class ActivityTaskStartedEventAttributes(BaseAttribute):
    @property
    def identity(self):
        return self.attributes['identity']

    @property
    def scheduled_event_id(self):
        return self.attributes['scheduledEventId']


class ExternalWorkflowExecutionCancelRequestedEventAttributes(BaseAttribute):
    @property
    def workflow_execution(self):
        return self.attributes['workflowExecution']

    @property
    def initiated_event_id(self):
        return self.attributes['initiatedEventId']


class ActivityTaskTimedOutEventAttributes(BaseAttribute):
    @property
    def details(self):
        return self.attributes['details']

    @property
    def started_event_id(self):
        return self.attributes['startedEventId']

    @property
    def scheduled_event_id(self):
        return self.attributes['scheduledEventId']

    @property
    def timeout_type(self):
        return self.attributes['timeoutType']


class CancelTimerFailedEventAttributes(BaseAttribute):
    @property
    def decision_task_completed_event_id(self):
        return self.attributes['decisionTaskCompletedEventId']

    @property
    def cause(self):
        return self.attributes['cause']

    @property
    def timer_id(self):
        return self.attributes['timerId']


class StartLambdaFunctionFailedEventAttributes(BaseAttribute):
    @property
    def cause(self):
        return self.attributes['cause']

    @property
    def scheduled_event_id(self):
        return self.attributes['scheduledEventId']

    @property
    def message(self):
        return self.attributes['message']


class ActivityTaskFailedEventAttributes(BaseAttribute):
    @property
    def details(self):
        return self.attributes['details']

    @property
    def started_event_id(self):
        return self.attributes['startedEventId']

    @property
    def scheduled_event_id(self):
        return self.attributes['scheduledEventId']

    @property
    def reason(self):
        return self.attributes['reason']
