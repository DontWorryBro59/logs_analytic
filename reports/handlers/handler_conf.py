import re


class HandlerConf:

    @property
    def all_levels(self) -> list[str]:
        """Return all levels.
        Example:
            ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        """
        all_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        return all_levels

    @property
    def handler_pattern(self) -> re.Pattern:
        """Return pattern for handler.
        Example:
            ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3} (?P<level>DEBUG|INFO|WARNING|ERROR|CRITICAL) .*?: .*?(?P<path>/[^\s\[]+)
        """
        handler_pattern = re.compile(
            r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3} '
            r'(?P<level>DEBUG|INFO|WARNING|ERROR|CRITICAL) .*?: .*?(?P<path>/[^\s\[]+)'
        )
        return handler_pattern


config = HandlerConf()
