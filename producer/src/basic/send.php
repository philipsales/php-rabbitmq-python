<?php 
require_once __DIR__ . '../../../vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;
use PhpAmqpLib\Message\AMQPMessage;

$ip = 'localhost';
$port = 5672;
$username = 'guest';
$password = 'guest';

$connection = new AMQPStreamConnection($ip, $port, $username, $password);
$channel = $connection->channel();

$queue_name = 'hello';
$channel->queue_declare($queue_name, false, false, false, false);

$queue_msg = "hello world";
$msg = new AMQPMessage($queue_msg);
$channel->basic_publish($msg, '', 'hello');

echo " [x] Sent 'Hello World!'\n";

$channel->close();
$connection->close();
?>