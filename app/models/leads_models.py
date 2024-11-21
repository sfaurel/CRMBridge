from flask_restx import Namespace, fields

# TODO: Review and keep only relevant fields for the application context.
#       Remove unnecessary fields to optimize performance and fit business needs.


class LeadsModel:

    api = Namespace('leads', description='Leads operations')

    error_model = api.model('Error', {
        'status': fields.String(description='error'),
        'message': fields.String(description='Error description'),
        'details': fields.Raw(description='Error details')
    })

    lead_payload_model = api.model('LeadPayload', {
        'name': fields.String(description='The name of the lead', required=True),
        'notes': fields.String(description='The notes on the lead, on default none', required=False),
        'assigneesEmails': fields.List(fields.String, description="assignees email list, on default assigned to default user", required=False)
    })

    user_entry_model = api.model('UserEntry', {
        'displayName': fields.String(description='Display name of the user'),
        'fullName': fields.String(description='Full name of the user'),
        'email': fields.String(description='Email address'),
        'image': fields.String(description='Profile image URL'),
        'userKey': fields.String(description='Unique user key'),
    })

    stage_history_entry_model = api.model('StageHistoryEntry', {
        'stageKey': fields.String(description='Stage key identifier'),
        'lastEntryToStageTs': fields.Integer(description='Last timestamp of entry to the stage'),
        'timeInStageMs': fields.Integer(description='Time spent in stage in milliseconds'),
    })

    contact_model = api.model('Contact', {
        'isStarred': fields.Boolean(description='If the contact is starred'),
        'isAutoboxed': fields.Boolean(description='If the contact is auto-boxed'),
        'autoboxerKey': fields.String(description='Autoboxer key'),
        'autoboxingTimestamp': fields.Integer(description='Autoboxing timestamp'),
        'autoboxingSource': fields.String(description='Source of autoboxing'),
        'key': fields.String(description='Unique key for the contact'),
    })

    lead_model = api.model('Lead', {
        'lastSavedTimestamp': fields.Integer(description='Last saved timestamp'),
        'boxKey': fields.String(description='Unique box key'),
        'pipelineKey': fields.String(description='Pipeline key identifier'),
        'creatorKey': fields.String(description='Key of the creator'),
        'creationTimestamp': fields.Integer(description='Creation timestamp'),
        'lastUpdatedTimestamp': fields.Integer(description='Last updated timestamp'),
        'lastStageChangeTimestamp': fields.Integer(description='Last stage change timestamp'),
        'totalNumberOfEmails': fields.Integer(description='Total number of emails'),
        'totalNumberOfSentEmails': fields.Integer(description='Total number of sent emails'),
        'totalNumberOfLastSentEmailViews': fields.Integer(description='Total views of the last sent email'),
        'totalNumberOfLastSentEmailLinksClicks': fields.Integer(description='Total clicks on the links of the last sent email'),
        'totalNumberOfSentEmailsViews': fields.Integer(description='Total views of all sent emails'),
        'totalNumberOfReceivedEmails': fields.Integer(description='Total number of received emails'),
        'name': fields.String(description='Name of the CRM entry'),
        'notes': fields.String(description='Notes for the CRM entry'),
        'assignedToSharingEntries': fields.List(fields.Nested(user_entry_model), description='List of assigned users'),
        'creatorSharingEntry': fields.Nested(user_entry_model, description='Details of the creator'),
        'followerSharingEntries': fields.List(fields.Nested(user_entry_model), description='List of followers'),
        'stageKey': fields.String(description='Stage key identifier'),
        'followerKeys': fields.List(fields.String, description='List of follower keys'),
        'linkedBoxKeys': fields.List(fields.String, description='List of linked box keys'),
        'contacts': fields.List(fields.Nested(contact_model), description='List of associated contacts'),
        'emailAddressesAutoExtracted': fields.List(fields.String, description='List of auto-extracted email addresses'),
        'emailAddressesBlacklist': fields.List(fields.String, description='List of blacklisted email addresses'),
        'emailAddresses': fields.List(fields.String, description='List of email addresses'),
        'taskCompleteCount': fields.Integer(description='Number of completed tasks'),
        'taskIncompleteCount': fields.Integer(description='Number of incomplete tasks'),
        'taskOverdueCount': fields.Integer(description='Number of overdue tasks'),
        'taskAssigneeKeySet': fields.List(fields.String, description='Keys of task assignees'),
        'overdueTaskAssigneeKeySet': fields.List(fields.String, description='Keys of overdue task assignees'),
        'incompleteTaskAssigneeKeySet': fields.List(fields.String, description='Keys of incomplete task assignees'),
        'taskAssigneeSharingEntrySet': fields.List(fields.String, description='Sharing entry keys for task assignees'),
        'overdueTaskAssigneeSharingEntrySet': fields.List(fields.String, description='Sharing entry keys for overdue task assignees'),
        'incompleteTaskAssigneeSharingEntrySet': fields.List(fields.String, description='Sharing entry keys for incomplete task assignees'),
        'taskPercentageComplete': fields.Float(description='Percentage of tasks completed'),
        'taskTotal': fields.Integer(description='Total number of tasks'),
        'callLogCount': fields.Integer(description='Count of call logs'),
        'meetingNotesCount': fields.Integer(description='Count of meeting notes'),
        'totalCallLogDuration': fields.Integer(description='Total duration of call logs'),
        'totalMeetingNotesDuration': fields.Integer(description='Total duration of meeting notes'),
        'followerCount': fields.Integer(description='Number of followers'),
        'commentCount': fields.Integer(description='Number of comments'),
        'gmailThreadCount': fields.Integer(description='Count of Gmail threads'),
        'fileCount': fields.Integer(description='Count of files'),
        'fields': fields.Raw(description='Custom fields as a dictionary'),
        'stageHistoryEntries': fields.List(fields.Nested(stage_history_entry_model), description='History of stage changes'),
        'key': fields.String(description='Unique key for the CRM entry'),
        'freshness': fields.Float(description='Freshness score'),
    })
