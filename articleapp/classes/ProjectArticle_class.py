from .ABC import Article


# ProjectArticle
class ProjectArticle(Article):
    def __init__(self):
        super(ProjectArticle, self).__init__()
        self._like = 0

    def like(self):
        self._like += 1

    def unlike(self):
        self._like -= 1
        if self._like < 0:
            self._like = 1

    def update(self, target, data):
        pass

    def delete(self):
        pass

    def report(self):
        pass

    def contact(self):
        pass

    def make(self, data):
        pass


