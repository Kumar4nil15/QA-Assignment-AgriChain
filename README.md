**Test Cases for the Website (https://agrichain.com)**
##Manual Test Cases
###1.	UI & Usability Testing
o	Verify that the home page loads correctly with the input field and submit button.
o	Check the alignment and visibility of all UI elements on different screen sizes.
o	Ensure the input field allows user input and the submit button is clickable.
o	Validate that the navigation to the result page happens correctly after submission.
o	Confirm the responsiveness of the website across different browsers and devices.
o	Verify error messages for empty input, special characters, and non-string inputs.
###2.	Functional Testing
o	Enter a valid string (e.g., "abcabcbb") and verify that the correct output (3) is displayed.
o	Check with a string having all unique characters (e.g., "abcdef") and expect output equal to the length of the string.
o	Enter a string with repeating characters (e.g., "bbbbbb") and validate that output is 1.
o	Submit an empty string and ensure proper error handling.
o	Test with long strings to check performance and handling.
###3.	Negative Test Cases
o	Enter numbers ("123456") and verify if the site handles it correctly.
o	Input special characters ("@#$%^"), verify behavior.
o	Test navigation by pressing the back button after submission.
o	Refresh the result page and check if the result persists or resets.
