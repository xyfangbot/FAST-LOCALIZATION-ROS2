# FAST-LOCALIZATION ROS 2

This fork ports [YWL0720/FAST-LOCALIZATION](https://github.com/YWL0720/FAST-LOCALIZATION)
at upstream commit `93da4f462b8da16679c18a8aea9545ed4cb3c71b` to ROS 2 Humble on Ubuntu 22.04.
The localization algorithm is unchanged: FAST-LIO2 odometry, Scan Context global candidate
retrieval, two-stage ICP, two-frame consistency checking, global state injection, and the
global ikd-tree localization path remain the upstream implementation.

The ROS 2 interface accepts standard messages:

- `sensor_msgs/msg/PointCloud2`
- `sensor_msgs/msg/Imu`

## Build

Install ROS 2 Humble development dependencies, PCL, and Eigen, then build with colcon:

```bash
source /opt/ros/humble/setup.bash
colcon build --base-paths /path/to/FAST-LOCALIZATION-ROS2
```

## Prior map

The map directory is an explicit runtime parameter and retains the upstream format:

```text
prior-map/
├── pcd/
│   ├── 0.pcd
│   └── 1.pcd
└── pose.json
```

Each line of `pose.json` is `tx ty tz qw qx qy qz`, and PCD IDs are zero-based and
contiguous. No interactive keypress or initial-pose topic is required.

## Run

```bash
source install/setup.bash
ros2 launch fast_localization localization_mid360.launch.py \
  map_dir:=/path/to/prior-map \
  params_file:=/path/to/mid360.yaml
```

The node publishes retained status strings on `/fast_localization/status`:
`map_loading`, `localizing`, `localized`, or `failed`. Topics, frames, and output paths are
parameters in `config/mid360.yaml`.

## Acknowledgments

FAST-LOCALIZATION builds on FAST-LIO2, HBA, Scan Context, and ikd-Tree. The original
authors and license notices are preserved in the source tree.
