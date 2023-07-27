from VkApi import VkApi

testData = {
    "output_img": ['https://img3.akspic.ru/previews/5/5/4/1/7/171455/171455-zhivopis-illustracia-art-voda-oblako-500x.jpg'],
    "output_text": 'testing post'
}
user_token = "vk1.a.RLXw_-XXRKKrUMXsxZHFwSn4isM0aw7KTb2l_1KdPhyuH1H-Q0OmZJ2q1N4N1irg10GsbiuCwM_gfnkJeb3zlPHMRIe7XT41AP8FF4hWhV9-rvAPJrdtK4a4gYCBH5qt6wc2vwJhroRFzHuHWVbx1GI2MnP-eacSRvbUxLG1Wwz7rA2MILNiOl4AK2AijipItHzprPCje2_biBcluglpKQ"


test = VkApi(user_token, -214053144)

test.get_model_data(testData)
test.download_images()
test.generate_text()
test.generate_post()

print("Done")