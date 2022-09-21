import urllib.parse
import os


def get_valid_dsn():
    dir_path = os.path.normpath(os.path.dirname(os.path.dirname(__file__)))
    file_path = os.path.join(dir_path, 'secrets\\postgres_dsn')
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as dsn_file:
            db_dsn_str = dsn_file.readline()
    else:
        print('There is no dsn string at ../secrets/postgres_dsn')
        db_dsn_str = input('enter dsn string here:')

    parsing_dsn_result = urllib.parse.urlparse(db_dsn_str)
    username_raw = parsing_dsn_result.username
    password_raw = parsing_dsn_result.password

    username_safe = urllib.parse.quote_plus(username_raw)
    password_safe = urllib.parse.quote_plus(password_raw)

    parsing_dsn_result._replace(
        netloc=f'{username_safe}:{password_safe}@{parsing_dsn_result.hostname}:{parsing_dsn_result.port}')
    return urllib.parse.urlunparse(parsing_dsn_result)