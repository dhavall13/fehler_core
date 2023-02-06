# Fehler API - Django Backend

Fehler is a project management software which let teams plan, track and manage software developement
projects.

This is the fehler REST API developed to provide and store data for [Fehler Website](https://github.com/givek/fehler_web/).

## Technologies

- Python
- Django
- Django Rest Framework

## Getting Started

To get a local copy up and running follow these simple steps:

### Prerequisites

- Python 3.

  ```shell
  $ sudo apt install python3.8
  ```

### Installation

1. Create a local copy of this git repository with `git clone` command.

   ```shell
   $ git clone https://github.com/givek/fehler_core.git
   ```

2. Create a Virtual Enviornment with the `venv` module.

   ```shell
   $ python3 -m venv venv
   ```

3. Once you’ve created a virtual environment, you may activate it.

   ```shell
   $ source venv/bin/activate
   ```

4. Now, install the requirements from the `requirements.txt` file.

   ```shell
   $ pip install -r requirements.txt
   ```

5. Now, apply the migrations with the management command.

   ```shell
   $ python manage.py migrate
   ```

6. Finally, start the developement server with the management commnad.

   ```shell
   $ python manage.py runserver
   ```

## Entity-Relationship Diagram

Created with [Lucidchart](https://www.lucidchart.com/)

![fehler-schema](images/fehler-system-design.png)

## Screenshots

- Spaces
  ![Spaces](images/spaces.png)

- Projects
  ![Projects](images/projects.png)

- Kanban Board
  ![Kanban Board](images/kanban-board.png)

- Risk Register
  ![Risk Register](images/risk-register.png)

- Risk Matrix
  ![Risk Matrix](images/risk-matrix.png)

## Authors

- Vivek Gandharkar - [givek](https://github.com/givek/)
- Dhaval Chaudhari - [dhavall13](https://github.com/dhavall13/)

## License

This project is licensed under the MIT License - see the [LICENSE](../main/LICENSE) file for details
