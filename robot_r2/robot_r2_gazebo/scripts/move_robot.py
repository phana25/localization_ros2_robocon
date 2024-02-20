#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose
from action_msgs.msg import GoalStatus

class MoveRobotNode(Node):
    def __init__(self):
        super().__init__('move_robot')
        self.client = ActionClient(self, NavigateToPose, '/NavigateToPose')
        
    def send_goal(self, x_goal, y_goal):
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose.pose.position.x = x_goal
        goal_msg.pose.pose.position.y = y_goal
        goal_msg.pose.pose.orientation.w = 1.0
        goal_msg.pose.header.frame_id = 'map'
        goal_msg.pose.header.stamp = self.get_clock().now().to_msg()

        self.client.wait_for_server()

        self.goal_future = self.client.send_goal_async(goal_msg)
        self.goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')

        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self.goal_result_callback)

    def goal_result_callback(self, future):
        result = future.result().result
        status = future.result().status
        if status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info('Goal succeeded! Result: {0}'.format(result.sequence))
        else:
            self.get_logger().info('Goal failed with status code: {0}'.format(status))

def main(args=None):
    rclpy.init(args=args)

    move_robot_node = MoveRobotNode()

    # Replace x_goal and y_goal with your desired coordinates
    x_goal = 1.0
    y_goal = 2.0
    move_robot_node.send_goal(x_goal, y_goal)

    rclpy.spin(move_robot_node)

    move_robot_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()