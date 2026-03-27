from nautobot.extras.jobs import Job, ObjectVar, register_jobs
from nautobot.extras.models import ExternalIntegration
from nautobot.extras.choices import (
    SecretsGroupAccessTypeChoices,
    SecretsGroupSecretTypeChoices,
)

import requests


class NetBoxTestJob(Job):

    source = ObjectVar(
        model=ExternalIntegration,
        label="NetBox Instance",
        required=True
    )

    class Meta:
        name = "NetBox Test API"

    def run(self, source):
        url = source.remote_url

        token = source.secrets_group.get_secret_value(
            access_type=SecretsGroupAccessTypeChoices.TYPE_HTTP,
            secret_type=SecretsGroupSecretTypeChoices.TYPE_TOKEN,
        )

        response = requests.get(
            f"{url}/api/status/",
            headers={"Authorization": f"Token {token}"},
            timeout=10,
        )

        self.logger.info(response.status_code)


# 🔥 обязательно
register_jobs(NetBoxTestJob)
