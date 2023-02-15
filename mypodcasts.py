import getpodcast

opt = getpodcast.options(
    date_from='2021-01-01',
    root_dir='./podcast')

podcasts = {
    "SGU": "https://feed.theskepticsguide.org/feed/sgu"
}

getpodcast.getpodcast(podcasts, opt)

