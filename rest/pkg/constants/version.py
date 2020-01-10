from pkg.utils.git import get_top_commit


APP_NAME = 'MyBeer'
SERVER_NAME = f'{APP_NAME} REST server'
SERVER_VERSION = '0.01'


def get_server_version_full():
    commit = get_top_commit()
    commit_str = f'.{commit}' if commit else ''
    return f'{SERVER_VERSION}{commit_str}'


SERVER_VERSION_FULL = get_server_version_full()
SOFTWARE_VERSION = f'{SERVER_NAME} v{SERVER_VERSION_FULL}'
