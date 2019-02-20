
## Prerequisites
Tested on the following

| Dependencies | Versions |
| ------------ | -------- |
| PHP          | 5.6.3    |
| Compose      | 1.8.4    |
| RabbitMQ     | 3.7.12   |
| Python       | 3.6.2    |
| Virtualenv   | 15.1.0   |

## Getting started
1. Install php dependenices 
    ```bash
    cd consumer
    composer install
    ```
1. Create Consumer Python virtualenv
    ```bash
    cd producer
    virtualenv --python=<$PATH_TO_PYTHON3.6> rabbitmq-env/
    ```
1. Activate virtualenv
    ```bash
    source rabbitmq-env/bin/activate
    ```
1. Install python dependenices 
    ```bash
    pip install pika
    ```

## Running the Basic 
1. Run python consumer 
    ```bash
    cd consumer/src/basic
    python receive.py
    ```

1. Run php producer 
    ```bash
    cd producer/src/basic
    python send.php
    ```

## Running the Queue  
1. Run python consumer 
    ```bash
    cd consumer/src/queue
    python worker.py
    ```

1. Run php producer 
    ```bash
    cd producer/src/queue
    python new_task.php
    ```

## Deployment
1. Copy build folder to webserver root `/var/www/html` for Apache, `/usr/share/nginx/html` for Nginx

## Built With
* [RabbitMQ](https://www.rabbitmq.com)

## Contributing
## Versioning 
## Authors
* **Philip Sales** - *adopted work*
## License
This project is licensed under the Creative Commons- see the Types of [Licenses](https://opensource.org/licenses/alphabetical) 
## Acknowledgments
* [RabbitMQ](https://www.rabbitmq.com)

