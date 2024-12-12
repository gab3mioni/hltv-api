from abc import ABC, abstractmethod

class IEventScraper(ABC):
    @abstractmethod
    def get_event_details(self):
        pass