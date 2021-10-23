from django.db import models


class Role(models.IntegerChoices):
    ADMIN = 1
    AUDITOR = 2
    READER = 3


DEFAULT_GROUPS = {
    Role.ADMIN: [
        # Users
        'add_user',
        'change_user',
        'delete_user',
        'view_user',
        # Projects
        'add_project',
        'change_project',
        'delete_project',
        'view_project',
        'add_target',
        'delete_target',
        'view_target',
        'add_targetport',
        'delete_targetport',
        'view_targetport',
        # Executions
        'add_task',
        'delete_task',
        'view_task',
        'view_execution',
        # Findings
        'add_osint',
        'delete_osint',
        'view_osint',
        'add_host',
        'delete_host',
        'view_host',
        'add_enumeration',
        'delete_enumeration',
        'view_enumeration',
        'add_httpendpoint',
        'delete_httpendpoint',
        'view_httpendpoint',
        'add_technology',
        'delete_technology',
        'view_technology',
        'add_vulnerability',
        'change_vulnerability',
        'delete_vulnerability',
        'view_vulnerability',
        'add_credential',
        'delete_credential',
        'view_credential',
        'add_exploit',
        'delete_exploit',
        'view_exploit',
        # Processes
        'add_process',
        'change_process',
        'delete_process',
        'view_process',
        'add_step',
        'change_step',
        'delete_step',
        'view_step',
        # Tools
        'view_tool',
        'view_intensity',
        'view_configuration',
        'view_input',
        'view_output',
    ],
    Role.AUDITOR: [
        # Projects
        'view_project',
        'add_target',
        'delete_target',
        'view_target',
        'add_targetport',
        'delete_targetport',
        'view_targetport',
        # Executions
        'add_task',
        'delete_task',
        'view_task',
        'view_execution',
        # Findings
        'add_osint',
        'delete_osint',
        'view_osint',
        'add_host',
        'delete_host',
        'view_host',
        'add_enumeration',
        'delete_enumeration',
        'view_enumeration',
        'add_httpendpoint',
        'delete_httpendpoint',
        'view_httpendpoint',
        'add_technology',
        'delete_technology',
        'view_technology',
        'add_vulnerability',
        'change_vulnerability',
        'delete_vulnerability',
        'view_vulnerability',
        'add_credential',
        'delete_credential',
        'view_credential',
        'add_exploit',
        'delete_exploit',
        'view_exploit',
        # Processes
        'add_process',
        'change_process',
        'delete_process',
        'view_process',
        'add_step',
        'change_step',
        'delete_step',
        'view_step',
        # Tools
        'view_tool',
        'view_intensity',
        'view_configuration',
        'view_input',
        'view_output',
    ],
    Role.READER: [
        # Projects
        'view_project',
        'view_target',
        'view_targetport',
        # Executions
        'view_task',
        'view_execution',
        # Findings
        'view_osint',
        'view_host',
        'view_enumeration',
        'view_httpendpoint',
        'view_technology',
        'view_vulnerability',
        'view_credential',
        'view_exploit',
    ]
}
