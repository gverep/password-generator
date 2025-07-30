# Password Generator

This project is a command-line application that can generate both **deterministic** and **random** passwords. The passwords can be created with a specified length and a customizable set of character pools (uppercase letters, digits, special characters).

## Features

- **Deterministic Password Generation**: Generates the same password every time with the same `secret_key` and `subject`.
- **Random Password Generation**: Random passwords can be created.
- **Character Pools**: Includes uppercase letters, digits, and special characters.
- **HMAC-based deterministic password generation**.


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/gverep/password-generator.git
    cd password_generator
    ```

2. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Install the package:
    ```sh
    pip install .
    ```

## Usage

Generate a random password:
```sh
generate-password 12
```

Generate a deterministic password:
```sh
generate-password 12 --secret-key "mysecretkey" --subject "mysubject"
```

For more options, use the following command:
```sh
generate-password --help
```

## Tests

To run the tests, use:
```sh
pytest
```

## License

This project is licensed under the [MIT](LICENSE) License.