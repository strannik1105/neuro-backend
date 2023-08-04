from enum import StrEnum, auto


class SocialNetworks(StrEnum):
    VK = auto()
    TG = auto()
    OK = auto()
    DISCORD = auto()
    DZEN = auto()


class Rate(StrEnum):
    BASE = auto()
    IMPROVED = auto()
    MAXIMUM = auto()
