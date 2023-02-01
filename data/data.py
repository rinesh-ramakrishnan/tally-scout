import settings

if settings.SOURCE_TYPE.upper() == 'FILE':
    from .file import raw_data