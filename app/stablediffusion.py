import replicate

def getimage(text):
    model = replicate.models.get("stability-ai/stable-diffusion")
    version = model.versions.get("27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478")
    return version.predict(prompt=text)