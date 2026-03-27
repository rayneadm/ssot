from nautobot.extras.jobs import Job

class TestSSoT(Job):
    class Meta:
        name = "SSoT Test Job"

    def run(self):
        self.log_info(message="SSoT is working!")
