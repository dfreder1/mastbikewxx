from mastodon import Mastodon

#   Set up Mastodon
mastodon = Mastodon(
    access_token = 'OSPApam3PpPqzSs3GEBTA15nTN0HKTF0WhT2_XFp9TY',
    api_base_url = 'https://bot.ave5.dev/'
)

mastodon.status_post("hello world!")
