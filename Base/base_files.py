

def customer_profile_pic_upload(instance, filename):
    return 'user_{0}/{1}'.format(instance.id, filename)


def product_image_upload(instance, filename):
    return 'user_{0}/{1}'.format(instance.id, filename)

