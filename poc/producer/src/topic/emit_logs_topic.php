<?php

require_once __DIR__ . '../../../vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;
use PhpAmqpLib\Message\AMQPMessage;

$ip_address = 'localhost';
$port = 5672;
$username = 'guest';
$password = 'guest';
$exchange_type = 'topic';
$exchange_name = 'couchbase_post';

$connection = new AMQPStreamConnection($ip_address, $port, $username, $password);
$channel = $connection->channel();

$channel->exchange_declare($exchange_name, $exchange_type, false, false, false);

$routing_key = isset($argv[1]) && !empty($argv[1]) ? $argv[1] : '*.info';

$data = implode(' ', array_slice($argv, 2));
if (empty($data)) {
    $data = '{ "product_name": "paracetamol", "item": "2" }';
}

$msg = new AMQPMessage($data);

$channel->basic_publish($msg, $exchange_name, $routing_key);

echo ' [x] Sent ', $routing_key, ':', $data, "\n";

$channel->close();
$connection->close();