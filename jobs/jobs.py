from nautobot.extras.jobs import Job, register_jobs


class TestJob(Job):
    def run(self):
        self.logger.info("OK")


register_jobs(TestJob)
