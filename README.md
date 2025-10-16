# P-th Prime Finder

## Summary

This is a minimal, working application to find the *p*-th prime number. It consists of two main components:

1.  A command-line Python script (`main.py`) for backend or terminal usage.
2.  An interactive web interface (`index.html`) for a user-friendly experience, running entirely on the client-side.

## Setup

No complex setup or external libraries are required.

### Python Script

-   You need Python 3.x installed on your system.
-   Save the `main.py` file to your local machine.

### Web Interface

-   No setup is needed. Simply open the `index.html` file in any modern web browser.

## Usage

### Command-Line

To run the Python script, open your terminal or command prompt, navigate to the directory where you saved `main.py`, and run the following command:

```sh
python main.py <p>
```

Replace `<p>` with the position of the prime number you want to find.

**Example:**

```sh
python main.py 10
# Output: The 10th prime number is: 29

python main.py 10001
# Output: The 10001th prime number is: 104743
```

### Web Interface

1.  Open `index.html` in your web browser.
2.  Enter a positive integer into the input field.
3.  Click the "Find Prime" button.
4.  The result will be displayed below the button. For large numbers, there might be a short delay as the browser performs the calculation.

## Code Explanation

### `main.py`

-   **`is_prime(n)`**: This function checks if a given number `n` is prime. It uses an optimized trial division algorithm that skips multiples of 2 and 3.
-   **`find_pth_prime(p)`**: This is the core function. It iterates through odd numbers, using `is_prime()` to identify primes, and counts them until it finds the *p*-th one.
-   **`if __name__ == "__main__":`**: This block handles the command-line execution. It parses the command-line arguments, calls `find_pth_prime()`, and prints the result or an error message.

### `index.html`

-   **HTML**: Provides the basic structure, including a title, an input form for the number `p`, a submit button, and a container to display the result.
-   **CSS**: Minimal inline CSS is included in a `<style>` tag to provide a clean and centered layout for better user experience.
-   **JavaScript**: The entire prime-finding logic is replicated in JavaScript within the `<script>` tag. 
    -   An event listener on the form's `submit` event prevents the page from reloading.
    -   It reads the input value, validates it, and then calls a JavaScript implementation of the prime-finding algorithm.
    -   The result is dynamically inserted into the result container on the page. The entire application runs in the browser without needing a server.

## License

This project is licensed under the MIT License. See the LICENSE file for details (if one were included). In short, you are free to use, modify, and distribute this software.
