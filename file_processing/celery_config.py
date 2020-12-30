from datetime import timedelta


class CeleryConf:
    CELERY_IMPORTS = 'app.tasks'
    CELERY_TASK_RESULT_EXPIRES = 30
    CELERY_TIMEZONE = 'UTC'

    CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'

    CELERYBEAT_SCHEDULE = {
        'test-celery': {
            'task': 'delete_temporary_files_periodically',
            'schedule': timedelta(seconds=30),
        }
    }