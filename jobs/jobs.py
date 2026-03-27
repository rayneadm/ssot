from nautobot.apps.jobs import Job, ObjectVar
from nautobot.extras.models import ExternalIntegration
from nautobot.extras.choices import SecretsGroupAccessTypeChoices, SecretsGroupSecretTypeChoices

import requests


class NetBoxTestJob(Job):

    source = ObjectVar(
        model=ExternalIntegration,
        label="NetBox Instance",
        required=True
    )

    class Meta:
        name = "NetBox Test API"
        description = "Test connection to NetBox via External Integration"

    def run(self, source):
        self.logger.info(f"Using NetBox: {source.name}")

        url = source.remote_url

        token = source.secrets_group.get_secret_value(
            access_type=SecretsGroupAccessTypeChoices.TYPE_HTTP,
            secret_type=SecretsGroupSecretTypeChoices.TYPE_TOKEN,
        )

        headers = {
            "Authorization": f"Token {token}",
            "Accept": "application/json",
        }

        api_url = f"{url}/api/status/"

        response = requests.get(api_url, headers=headers, timeout=10)

        self.logger.info(f"Status code: {response.status_code}")

        if response.ok:
            self.logger.info(f"Response: {response.json()}")
        else:
            self.logger.error(f"Error: {response.text}")


# 🔥 ВОТ ЭТО КЛЮЧЕВОЕ
jobs = [NetBoxTestJob]
