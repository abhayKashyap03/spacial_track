// Generated by gencpp from file motion_tracker/ImageContour.msg
// DO NOT EDIT!


#ifndef MOTION_TRACKER_MESSAGE_IMAGECONTOUR_H
#define MOTION_TRACKER_MESSAGE_IMAGECONTOUR_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <sensor_msgs/Image.h>
#include <sensor_msgs/Image.h>
#include <sensor_msgs/Image.h>

namespace motion_tracker
{
template <class ContainerAllocator>
struct ImageContour_
{
  typedef ImageContour_<ContainerAllocator> Type;

  ImageContour_()
    : ann_file()
    , frame()
    , prevFrame()
    , gray_frame()  {
    }
  ImageContour_(const ContainerAllocator& _alloc)
    : ann_file(_alloc)
    , frame(_alloc)
    , prevFrame(_alloc)
    , gray_frame(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _ann_file_type;
  _ann_file_type ann_file;

   typedef  ::sensor_msgs::Image_<ContainerAllocator>  _frame_type;
  _frame_type frame;

   typedef  ::sensor_msgs::Image_<ContainerAllocator>  _prevFrame_type;
  _prevFrame_type prevFrame;

   typedef  ::sensor_msgs::Image_<ContainerAllocator>  _gray_frame_type;
  _gray_frame_type gray_frame;





  typedef boost::shared_ptr< ::motion_tracker::ImageContour_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::motion_tracker::ImageContour_<ContainerAllocator> const> ConstPtr;

}; // struct ImageContour_

typedef ::motion_tracker::ImageContour_<std::allocator<void> > ImageContour;

typedef boost::shared_ptr< ::motion_tracker::ImageContour > ImageContourPtr;
typedef boost::shared_ptr< ::motion_tracker::ImageContour const> ImageContourConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::motion_tracker::ImageContour_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::motion_tracker::ImageContour_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::motion_tracker::ImageContour_<ContainerAllocator1> & lhs, const ::motion_tracker::ImageContour_<ContainerAllocator2> & rhs)
{
  return lhs.ann_file == rhs.ann_file &&
    lhs.frame == rhs.frame &&
    lhs.prevFrame == rhs.prevFrame &&
    lhs.gray_frame == rhs.gray_frame;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::motion_tracker::ImageContour_<ContainerAllocator1> & lhs, const ::motion_tracker::ImageContour_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace motion_tracker

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::motion_tracker::ImageContour_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::motion_tracker::ImageContour_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::motion_tracker::ImageContour_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::motion_tracker::ImageContour_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::motion_tracker::ImageContour_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::motion_tracker::ImageContour_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::motion_tracker::ImageContour_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ec56e43facaaa5042c6f1314b2415932";
  }

  static const char* value(const ::motion_tracker::ImageContour_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xec56e43facaaa504ULL;
  static const uint64_t static_value2 = 0x2c6f1314b2415932ULL;
};

template<class ContainerAllocator>
struct DataType< ::motion_tracker::ImageContour_<ContainerAllocator> >
{
  static const char* value()
  {
    return "motion_tracker/ImageContour";
  }

  static const char* value(const ::motion_tracker::ImageContour_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::motion_tracker::ImageContour_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string ann_file\n"
"sensor_msgs/Image frame\n"
"sensor_msgs/Image prevFrame\n"
"sensor_msgs/Image gray_frame\n"
"\n"
"================================================================================\n"
"MSG: sensor_msgs/Image\n"
"# This message contains an uncompressed image\n"
"# (0, 0) is at top-left corner of image\n"
"#\n"
"\n"
"Header header        # Header timestamp should be acquisition time of image\n"
"                     # Header frame_id should be optical frame of camera\n"
"                     # origin of frame should be optical center of camera\n"
"                     # +x should point to the right in the image\n"
"                     # +y should point down in the image\n"
"                     # +z should point into to plane of the image\n"
"                     # If the frame_id here and the frame_id of the CameraInfo\n"
"                     # message associated with the image conflict\n"
"                     # the behavior is undefined\n"
"\n"
"uint32 height         # image height, that is, number of rows\n"
"uint32 width          # image width, that is, number of columns\n"
"\n"
"# The legal values for encoding are in file src/image_encodings.cpp\n"
"# If you want to standardize a new string format, join\n"
"# ros-users@lists.sourceforge.net and send an email proposing a new encoding.\n"
"\n"
"string encoding       # Encoding of pixels -- channel meaning, ordering, size\n"
"                      # taken from the list of strings in include/sensor_msgs/image_encodings.h\n"
"\n"
"uint8 is_bigendian    # is this data bigendian?\n"
"uint32 step           # Full row length in bytes\n"
"uint8[] data          # actual matrix data, size is (step * rows)\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
;
  }

  static const char* value(const ::motion_tracker::ImageContour_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::motion_tracker::ImageContour_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.ann_file);
      stream.next(m.frame);
      stream.next(m.prevFrame);
      stream.next(m.gray_frame);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ImageContour_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::motion_tracker::ImageContour_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::motion_tracker::ImageContour_<ContainerAllocator>& v)
  {
    s << indent << "ann_file: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.ann_file);
    s << indent << "frame: ";
    s << std::endl;
    Printer< ::sensor_msgs::Image_<ContainerAllocator> >::stream(s, indent + "  ", v.frame);
    s << indent << "prevFrame: ";
    s << std::endl;
    Printer< ::sensor_msgs::Image_<ContainerAllocator> >::stream(s, indent + "  ", v.prevFrame);
    s << indent << "gray_frame: ";
    s << std::endl;
    Printer< ::sensor_msgs::Image_<ContainerAllocator> >::stream(s, indent + "  ", v.gray_frame);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MOTION_TRACKER_MESSAGE_IMAGECONTOUR_H
