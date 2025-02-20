import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32

class MiSubscriptor(Node):
    def __init__(self):
        super().__init__('mi_subscriptor')
        self.subscription = self.create_subscription(Int32, 'andres2', self.listener_callback, 10)
        self.subscription

    def listener_callback(self, msg2):
        self.get_logger().info('Recived: "%s"' % msg2.data)

def main(args=None):
    rclpy.init(args=args)
    mi_nodo = MiSubscriptor()
    rclpy.spin(mi_nodo)
    mi_nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()