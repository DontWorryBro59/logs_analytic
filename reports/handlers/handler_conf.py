import re


class HandlerConf:

    @property
    def all_levels(self) -> list[str]:
        all_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        return all_levels

    @property
    def handler_pattern(self) -> re.Pattern:
        handler_pattern = re.compile(
            r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3} '
            r'(?P<level>DEBUG|INFO|WARNING|ERROR|CRITICAL) .*?: .*?(?P<path>/[^\s\[]+)'
        )
        return handler_pattern
