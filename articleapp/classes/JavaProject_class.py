from ABC import Project


class PythonProject(Project):
    def __init__(self):
        super(PythonProject, self).__init__()

    def make_project(self, title, leader, stack, due_date, desc, tool):
        self.set_title(title)
        self.set_leader(leader)
        self.set_stack(stack)
        self.set_due_date(due_date)
        self.set_desc(desc)
        self.set_tool(tool)

    def delete_project(self):
        pass

    def update_project(self):
        pass

    def see_now(self):
        pass
