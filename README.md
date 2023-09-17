# ActiViz

ActiViz is a web application that allows users to visualize the output of different activation functions used in neural networks. Activation functions are a fundamental component of neural networks, influencing how a neuron's output is calculated based on its input. This tool enables users to select an activation function and input value to see the function's output graph and description.

To try out the live demo, visit [here](http://muthupalaniappan.pythonanywhere.com/).


## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Sample Outputs](#sample-outputs)
- [Contributing](#contributing)
- [License](#license)

## Features

- Visualization of four popular activation functions:
  - Sigmoid
  - ReLU (Rectified Linear Unit)
  - Tanh (Hyperbolic Tangent)
  - Leaky ReLU (Leaky Rectified Linear Unit)
- Input a specific value to see the function's output at that point.
- Descriptions of each activation function, explaining their characteristics and use cases.

## Getting Started

To get started with ActiViz, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   https://github.com/MuthuPalaniappan925/Acti-Viz.git
   ```

2. Install the required Python packages. You can use `pip` for this:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   flask run
   ```

4. Access the application in your web browser at `http://localhost:5000`.

## Usage

1. Upon opening the ActiViz web application, you'll see a form that allows you to select an activation function from a dropdown list.

2. Enter a specific value for `x` in the provided input field.

3. Click the "Plot" button to visualize the selected activation function's output graph and description.

4. The graph will display the function's behavior in the range of -10 to 10, including a marker at the specific value you entered.

5. You'll also see a description of the selected activation function, explaining its characteristics and use cases.


## Sample Outputs




## Contributing

If you would like to contribute to ActiViz, please follow these steps:

1. Fork the repository on GitHub.

2. Clone your forked repository to your local machine:

   ```bash
   https://github.com/MuthuPalaniappan925/Acti-Viz.git
   ```

3. Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature-name
   ```

4. Make your changes and commit them with clear, concise commit messages:

   ```bash
   git commit -m "Add feature / fix bug"
   ```

5. Push your changes to your GitHub repository:

   ```bash
   git push origin feature-name
   ```

6. Create a pull request from your branch to the main repository.

7. Wait for your pull request to be reviewed and merged.

## License

This project is licensed under the MIT License
