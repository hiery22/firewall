from src.firewall.command import command
from src.firewall.ui import FirewallUI
from src.firewall.logger.logger import Logger


class Controller:
    def __init__(self, logger: Logger):
        self.logger: Logger = logger

    @command("Block")
    async def block_command(self, arg: str):
        if arg == "":
            self.logger.info("Nothing Blocked")
        else:
            self.logger.info(f"Blocked: {arg}")

    @command("Allow")
    async def allow_command(self, arg: str):
        if arg == "":
            self.logger.info("Nothing Allowed")
        else:
            self.logger.info(f"Allowed: {arg}")
