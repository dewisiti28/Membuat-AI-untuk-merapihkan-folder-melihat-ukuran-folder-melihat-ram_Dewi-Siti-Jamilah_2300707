class Command:
    def __init__(self, folder=None, organize=False, size=False, check_ram=False):
        self.folder = folder
        self.organize = organize
        self.size = size
        self.check_ram = check_ram

    def __repr__(self):
        return (
            f"Command(folder={self.folder}, organize={self.organize}, "
            f"size={self.size}, check_ram={self.check_ram})"
        )
