import swf.attributes as attributes


class Event:
    def __init__(self, event):
        self.event = event

    @property
    def id(self):
        return self.event['eventId']

    @property
    def type(self):
        return self.event['eventType']

    @property
    def timestamp(self):
        return self.event['eventTimestamp']

    @property
    def attributes(self):
        attributes_name = self.type + 'EventAttributes'
        attributes_class = getattr(attributes, attributes_name)
        return attributes_class(self.event[attributes_name])


class EventType:
    ACTIVITY_TASK_CANCELED = 'ActivityTaskCanceled'
    ACTIVITY_TASK_CANCEL_REQUESTED = 'ActivityTaskCancelRequested'
    ACTIVITY_TASK_COMPLETED = 'ActivityTaskCompleted'
    ACTIVITY_TASK_FAILED = 'ActivityTaskFailed'
    ACTIVITY_TASK_SCHEDULED = 'ActivityTaskScheduled'
    ACTIVITY_TASK_STARTED = 'ActivityTaskStarted'
    ACTIVITY_TASK_TIMED_OUT = 'ActivityTaskTimedOut'

    CANCEL_TIMER_FAILED = 'CancelTimerFailed'
    CANCEL_WORKFLOW_EXECUTION_FAILED = 'CancelWorkflowExecutionFailed'

    CHILD_WORKFLOW_EXECUTION_CANCELED = 'ChildWorkflowExecutionCanceled'
    CHILD_WORKFLOW_EXECUTION_COMPLETED = 'ChildWorkflowExecutionCompleted'
    CHILD_WORKFLOW_EXECUTION_FAILED = 'ChildWorkflowExecutionFailed'
    CHILD_WORKFLOW_EXECUTION_STARTED = 'ChildWorkflowExecutionStarted'
    CHILD_WORKFLOW_EXECUTION_TERMINATED = 'ChildWorkflowExecutionTerminated'
    CHILD_WORKFLOW_EXECUTION_TIMED_OUT = 'ChildWorkflowExecutionTimedOut'

    COMPLETE_WORKFLOW_EXECUTION_FAILED = 'CompleteWorkflowExecutionFailed'

    CONTINUE_AS_NEW_WORKFLOW_EXECUTION_FAILED = (
        'ContinueAsNewWorkflowExecutionFailed')

    DECISION_TASK_COMPLETED = 'DecisionTaskCompleted'
    DECISION_TASK_SCHEDULED = 'DecisionTaskScheduled'
    DECISION_TASK_STARTED = 'DecisionTaskStarted'
    DECISION_TASK_TIMED_OUT = 'DecisionTaskTimedOut'

    EXTERNAL_WORKFLOW_EXECUTION_CANCEL_REQUESTED = (
        'ExternalWorkflowExecutionCancelRequested')
    EXTERNAL_WORKFLOW_EXECUTION_SIGNALED = 'ExternalWorkflowExecutionSignaled'

    FAIL_WORKFLOW_EXECUTION_FAILED = 'FailWorkflowExecutionFailed'

    LAMBDA_FUNCTION_COMPLETED = 'LambdaFunctionCompleted'
    LAMBDA_FUNCTION_FAILED = 'LambdaFunctionFailed'
    LAMBDA_FUNCTION_SCHEDULED = 'LambdaFunctionScheduled'
    LAMBDA_FUNCTION_STARTED = 'LambdaFunctionStarted'
    LAMBDA_FUNCTION_TIMED_OUT = 'LambdaFunctionTimedOut'

    MARKER_RECORDED = 'MarkerRecorded'

    RECORD_MARKER_FAILED = 'RecordMarkerFailed'
    REQUEST_CANCEL_ACTIVITY_TASK_FAILED = 'RequestCancelActivityTaskFailed'
    REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_FAILED = (
        'RequestCancelExternalWorkflowExecutionFailed')
    REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_INITIATED = (
        'RequestCancelExternalWorkflowExecutionInitiated')

    SCHEDULE_ACTIVITY_TASK_FAILED = 'ScheduleActivityTaskFailed'
    SCHEDULE_LAMBDA_FUNCTION_FAILED = 'ScheduleLambdaFunctionFailed'

    SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_FAILED = (
        'SignalExternalWorkflowExecutionFailed')
    SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_INITIATED = (
        'SignalExternalWorkflowExecutionInitiated')

    START_CHILD_WORKFLOW_EXECUTION_FAILED = 'StartChildWorkflowExecutionFailed'
    START_CHILD_WORKFLOW_EXECUTION_INITIATED = (
        'StartChildWorkflowExecutionInitiated')
    START_LAMBDA_FUNCTION_FAILED = 'StartLambdaFunctionFailed'
    START_TIMER_FAILED = 'StartTimerFailed'

    TIMER_CANCELED = 'TimerCanceled'
    TIMER_FIRED = 'TimerFired'
    TIMER_STARTED = 'TimerStarted'

    WORKFLOW_EXECUTION_CANCELED = 'WorkflowExecutionCanceled'
    WORKFLOW_EXECUTION_CANCEL_REQUESTED = 'WorkflowExecutionCancelRequested'
    WORKFLOW_EXECUTION_COMPLETED = 'WorkflowExecutionCompleted'
    WORKFLOW_EXECUTION_CONTINUED_AS_NEW = 'WorkflowExecutionContinuedAsNew'
    WORKFLOW_EXECUTION_FAILED = 'WorkflowExecutionFailed'
    WORKFLOW_EXECUTION_SIGNALED = 'WorkflowExecutionSignaled'
    WORKFLOW_EXECUTION_STARTED = 'WorkflowExecutionStarted'
    WORKFLOW_EXECUTION_TERMINATED = 'WorkflowExecutionTerminated'
    WORKFLOW_EXECUTION_TIMED_OUT = 'WorkflowExecutionTimedOut'
