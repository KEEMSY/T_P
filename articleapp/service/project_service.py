from abc import ABC

from project_db_service import find_all_article


# DB 매니저

class Article(ABC):
    def __init__(self):
        self.pk = None
        self.data = None
        self.writer = None

    def load_article(self, pk):
        print('hello')