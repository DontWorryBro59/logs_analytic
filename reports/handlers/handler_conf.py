import re


class HandlerConf:
    all_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    handler_pattern = re.compile(
        r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3} '
        r'(?P<level>DEBUG|INFO|WARNING|ERROR|CRITICAL) .*?: .*?(?P<path>/[^\s\[]+)'
    )
