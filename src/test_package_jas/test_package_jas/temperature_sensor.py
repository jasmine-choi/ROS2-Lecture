import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int64
import random

class TemperatureSensor(Node) :
    def __init__(self) :
        super().__init__('temperature_sensor')
        self.publisher_ = self.create_publisher(Int64, 'temperature_jas', 10)
        self.timer = self.create_timer(1, self.publish_temperature)
        
    def publish_temperature(self) :
        temperature = random.randint(20,30)
        msg = Int64()
        msg.data = temperature
        self.publisher_.publish(msg)
        self.get_logger().info('Temperautre is %d' % msg.data)

def main():
    rclpy.init()
    print('Hi from test_package.')
    node = TemperatureSensor()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()





