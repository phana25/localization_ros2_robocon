import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose

class MoveRobotNode(Node):
    def __init__(self):
        super().__init__('move_robot')
        self.client = ActionClient(self, NavigateToPose, 'NavigateToPose')

    def send_goal(self, x, y):
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose.pose.position.x = x
        goal_msg.pose.pose.position.y = y
        goal_msg.pose.pose.orientation.w = 1.0  # Assuming the robot should move forward
        goal_msg.pose.header.frame_id = 'map'
        goal_msg.pose.header.stamp = self.get_clock().now().to_msg()

        self.client.wait_for_server()
        self.client.send_goal_async(goal_msg)

def main(args=None):
    rclpy.init(args=args)

    move_robot_node = MoveRobotNode()

    # Replace these with the x and y coordinates you want the robot to move to
    x = 1.0
    y = 2.0
    move_robot_node.send_goal(x, y)

    rclpy.spin(move_robot_node)

    move_robot_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()