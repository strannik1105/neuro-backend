import vk_api
from FatherApi import FatherApi


class VkApi(FatherApi):

    def __init__(self, token, group_id):
        self.api = vk_api.VkApi(token=token)
        self.event = self.api.get_api()
        self.upload = vk_api.VkUpload(self.api)
        self.group_id = group_id

    def generate_post(self):
        super().generate_post()

        photos = self.upload.photo_wall(self._upload_list)
        for photo in photos:
            owner_id = photo['owner_id']
            photo_id = photo['id']
            access_key = photo['access_key']
            self._attachments.append(f'photo{owner_id}_{photo_id}_{access_key}')

        attachment = ','.join(self._attachments)
        self.event.wall.post(owner_id=self.group_id, message=self._text, attachments=f"{attachment}")

