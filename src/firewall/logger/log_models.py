from dataclasses import dataclass


@dataclass
class Log:
    id: str
    timestamp: str
    source: str
    action: str
    protocol: str
    reason: str


@dataclass
class PacketLog:
    src_ip: str
    src_map: str
    dst_ip: str
    dst_map: str
    src_port: int
    dst_port: int


@dataclass
class HttpLog(Log):
    method: str
    url: str
    headers: str | None
    body: str | None
