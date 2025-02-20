import rclpy
from rclpy.node import Node 

#importar el tipo de mesnaje con el cual el node va a crear
from std_msgs.msg import String # Se importan tipo s de mensajes "String"
#para umportat cada node siempre va a aestar enscpsulado 
#siempre cuadno se crea el node se cra lo siguiente en si:
class MiNodoPublicador(Node):

    def __init__(self):
        super().__init__('mi_nodo_publicador')
        self.publisher = self.create_publisher(String, 'andres1', 10)  # creacion del Topico (qt_size)
        time_period = 0.5 # definir el tiempo de publicar 
        self.timer = self.create_timer(time_period, self.timer_callback)# instancia del tiempo en que se publicar a el timer
        self.i =0

    def timer_callback(self):
        msg1 = String()
        msg1.data = 'Hola clase ucb: %d' % self.i

        self.publisher.publish(msg1)
        self.get_logger().info('Publicado: "%s"' % msg1.data)
        self.i +=1

def main(args=None):
    rclpy.init(args=args)
    mi_nodo = MiNodoPublicador() # se instancia toda la abtraccionde l nodo 
    rclpy.spin(mi_nodo)  # Hace que Corra para siempre es infinito a menos de una iterrupcion por teclado
    mi_nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()



