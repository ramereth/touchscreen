

def get_plugin_static_dirs():
    """
    function for building a list of paths for plugin static directories
    This allows the paths to be added automatically rather than require
    additional configuration for the plugins
    """
    import os
    from django.conf import settings

    paths = []
    for app in settings.INSTALLED_APPS:
        path = '%s/%s/static' % (settings.DOC_ROOT, app.split('.')[-1])

        # if the static dir exists, add it to the list
        if os.path.exists(path):
            paths.append((app, path))

    return paths