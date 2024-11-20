import rclpy
from rclpy.node import Node
<<<<<<< HEAD
from person_msgs.msg import Person

rclpy.init()
node =  Node("talker")
pub = node.create_publisher(Person, "person", 10)
=======
from std_msgs.msg import Int16

rclpy.init()
node =  Node("talker")
pub = node.create_publisher(Int16, "countup", 10)
>>>>>>> 7c3505a... make new Repositories
n = 0


def cb():
    global n
<<<<<<< HEAD
    msg = Person()
    msg.name = "野田琉晟"
    msg.age = n
=======
    msg = Int16()
    msg.data = n
>>>>>>> 7c3505a... make new Repositories
    pub.publish(msg)
    n += 1


def main():
    node.create_timer(0.5, cb)
    rclpy.spin(node)
