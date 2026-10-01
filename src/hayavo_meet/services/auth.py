class AuthService:

    def __init__(self, http):
        self.http = http

    async def authenticate(self, login: str, password: str):

        return await self.http.post(
            "/rtm/client/token",
            {
                "login": login,
                "password": password
            },
            auth_required=True
        )