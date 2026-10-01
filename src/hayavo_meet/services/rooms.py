from typing import Dict, Optional, Any
class RoomService:

    def __init__(self, http):
        self.http = http

    async def create(self, **payload):

        if "room_name" not in payload:
            raise ValueError("room_name is required")

        payload.setdefault("mode", "hm_default_meet_room")
        payload.setdefault("max_participants", 5)

        return await self.http.post(
            "/rtc/room/create",
            payload,
            auth_required=True
    )

    async def generate_host_token(
            self, 
            room_name: str,
            display_name: Optional[str] = None,
            attributes: Optional[Dict[str, str]] = None,
            ):

        payload = {
            "room_name": room_name,
        }

        if display_name is not None:
            payload["display_name"] = display_name

        if attributes is not None:
            payload["attributes"] = attributes

        return await self.http.post(
            "/rtc/room/token/host",
            payload,
            auth_required=True,
        )
        

    async def generate_guest_token(
            self, 
            room_name: str, 
            app_id: str,
            display_name: Optional[str] = None,
            attributes: Optional[Dict[str, str]] = None,
            ):

        payload = {
            "room_name": room_name,
            "app_id": app_id,
        }

        if display_name is not None:
            payload["display_name"] = display_name

        if attributes is not None:
            payload["attributes"] = attributes

        return await self.http.post(
            "/create/room/token/guest",
            payload,
            auth_required=False
        )