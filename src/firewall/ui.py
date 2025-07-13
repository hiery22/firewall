from __future__ import annotations

from datetime import datetime
import sys
import asyncio
import threading

from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Input, Static
from src.firewall.command import *


class FirewallUI(App):
    def generate_dummy_message(self):
        self.append_log("It's Dummy Log Message")

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.controller.ui = self
        self.logger = controller.logger
        self.logger.send_ui_log = self.show_log
        self.log_container = Vertical()
        self.command_input = Input(placeholder="enter command")
        self.mounted = asyncio.Event()

    def compose(self) -> ComposeResult:
        yield self.log_container
        yield self.command_input

    def on_mount(self) -> None:
        self.command_input.focus()
        self.mounted.set()

    async def on_input_submitted(self, message: Input.Submitted) -> None:
        cmd = message.value.strip()
        self.command_input.value = ""
        if cmd:
            self.append_log(f"> {cmd}")
            await executeCommand(cmd, self.controller)

    def append_log(self, message: str, now: datetime = None) -> None:
        if now is None:
            now = datetime.now()
        timestamp = str(now)[11:]
        log_line = Static(f"[{timestamp}] {message}")
        self.log_container.mount(log_line)
        self.log_container.scroll_end(animate=False)

    def show_log(self, message: str, now: datetime = None):
        if threading.get_ident() == self._thread_id:
            self.append_log(message, now)
        else:
            self.call_from_thread(self.append_log, message, now)
