import tensorflow as tf
# step 1
filenames = ['0a69b4b15b1511e78d4dc5a5765a83e8.jpg',
             '0a3673b15ae911e7a3c0c5a5765a83e8.jpg',
             '0aa2ae815ba311e79875c5a5765a83e8.jpg',
             '0af3ea704b4a11e7b601c5a5765a83e8.jpg']

filenames=['E:\\learn\\dogcat\\alldata\\train\person\\'+filename for filename in filenames]
# step 2
filename_queue = tf.train.string_input_producer(filenames)

# step 3: read, decode and resize images
reader = tf.WholeFileReader()
filename, content = reader.read(filename_queue)
image = tf.image.decode_jpeg(content, channels=3)
image = tf.cast(image, tf.float32)
resized_image = tf.image.resize_images(image, [224, 224])

# step 4: Batching
image_batch = tf.train.batch([resized_image], batch_size=8)
print(image_batch)