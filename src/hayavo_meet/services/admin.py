class AdminService:

    def __init__(self, http):
        self.http = http

    async def remove_participant(self, room: str, identity: str):

        return await self.http.post(
            "/rtc/av/kick",
            {
                "room_name": room,
                "identity": identity
            },
            auth_required=True
        )
        
        

    async def mute_participant(self, room: str, identity: str):

        return await self.http.post(
            "/rtc/video/mute",
            {
                "room_name": room,
                "identity": identity
            },
            auth_required=True
        )
        
        
    async def cleanup_rooms(self, room: str):
        
        return await self.http.post(
            "/rtc/video/end",
            {
                "room_name": room,
            },
            auth_required=True
        )