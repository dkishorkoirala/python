class InstagramPost:
    def post(self):
        print("Posting to Instagram...")


class Tweet:
    def post(self):
        print("Posting to Twitter...")


for m in [InstagramPost(), Tweet()]:
    m.post()
