from dbacademy.dbrest import DBAcademyRestClient

class PermissionsClient:

    def __init__(self, client: DBAcademyRestClient, token: str, endpoint: str):
        self.client = client      # Client API exposing other operations to this class
        self.token = token        # The authentication token
        self.endpoint = endpoint  # The API endpoint

    def get_job_permissions(self, job_id):
        return client.execute_get_json(f"{client.endpoint}/api/2.0/permissions/jobs/{job_id}/permissionLevels")

    def change_job_owner(self, job_id, username):
        params = {
            "access_control_list": [
                {
                    "user_name": username,
                    "permission_level": "IS_OWNER"
                }
            ]
        }
        return self.client.execute_patch(f"{self.endpoint}/permissions/jobs/{job_id}", params)
        