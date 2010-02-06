

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
        
        path = '%s/' % settings.DOC_ROOT

        if( len( app.split('.') ) > 1 ):
            path += '%s/%s/' % (app.split('.')[-2], app.split('.')[-1])
        else:
            path += '%s/' % app.split('.')[-1]
        
        path += "static"

        # if the static dir exists, add it to the list
        if os.path.exists(path):
            paths.append((app, path))

    return paths
