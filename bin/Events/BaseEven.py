import random
from abc import ABC, abstractmethod
import pygame
from Settings import hitSound, ScreenWidth
from Projectlite import Projectile


class BaseEven(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def draw(self, win):
        pass


class BaseAttachedEven(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def draw(self, win):
        pass

    @abstractmethod
    def move(self, enemys, player):
        pass

    @abstractmethod
    def get_event(self):
        pass
