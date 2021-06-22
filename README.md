# Property-based Testing with Hypothesis

Best seen in the following order:
 - `encode_decode.py`: directly uses an example provided in the hypothesis library documentation, and shows the elegance of property-based testing.
 - `smoothness.py`: lets students learn about minimum/maximum values in hypothesis, and gives them an opportunity to think about how to implement a property.
 - `triangle.py`: use the `assume` construct of hypothesis to learn about how to filter out the unwanted parts of the input space.
 - `complex_inputs.py`: use the `builds` construct of hypothesis to learn about how to make more complex inputs with hypothesis.

# Dependencies

Use the `requirements.txt` to install the following dependencies:

- `hypothesis`
- `pytest`
 
You can do `pip install -r requirements.txt` to install all dependencies in `requirements.txt`.

# How to execute the test cases

Ensure that your test functions start with `test_` prefix. Then, do the following to execute test functions in `target.py`, for example.

```
python3 -m pytest target.py
```
