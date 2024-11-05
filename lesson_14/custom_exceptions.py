class GroupLimitError(Exception):
    """Exception raised when more than 10 students are added to a group."""
    def __init__(self, message="The group can't have more than 10 students."):
        self.message = message
        super().__init__(self.message)
