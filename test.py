from nautobot.apps.jobs import Job

class TestSSoT(Job):
    class Meta:
        name = "SSoT Test Job"
        description = "Minimal test to verify jobs loading"

    def run(self):
        self.log_info(message="SSoT is working!")
