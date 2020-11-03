import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts

class MyServiceServer(Node):
    def __init__(self):
        super().__init__('server_node')
        self.srv = self.create_service(AddTwoInts, 'add_two_ints_jas', self.add_two_ints_callback)    # service name unique하게 설정 (이름 이니셜)

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info('Incoming request.. a: %d b: %d' % (request.a, request.b))
        return response

def main(args=None):
    rclpy.init(args=args)
    node = MyServiceServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()








