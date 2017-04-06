import uuid


class ApplicationContext:
    connections = {}


class Connection:
    id = ''
    name = ''
    region = ''
    aws_secret_access_key = ''
    aws_access_key_id = ''

    def __init__(self, name, aws_secret_access_key, aws_access_key_id, region):
        self.id = str(uuid.uuid4())
        self.name = name
        self.aws_secret_access_key = aws_secret_access_key
        self.aws_access_key_id = aws_access_key_id
        self.region = region

    def __hash__(self):
        return self.name.__hash__()

    def __cmp__(self, other):
        return self.name == other.name


context = ApplicationContext()
main_window = None
