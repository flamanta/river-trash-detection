import tensorflow as tf
import sys
import os

# Disable tensorflow compilation warnings
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

image_path = "testing"
num_list = []
for i in range(1, 31, 1):
    test = "testing"
    fileformat = ".jpg"
    i = str(i)
    image_path = test + i + fileformat

    if image_path:

        # Read the image_data
        image_data = tf.compat.v1.gfile.FastGFile(image_path, "rb").read()

        # Loads label file, strips off carriage return
        label_lines = [
            line.rstrip() for line in tf.io.gfile.GFile("tf_files/retrained_labels.txt")
        ]

        # Unpersists graph from file
        with tf.compat.v1.gfile.FastGFile("tf_files/retrained_graph.pb", "rb") as f:
            graph_def = tf.compat.v1.GraphDef()
            graph_def.ParseFromString(f.read())
            _ = tf.import_graph_def(graph_def, name="")

        with tf.compat.v1.Session() as sess:
            # Feed the image_data as input to the graph and get first prediction
            softmax_tensor = sess.graph.get_tensor_by_name("final_result:0")

            predictions = sess.run(
                softmax_tensor, {"DecodeJpeg/contents:0": image_data}
            )

            # Sort to show labels of first prediction in order of confidence
            top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

            with open("Outputs.txt", "a+") as text_file:
                for node_id in top_k:
                    human_string = label_lines[node_id]
                    score = predictions[0][node_id]
                    print("%s (score = %.5f)" % (human_string, score))

                    text_file.write("%s (score = %.5f)" % (human_string, score))
                    text_file.write("\n")
                text_file.write("\n")
