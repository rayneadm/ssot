print("LOADED TEST_JOB MODULE")
from nautobot.apps.jobs import Job

class TestJob(Job):
    class Meta:
        name = "Test Job"

    def run(self):
        self.logger.info("SSOT repo works")
