import rospy
import pcl

import laser_geometry.laser_geometry as lg

from sensor_msgs.msg import PointCloud2


class PCLProcess:
    def __init__(self, publish=True):
        self.__lp = lg.LaserProjection()
        self.first_pcl = None
        self.__publish = publish
        if self.__publish:
            self.__pub = rospy.Publisher('pcl_pub', PointCloud2, queue_size=1)

    def preprocess(self, data):
        pc2_msg = self.__lp.projectLaser(data)
        if self.__publish:
            self.__pub.publish(pc2_msg)
        point_cloud = pcl.PointCloud(pc2_msg)
        if self.first_pcl is None:
            print("\nSetting point cloud as first cloud i.e \"cloud\" of reference\n")
            self.first_pcl = pcl.PointCloud(point_cloud)
            return
        return pcl.PointCloud(point_cloud)


if __name__ == '__main__':
    rospy.init_node('pcl_process', anonymous=True)
    PCLProcess()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        exit(0)
