import requests


class FatherApi:

    _upload_list = []
    _text = ""
    _model_data = {}
    _attachments = []

    def generate_post(self):
        pass

    def download_images(self):
        count = 1
        for link in self._model_data['output_img']:
            image = requests.get(link)
            out = open(f"{count}.jpg", "wb")
            out.write(image.content)
            out.close()
            self._upload_list.append(f"{count}.jpg")
            count += 1

    def generate_text(self):
        _text = ' '.join(self._model_data['output_text'])
        print(_text)

    def get_model_data(self, data: dict):
        self._model_data = data
