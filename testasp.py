from aylienapiclient import textapi

client = textapi.Client("6b9ec271", "3229130c0fb3ab4b3d09a432a7ebcb0a")

text = "bad experience due to flight delay"
absa = client.AspectBasedSentiment({'domain': 'airlines', 'text': text})
for aspect in absa['aspects']:
  print(aspect)
print(client.RateLimits())
