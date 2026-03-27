from nautobot.apps.jobs import Job, register_jobs

class TestJob(Job):
    class Meta:
        name = "Test Job"

    def run(self):
        self.logger.info("SSOT repo works")

register_jobs(TestJob)
