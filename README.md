# Gazebo Example for Northwestern's ME450 Embedded Systems in Robotics
This package provides an example/template for creating ROS 2 Python Packages that interact with Gazebo (Modern Gazebo, not Gazebo Classic)
It depends on `ros_gz` and `ros_gz_sim_demos`.

# Files
1. `colcon.pkg` sets up environment variables (when the package workspace is sourced) to enable gazebo to find assets installed by this package
2. `env-hooks/me495_gazebo.dsv` sets the gazebo-relevant values. 
    - It hard-codes the package name instead of using @PROJECT_NAME@ (as in the standard template)
      because this is a python package, and substitution of @PROJECT_NAME@ with the name of the package is a CMake feature.
3. `setup.py` - uses globbing and a custom function to automatically and recursively install files in the `worlds`, `models` and `launch` directories
   - Primarily for convenince, but often gazebo models have nested file structure
4. `models` contains an example model, derived from an existing Fuel model
5. `worlds` contains the example world. It's called `empty.world.sdf` but it does have items in it
6. `launch/example_world.launch.xml` starts the gazebo server with `empty.world.sdf`, optionally starts the gazebo client,
   spawns two models (one from an `sdf` file, one from a `urdf.xacro`), and sets up a `ros_gz_bridge parameter_bridge`.
7. `launch/bridge.yaml` contains the configuration for the bridge
8. `package.xml` If using as a template, you can likely remove the `exec_depend` on `ros_gz_sim_demos`

# Further Reading
[ME450 Gazebo Notes](https://nu-msr.github.com/ros_notes/simulation.html)

[Northwestern MS in Robotics](https://www.mccormick.northwestern.edu/robotics/)
