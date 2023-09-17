from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

## The List of Activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def tanh(x):
    return np.tanh(x)

def leaky_relu(x, alpha=0.01):
    return np.maximum(alpha * x, x)

@app.route("/", methods=["GET", "POST"])
def index():
    desc = ""
    sig_desc = "The sigmoid activation function maps input values to the range (0, 1). It's often used in the output layer of binary classification models as it can represent probabilities. However, it can suffer from the vanishing gradient problem."
    tanh_desc = "The tanh activation function is similar to the sigmoid but maps input values to the range (-1, 1). It also suffers from the vanishing gradient problem but is zero-centered, making optimization potentially easier."
    relu_desc = " ReLU activation replaces negative values with zero and leaves positive values unchanged. It's widely used in deep learning because of its simplicity and the fact that it mitigates the vanishing gradient problem. However, it can suffer from the dying ReLU problem when neurons get stuck in the zero-activation state."
    l_relu_desc = "Leaky ReLU is a variation of ReLU that allows a small, non-zero gradient for negative inputs. This helps prevent neurons from dying, and it has become a popular choice for many neural network architectures."
    if request.method == "POST":
        
        function_name = request.form["activation_function"]
        if function_name == "sigmoid":
            desc = sig_desc
        elif function_name == "relu":
            desc = relu_desc
        elif function_name == "tanh":
            desc = tanh_desc
        else:
            desc = l_relu_desc
            
        specific_value = float(request.form["specific_value"])
        x = np.linspace(-10, 10, 400)
        plt.figure(figsize=(8, 6))
        plt.plot(x, eval(function_name)(x), label=function_name, linewidth=2)
        plt.scatter(specific_value, eval(function_name)(specific_value), color='red', marker='o',
                    label=f'{function_name}({specific_value}) = {eval(function_name)(specific_value):.4f}')
        plt.title(f'{function_name} Function')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()

        ## Save the plot to a BytesIO object and encode it as base64
        img_stream = BytesIO()
        plt.savefig(img_stream, format='png')
        img_stream.seek(0)
        img_data = base64.b64encode(img_stream.read()).decode()
        img_src = f'data:image/png;base64,{img_data}'
        val = eval(function_name)(specific_value)
        return render_template("index.html", img_src=img_src,val=val,desc=desc)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
