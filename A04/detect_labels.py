def detect_labels_uri(uri):
    """Detects labels in the file located in Google Cloud Storage or on the
    Web."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        print(label.description)

detect_labels_uri('https://scontent-sea1-1.cdninstagram.com/vp/7831adc9c2d624937ec8197b4affcded/5C76DA0B/t51.2885-15/e15/c181.0.718.718/s480x480/44904753_194498844802328_8238377254064471543_n.jpg?ig_cache_key=MTkxMjcyNTE4Njk1Njg2MzM4Mg%3D%3D.2.c')