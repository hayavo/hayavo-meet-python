from typing import Dict, Optional, Any
from ..exceptions import ValidationError


class CallService:
    def __init__(self, http, config):
        self.http = http
        self.config = config

    
    async def start(self, **payload):

        media = payload.pop("media", None)

        if media:
            audio = media.get("audio", True)
            video = media.get("video", True)
            screen = media.get("screen", False)
        else:
            audio = payload.pop("audio", True)
            video = payload.pop("video", True)
            screen = payload.pop("screen", False)

        if video and not self.config.allow_video:
            raise ValidationError("Video feature not allowed")

        if audio and not self.config.allow_audio:
            raise ValidationError("Audio feature not allowed")

        if screen and not self.config.allow_screen:
            raise ValidationError("Screen sharing not allowed")

        payload["media"] = {
            "audio": audio,
            "video": video,
            "screen": screen,
        }

        return await self.http.post(
            "/rtc/call/start",
            payload,
            auth_required=True
    )

   
    async def generate_host_token(
            self, 
            call_id: str,
            display_name: Optional[str] = None,
            attributes: Optional[Dict[str, str]] = None,
            ):

        payload = {
            "call_id": call_id,
        }

        if display_name is not None:
            payload["display_name"] = display_name

        if attributes is not None:
            payload["attributes"] = attributes


        return await self.http.post(
            "/rtc/call/token",
            payload,
            auth_required=True
        )

    
    async def generate_guest_token(
            self, 
            call_id: str, 
            app_id: str,
            display_name: Optional[str] = None,
            attributes: Optional[Dict[str, str]] = None,
            ):

        payload = {
            "call_id": call_id,
            "app_id": app_id
        }

        if display_name is not None:
            payload["display_name"] = display_name

        if attributes is not None:
            payload["attributes"] = attributes

        return await self.http.post(
            "/create/call/guest/token",
            payload,
            auth_required=False
        )

    
    async def end(self, call_id: str):
        return await self.http.post(
            "/rtc/call/end",
            {"call_id": call_id},
            auth_required=True
        )

    
    async def mute_participant(self, call_id: str, identity: str, mute: bool = True):
        return await self.http.post(
            f"/rtc/call/{call_id}/mute",
            {"identity": identity, "mute": mute},
            auth_required=True
        )

    async def disable_participant_video(self, call_id: str, identity: str, disable: bool = True):
        return await self.http.post(
            f"/rtc/call/{call_id}/video-off",
            {"identity": identity, "disable": disable},
            auth_required=True
        )


    async def remove_participant(self, call_id: str, identity: str):
        return await self.http.post(
            f"/rtc/call/{call_id}/kick",
            {"identity": identity},
            auth_required=True
        )