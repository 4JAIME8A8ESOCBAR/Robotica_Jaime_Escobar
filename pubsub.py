# CREACION DE NODO "PUBLICADOR Y SUBCRIPTOR"
import rclpy
from rclpy.node import Node 

from std_msgs.msg import String # Se importan tipo s de mensajes "String"
from std_msgs.msg import Int32 # Se importan tipo s de mensajes "String"

class MiNodoPublicadorSubscriptor(Node):

    def __init__(self):
        super().__init__('mi_nodo_publicador_subscriptor')
        self.publisher = self.create_publisher(Int32, 'andres2', 10)  # creacion del Topico (qt_size)
        time_period = 0.5 # definir el tiempo de publicar 
        self.timer = self.create_timer(time_period, self.timer_callback)# instancia del tiempo en que se publicar a el timer
        self.j = 0

        self.subscription = self.create_subscription(String, 'andres1', self.listener_callback, 10)
        self.subscription

    def listener_callback(self, msg1):
        self.get_logger().info('Recived: "%s"' % msg1.data)

    def timer_callback(self):
        msg2 = Int32()
        msg2.data = self.j

        self.publisher.publish(msg2)
        self.get_logger().info('Publicado: "%s"' % msg2.data)
        self.j +=2

def main(args=None):
    rclpy.init(args=args)
    mi_nodo = MiNodoPublicadorSubscriptor() # se instancia toda la abtraccionde l nodo 
    rclpy.spin(mi_nodo)  # Hace que Corra para siempre es infinito a menos de una iterrupcion por teclado
    mi_nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()



