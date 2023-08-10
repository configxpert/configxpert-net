class noPassword:
    def __init__(self, configuration):
        self.configuration = configuration

    def check(self):
        # Check for the absence of a password configuration
        for line in self.configuration.splitlines():
            if "password" in line.lower():
                # password configuration is present
                return "Pass"
        return "Fail"
