# Automation Test Cases
## Valid Input Tests

> - Verify correct output for "abcabcbb", "pwwkew", and "bbbbb".

> - Test different valid inputs and assert correct outputs.

## Invalid Input Handling

> - Automate cases where the user enters an empty string, numbers, or special characters and validate error messages.

## Navigation Testing

> - Automate the flow of entering input, clicking submit, and validating the navigation to the result page.

> - Ensure that using the back button retains the previous input.

> - Cross-browser Testing

> - Run the tests on Chrome, Firefox, and Edge to ensure compatibility.

## Automation Script for One Test Case
> - Test Case:
> - Verify Longest Substring Calculation for Input "abcabcbb"
> - This script will:
> - Launch the browser and open https://agrichain.com.
> - Enter "abcabcbb" in the input field.
> - Click the submit button.
> - Verify that the result page displays 3.



## Execution
> - Install dependencies:
pip install selenium pytest

## Run the test:
> - pytest tests/test_longest_substring.py
